# AccessoryTransportAppExtension

**Framework**: Accessory Transport Extension  
**Kind**: protocol  
**Role**: Protocol

A protocol for an extension that transmits data to an accessory you develop.

**Availability**:
- iOS 26.2+

## Declaration

```swift
protocol AccessoryTransportAppExtension : AppExtension
```

## Mentions

- [Receiving iOS notifications on an accessory](./receiving-ios-notifications-on-an-accessory.md)
- [Forwarding notifications to your accessory using the internet transport type](./forwarding-notifications-to-your-accessory-using-the-internet-transport-type.md)

## Overview

Implement this protocol in an extension with an `EXExtensionPointIdentifier` value of `com.apple.accessory-transport-extension` to relay data to your accessory. The extension supports sharing Wi-Fi networks and forwarding iOS system notifications.

> ❗ **Important**: The system requires your app extension to have the [`com.apple.developer.accessory-transport-extension`](../BundleResources/entitlements/com.apple.developer.accessory-transport-extension.md) entitlement to use this protocol.

## Wi-Fi network sharing

Use this extension with [Wi-Fi Infrastructure](../WiFiInfrastructure/WiFiInfrastructure.md) to share a Wi-Fi network with your accessory. The system calls your extension’s [`accept(sessionRequest:)`](./accessorytransportappextension/accept%28sessionrequest%29.md) method when it needs to establish a transport session for Wi-Fi sharing.

In your extension’s target properties, specify the extension point identifier:

```xml
<plist>
    <dict>
        <key>EXAppExtensionAttributes</key>
        <dict>
            <key>EXExtensionPointIdentifier</key>
            <string>com.apple.accessory-transport-extension</string>
        </dict>
    </dict>
</plist>
```

In your extension’s Swift code, implement the protocol and provide an event handler:

```swift
@main
struct TransportExtension: AccessoryTransportAppExtension {
    func accept(sessionRequest: AccessoryTransportSession.Request) -> AccessoryTransportSession.Request.Decision {
        return sessionRequest.accept {
            MyTransportEventHandler(session: sessionRequest.session)
        }
    }
}

class MyTransportEventHandler: AccessoryTransportSession.EventHandler {
    func invalidationHandler(error: AccessoryTransportSession.Error?) {
        // Clean up when the session ends.
    }
}
```

After accepting a session, your extension connects directly to the accessory using [`ASAccessorySession`](../AccessorySetupKit/asaccessorysession.md) and delivers Wi-Fi network data using [`WINetworkSharingProvider`](../WiFiInfrastructure/winetworksharingprovider.md).

## Notification forwarding

For notification forwarding, set up your extension the same way as for Wi-Fi network sharing. The system invokes your extension to relay encrypted notification data from your app’s [`AccessoryDataProvider`](./accessorydataprovider.md) extension to your accessory.

Implement [`dataEventHandler(event:)`](./accessorytransportsession/eventhandler/dataeventhandler%28event%29.md) in your event handler to receive and transmit data:

```swift
class MyTransportEventHandler: AccessoryTransportSession.EventHandler {
    func dataEventHandler(event: AccessoryTransportSession.DataEvent) {
        switch event {
        case .ciphertext(let data, let featureID):
            // Transmit encrypted notification data to accessory over Bluetooth.
            sendToAccessory(data)
        case .plaintext(let data, let featureID):
            // Transmit plaintext data to accessory.
            sendToAccessory(data)
        }
    }
    
    func invalidationHandler(error: AccessoryTransportSession.Error?) {
        // Clean up when the session ends.
    }
}
```

The system encrypts data using keys through your app’s [`AccessoryTransportSecurity`](./accessorytransportsecurity.md) (ATS) extension and then delivers the encrypted data as `ciphertext` to your handler. Your extension transmits the encrypted data to the accessory, which decrypts the data using shared encryption keys.

> **Note**:  Call [`cancel(error:)`](./accessorytransportsession/cancel%28error%29.md) on the session if your extension encounters an error that requires terminating the session.

## Support Bluetooth in the background

The system suspends your transport extension when it’s idle, and relaunches or resumes the extension when your accessory sends an update for a characteristic to which your extension subscribes (for more information on characteristics, see [Transferring Data Between Bluetooth Low Energy Devices](../CoreBluetooth/transferring-data-between-bluetooth-low-energy-devices.md)). If the system calls your central manager delegate’s [`centralManager(_:willRestoreState:)`](../CoreBluetooth/cbcentralmanagerdelegate/centralmanager%28_,willrestorestate%29.md) method so your extension can reconstitute its prior session state, the system initiates a *cold relaunch*. If your extension’s objects remain in memory and the system doesn’t call the method, the restart of the accessory is a *warm resume*, because your existing state persists unchanged. In either case, to restore a prior Bluetooth session, configure your extension’s target properties and use the [Core Bluetooth](../CoreBluetooth/CoreBluetooth.md) framework’s [`CBCentralManager`](../CoreBluetooth/cbcentralmanager.md), as shown below.

In your extension’s target properties in Xcode, include the [AccessorySetupKit](../AccessorySetupKit/AccessorySetupKit.md) entries your companion app declares for accessory permissions, so the extension has access to the same approved accessories. Add the `bluetooth-central` background mode to your extension’s target properties:

```xml
<key>UIBackgroundModes</key>
<array>
    <string>bluetooth-central</string>
</array>
```

When your extension instantiates [`CBCentralManager`](../CoreBluetooth/cbcentralmanager.md), use the [`transportStateRestoreIdentifier`](./accessorytransportsession/transportstaterestoreidentifier.md), which is unique to your transport extension instance. The system allocates background operation time and state restoration to one `CBCentralManager` per restoration identifier, and the system doesn’t grant background operation time or state restoration to additional instances.

> **Note**: Only the transport app extension needs this background mode; neither [`AccessoryDataProvider`](./accessorydataprovider.md) nor [`AccessoryTransportSecurity`](./accessorytransportsecurity.md) requires it.

## Topics

### Accepting session requests
- [func accept(sessionRequest: AccessoryTransportSession.Request) -> AccessoryTransportSession.Request.Decision](./accessorytransportappextension/accept%28sessionrequest%29.md)
  Handles a new session request for the accessory.
- [AccessoryTransportSession.Request.Decision](./accessorytransportsession/request/decision.md)
  An opaque type returned from the incoming session handler of an event listener.
### Handling session events
- [AccessoryTransportSession.EventHandler](./accessorytransportsession/eventhandler.md)
  A protocol that defines methods for handling transport session events.
- [AccessoryTransportSession.DataEvent](./accessorytransportsession/dataevent.md)
  An enumeration of data events that the transport extension receives.
### Managing sessions
- [class AccessoryTransportSession](./accessorytransportsession.md)
  A class that manages a transport session between the extension and the system.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/appextension.md)

## See Also

### Wi-Fi network sharing
- [protocol AccessoryTransportExtensionConfiguration](./accessorytransportextensionconfiguration.md)
  An interface that enables you to configure and manage communication between your extension and the system.
- [class AccessoryTransportSession](./accessorytransportsession.md)
  A class that manages a transport session between the extension and the system.
- [Wi-Fi Infrastructure](../WiFiInfrastructure/WiFiInfrastructure.md)
  Share Wi-Fi network credentials securely between devices and connected accessories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportappextension)*