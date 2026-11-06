# Sending data to an accessory in the background

**Framework**: Accessory Transport Extension  
**Role**: Article

Move data between your accessory and your app when a person’s device is asleep or your app is in the background.

## Overview

The Accessory Transport Extension framework lets your app exchange data with your accessory without waiting for the person to open your app or turn on their iPhone’s screen. Use this capability for tasks like status synchronization or silent preparation for firmware updates.

To implement background data transfer, the framework provides *accessory workers*. Use [`AccessoryWorker`](./accessoryworker.md), or [`AccessoryGPUWorker`](./accessorygpuworker.md) if your app’s background tasks need to use the GPU. Unlike notification forwarding, accessory workers send and receive data in a format that you define. As a result, your app needs to take its own steps to protect sensitive data.

Data can flow from your app to your accessory or from your accessory to your app, and your accessory starts the exchange. The accessory might report a change to your app, such as when a person turns a dial on a thermostat accessory: your companion app shows the new mode the next time the person opens it. Alternatively, the accessory might ask your app for a piece of data when it connects, such as the current weather, and your background [`AccessoryWorker`](./accessoryworker.md) extension then supplies the weather conditions for display on the accessory.

To exchange data in the background, your app implements two extensions:

- **[`AccessoryDataProvider`](./accessorydataprovider.md)**: Declares the worker feature, handles data that the transport extension sends, and can save results to the shared app group container for your companion app.
- **[`AccessoryTransportAppExtension`](./accessorytransportappextension.md)**: Enrolls the worker feature for the accessory, opens a session when your accessory reports a change, and relays data between your accessory and your data provider extension over Bluetooth.

## Declare the worker feature in your data provider extension

Declare the worker feature so the system can route sessions from your transport extension to the correct handler. In your extension’s target properties, add the feature’s `AccessoryWorker/featureID` to the `EXCapabilities` key:

```xml
<plist>
    <dict>
        <key>EXAppExtensionAttributes</key>
        <dict>
            <key>EXExtensionPointIdentifier</key>
            <string>com.apple.accessory-data-provider</string>
            <key>EXCapabilities</key>
            <array>
                <string>AccessoryTransportExtension.AccessoryWorker</string>
            </array>
        </dict>
    </dict>
</plist>
```

In your extension’s Swift code, implement the [`AccessoryDataProvider`](./accessorydataprovider.md) protocol and declare [`AccessoryWorker`](./accessoryworker.md) with a closure that creates your handler:

```swift
import AccessoryTransportExtension

@main
struct DataProvider: AccessoryDataProvider {
    var extensionPoint: AppExtensionPoint {
        Identifier("com.apple.accessory-data-provider")
        Implementing {
            AccessoryWorker {
                ThermostatModeHandler()
            }
        }
    }
}
```

> **Note**: If your app requires the GPU in the background, declare [`AccessoryGPUWorker`](./accessorygpuworker.md) instead and provide a handler that conforms to [`AccessoryGPUWorker.Handler`](./accessorygpuworker/handler.md).

Add the [`com.apple.developer.accessory-data-provider`](../BundleResources/entitlements/com.apple.developer.accessory-data-provider.md) entitlement to your extension.

## Open a session when your accessory reports a change

The system launches or wakes your transport extension when your accessory reports a change, for example, by signaling a Bluetooth event. Your transport extension enrolls a worker feature for the accessory by calling `AccessoryWorker/requestAuthorization(for:)`.

Then your extension calls [`makeFeatureSession(_:)`](./accessorytransportsession/makefeaturesession%28_%29.md) to open a *feature session*, which is a data channel between the transport extension and your data provider extension. The framework scopes communication through this data channel to just the one feature rather than the entire accessory connection.

To prepare information for the next time the accessory connects, such as a firmware file that your companion app downloaded, write it to the shared app group container ahead of time. When the accessory’s Bluetooth connection triggers the next launch, the transport extension reads the information and relays it to the accessory without launching your data provider extension.

The following code demonstrates the [`AccessoryTransportAppExtension`](./accessorytransportappextension.md) acceptance of a session request from the system and then creates a handler for the accessory:

```swift
import AccessorySetupKit

@main
struct TransportExtension: AccessoryTransportAppExtension {
    func accept(sessionRequest: AccessoryTransportSession.Request) -> AccessoryTransportSession.Request.Decision {
        let accessory: ASAccessory = /* The accessory this extension manages, from AccessorySetupKit. */
        return sessionRequest.accept {
            TransportEventHandler(session: sessionRequest.session, accessory: accessory)
        }
    }
}

class TransportEventHandler: AccessoryTransportSession.EventHandler {
    private let session: AccessoryTransportSession
    private let accessory: ASAccessory
    private var modeUpdateSession: AccessoryWorker.FeatureSession?

    init(session: AccessoryTransportSession, accessory: ASAccessory) {
        self.session = session
        self.accessory = accessory
    }
}
```

Add the [`com.apple.developer.accessory-transport-extension`](../BundleResources/entitlements/com.apple.developer.accessory-transport-extension.md) entitlement to your extension’s code signature to use the [`AccessoryTransportAppExtension`](./accessorytransportappextension.md) protocol.

When the accessory reports that the person changed the thermostat’s mode using the physical dial, the handler calls `AccessoryWorker/requestAuthorization(for:)` to enroll the worker feature for the accessory. The system returns an authorized status immediately, without prompting the person:

```swift
func accessoryReportedModeChange(_ mode: Data) async throws {
    let status = try await AccessoryWorker.requestAuthorization(for: accessory)
    guard status == .authorized else {
        return
    }

    let modeUpdateSession = try session.makeFeatureSession {
        ThermostatModeSessionHandler(mode: mode)
    }
    self.modeUpdateSession = modeUpdateSession
    try await modeUpdateSession.activate()
}

func invalidationHandler(error: AccessoryTransportSession.Error?) {
    modeUpdateSession = nil
}
```

> **Note**: To read the status without enrolling, call `AccessoryWorker/authorizationStatus(for:)`. [`AccessoryGPUWorker`](./accessorygpuworker.md) declares the same two methods.

The code checks the status first because returning from [`activate()`](./accessoryfeatureruntimesession/activate%28%29.md) doesn’t mean the session started, and the method doesn’t throw when the feature isn’t enrolled. The system can also decline to launch your data provider extension for the feature session when the device is under heavy load or the battery is low.

Keep your worker sessions brief instead of leaving one open for the entire Bluetooth connection, since the system counts your extension’s battery usage against your app’s battery usage.

## Send the mode change and end the session

When the feature session starts, the system calls [`sessionStarted(_:)`](./accessoryfeatureruntimesessionhandler/sessionstarted%28_%29.md) on the handler you passed to [`makeFeatureSession(_:)`](./accessorytransportsession/makefeaturesession%28_%29.md), which conforms to [`AccessoryWorker.FeatureSession.Handler`](./accessoryworker/featuresession/handler.md). Send the data your accessory reports at that time, then wait for your data provider extension’s acknowledgment before invalidating the session.

The following code sends the thermostat’s new mode as soon as the session starts:

```swift
class ThermostatModeSessionHandler: AccessoryWorker.FeatureSession.Handler {
    private let mode: Data
    private weak var session: AccessoryWorker.FeatureSession?

    init(mode: Data) {
        self.mode = mode
    }

    func sessionStarted(_ session: AccessoryWorker.FeatureSession) {
        self.session = session
        Task {
            try await session.send(data: mode)
        }
    }
}
```

Once the data provider extension confirms the data write, the handler tears down the session:

```swift
func dataReceived(_ data: Data) {
    session?.invalidate()
}

func sessionInvalidated(error: (any Error)?) {
    session = nil
}
```

The data provider extension in this example acknowledges completion by sending back an empty `Data` value, although you choose the exact signal. Check whether the [`dataReceived(_:)`](./accessoryfeatureruntimesessionhandler/datareceived%28_%29.md) payload is empty before parsing it, to tell a completion acknowledgment apart from new data.

## Save the mode change in your data provider extension

When the transport extension’s [`AccessoryWorker.FeatureSession`](./accessoryworker/featuresession.md) starts, the system begins a matching [`AccessoryWorker.Session`](./accessoryworker/session.md) in your data provider extension and calls [`sessionStarted(_:)`](./accessoryfeaturesessionhandler/sessionstarted%28_%29.md) on the handler you declare in `extensionPoint`. When the transport extension sends data, the system delivers it to the handler’s [`dataReceived(_:)`](./accessoryfeaturesessionhandler/datareceived%28_%29.md) method.

> ❗ **Important**: Your companion app receives updates from the accessory in the shared app group container and only [`AccessoryWorker`](./accessoryworker.md) can write to it. For more information, see [`AccessoryDataProvider`](./accessorydataprovider.md).

The following code saves the thermostat’s new mode to the shared container and sends an empty acknowledgment to the transport extension:

```swift
class ThermostatModeHandler: AccessoryWorker.Handler {
    private weak var session: AccessoryWorker.Session?

    func sessionStarted(_ session: AccessoryWorker.Session) {
        self.session = session
    }

    func dataReceived(_ data: Data) {
        // Save the mode to your shared app group container using your own storage mechanism.

        Task {
            try await session?.send(data: Data())
        }
    }

    func sessionInvalidated(error: (any Error)?) {
        session = nil
    }
}
```

The companion app reads the saved mode from the shared container the next time the person opens the app.

> 💡 **Tip**: Not every worker task starts with data from the accessory. When the accessory requests information about the weather, for example, your data provider extension can send the current conditions as soon as its session starts, without waiting for the transport extension to send anything.

## See Also

### Background work
- [struct AccessoryWorker](./accessoryworker.md)
  A feature that carries data between your data provider and transport extensions.
- [struct AccessoryGPUWorker](./accessorygpuworker.md)
  A feature for GPU work that carries data between your data provider and transport extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/sending-data-to-an-accessory-in-the-background)*