# Creating a media device extension

**Framework**: Media Device

Provide a way for people to find, connect to, and control your media device by adding a device extension in your iOS app.

#### Overview

A media device extension brings TVs, speakers, and streaming devices into systems’s media device picker, the picker that opens when someone taps an [`AVRoutePickerView`](https://developer.apple.com/documentation/AVKit/AVRoutePickerView) in an app. Your extension implements a media sharing protocol that handles discovery, connection, and playback for these devices.

When a person opens the media device picker, the system launches your extension and asks it discover available devices. Your extension scans for nearby devices and reports each one to the system, so they appear in the picker.

When the person selects a device, the system calls [`activateDevice(_:session:for:)`](mediadeviceextension/activatedevice(_:session:for:).md). Your extension connects to the device and reports the result through [`routingManager(for:)`](mediadeviceroutingmanager/routingmanager(for:).md): call [`activatedDevice(_:session:)`](mediadeviceroutingmanager/activateddevice(_:session:).md) on success, or [`failedToActivateDevice(_:session:error:)`](mediadeviceroutingmanager/failedtoactivatedevice(_:session:error:).md) on failure.

> ❗ **Important**: Only maintain connections to devices the system has activated. Don’t make persistent connections that extend beyond the purpose of discovery before the system notifies you that the person has made a selection and activated a device.

When the device is active, your extension is ready to receive media. Media apps that support your protocol use [`AVSystemRoute`](https://developer.apple.com/documentation/AVSystemRouting/AVSystemRoute-5s2um) to start playback on the device. If your extension conforms to [`RealtimeSampleHandling`](realtimesamplehandling.md), the system also routes real-time audio or video samples to it.

Your extension works with [`AVSystemRouting`](https://developer.apple.com/documentation/AVSystemRouting), the framework media apps use to observe routes and control playback. Apps observe route changes through [`AVSystemRouteController`](https://developer.apple.com/documentation/AVSystemRouting/AVSystemRouteController-18ns8) and control playback through [`AVSystemRoute`](https://developer.apple.com/documentation/AVSystemRouting/AVSystemRoute-5s2um). Your extension handles the protocol-specific communication with the hardware.

#### Create and Configure the Extension Target

In Xcode, choose File > New > Target, select Generic Extension. Xcode adds the new extension to your project.

Both the extension and its container app require the [`com.apple.developer.media-device-extension`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.media-device-extension) entitlement set to Media Sharing Protocol ID that uniquely names your protocol:

```xml
<key>com.apple.developer.media-device-extension</key>
<string>com.example.sharingprotocol</string>
```

In the extension’s Info pane in Xcode, set `EXExtensionPointIdentifier` to `com.apple.media-device-extension` inside the `EXAppExtensionAttributes` dictionary.

#### Declare Your Protocol Type

Your Media Sharing Protocol ID identifies your protocol throughout the system, and you set it in three places that must all use the same value:

1. The string value of the `com.apple.developer.media-device-extension` entitlement (set above).
2. The `UTTypeIdentifier` of a `UTExportedTypeDeclarations` entry in the extension’s Info pane in Xcode.
3. The identifier your extension’s [`protocolType`](mediadeviceextension/protocoltype.md) property returns.

Declare a custom Uniform Type Identifier in the extension’s Info pane in Xcode using the same identifier. The type must conform to `public.media-sharing-protocol`:

```xml
<key>UTExportedTypeDeclarations</key>
<array>
    <dict>
        <key>UTTypeIdentifier</key>
        <string>com.example.sharingprotocol</string>
        <key>UTTypeDescription</key>
        <string>My Sharing Protocol</string>
        <key>UTTypeConformsTo</key>
        <array>
            <string>public.media-sharing-protocol</string>
        </array>
    </dict>
</array>
```

The system uses the `UTTypeDescription` value as your protocol’s display name. It appears in the media device picker, in the Settings interface that lets people choose a preferred protocol, and in system-surfaced error screens. Choose a name that is short, recognizable, and appropriate for people to easily identify your device.

#### Implement the Media Device Extension

In the new target, create a class that conforms to [`MediaDeviceExtension`](mediadeviceextension.md) and mark it with `@main`:

```swift
import MediaDevice
import UniformTypeIdentifiers

@main
@available(iOS 27.0, *)
class MyDeviceExtension: MediaDeviceExtension {

    var protocolType: UTType {
        UTType(exportedAs: "com.example.sharingprotocol")
    }

    var supportsSimultaneousSessions: Bool { false }

    lazy var routingManager: MediaDeviceRoutingManager = .routingManager(for: self)

    required init() {}

    func startDeviceDiscovery() {
        // Start protocol-specific network discovery here.
    }

    func stopDeviceDiscovery() {
        // Stop protocol-specific network discovery here.
    }

    func activateDevice(
        _ device: MediaOutputDevice,
        session: MediaOutputSession,
        for deviceFeatures: MediaOutputDevice.Capabilities
    ) {
        // Connect to the device and report the result through the routing manager.
    }

    func connectUsingPairingCode(
        _ pairingCode: String?,
        to device: MediaOutputDevice,
        session: MediaOutputSession
    ) {
        // Authenticate the device with the person's pairing input.
    }

    func deactivateDevice(
        _ device: MediaOutputDevice,
        session: MediaOutputSession
    ) {
        // Disconnect the device and release any session-scoped resources.
    }

    func setVolume(_ volume: Float, for device: MediaOutputDevice) {
        // Set the device's volume to the requested level in the range 0.0 - 1.0.
    }

    func volume(for device: MediaOutputDevice) -> Float {
        // Return the device's current volume level in the range 0.0 - 1.0.
        0
    }

    func changeVolume(by increments: Int, for device: MediaOutputDevice) {
        // Apply a relative volume change to the device.
    }

    func muteDevice(_ device: MediaOutputDevice) {
        // Mute the device.
    }

    func isDeviceMuted(_ device: MediaOutputDevice) -> Bool {
        // Return the device's current mute state.
        false
    }

    func startSession(
        _ session: MediaOutputSession,
        identifier: String?,
        url: URL
    ) {
        // Begin playback of the URL on the remote device.
    }

    func stopSession(_ session: MediaOutputSession) {
        // Stop playback for this session.
    }

    func sendData(
        _ data: Data,
        toApplication applicationIdentifier: String,
        session: MediaOutputSession
    ) {
        // Forward the data payload to the target app on the remote device.
    }
}
```

The `routingManager` property is how your extension communicates with the system. Obtain an instance by calling [`routingManager(for:)`](mediadeviceroutingmanager/routingmanager(for:).md), then use it throughout your extension to report discovered devices, activation results, sessions, and pairing requests.

The `supportsSimultaneousSessions` property tells the system whether your extension can handle multiple [`MediaOutputSession`](mediaoutputsession.md) instances at the same time.

#### Discover Devices on the Network

When a person opens the media device picker, the system calls [`startDeviceDiscovery()`](mediadeviceextension/startdevicediscovery().md). Use your protocol’s discovery mechanism to find devices, then report them to the system through [`routingManager(for:)`](mediadeviceroutingmanager/routingmanager(for:).md).

```swift
func startDeviceDiscovery() {
    // Start protocol-specific network discovery here.
    // As you find devices, create a `MediaOutputDevice` and report it
    // to make the device available to the system.
    // Use a stable identifier (for example, derived from your protocol's
    // device ID) so the same physical device produces the same ID
    // across discoveries.

    guard let device = MediaOutputDevice(
        id: deviceID,
        displayName: "Living Room TV",
        capabilities: [.urlPlayback],
        requiredNetworkEndpoints: endpoints
    ) else { return }

    routingManager.foundDevice(device)
}

func stopDeviceDiscovery() {
    // Stop protocol-specific network discovery here.
}
```

Report discovery events through [`routingManager(for:)`](mediadeviceroutingmanager/routingmanager(for:).md) as devices appear and disappear on the network:

- [`foundDevice(_:)`](mediadeviceroutingmanager/founddevice(_:).md) — Reports a newly discovered device so the system can include it in the device list.
- [`lostDevice(_:)`](mediadeviceroutingmanager/lostdevice(_:).md) — Removes a previously discovered device from the device list.
- [`updateDevices(_:)`](mediadeviceroutingmanager/updatedevices(_:).md) — Refreshes the state of one or more devices after their properties change.
- [`discoveryFailed(_:)`](mediadeviceroutingmanager/discoveryfailed(_:).md) — Reports an unexpected discovery failure. Don’t call this when no devices are found.

#### Activate a Device

When a person selects a device, the system calls [`activateDevice(_:session:for:)`](mediadeviceextension/activatedevice(_:session:for:).md). Connect to the device and report the result through [`routingManager(for:)`](mediadeviceroutingmanager/routingmanager(for:).md).

```swift
func activateDevice(
    _ device: MediaOutputDevice,
    session: MediaOutputSession,
    for deviceFeatures: MediaOutputDevice.Capabilities
) {
    // Handle possible device authorization here.

    do {
        try myProtocolClient.connect(to: device)
        routingManager.activatedDevice(device, session: session)
    } catch {
        routingManager.failedToActivateDevice(
            device,
            session: session,
            error: MediaDeviceError(.connectionFailed)
        )
    }
}
```

When the person disconnects from the device, the system calls [`deactivateDevice(_:session:)`](mediadeviceextension/deactivatedevice(_:session:).md). Disconnect and release any resources associated with the session.

#### Handle Device Authorization

Some devices require pairing before activation. When a device needs authorization, call [`requestPairingCode(for:session:reason:authorizationMethod:)`](mediadeviceroutingmanager/requestpairingcode(for:session:reason:authorizationmethod:).md) to present a pairing interface. The [`MediaOutputDevice.AuthorizationMethod`](mediaoutputdevice/authorizationmethod.md) type defines the available pairing interfaces:

- [`numericCode(length:)`](mediaoutputdevice/authorizationmethod/numericcode(length:).md) — A numeric PIN code with a fixed digit count. Pass [`fourCharacter`](mediaoutputdevice/authorizationmethod/codelength/fourcharacter.md) or [`sixCharacter`](mediaoutputdevice/authorizationmethod/codelength/sixcharacter.md).
- [`password`](mediaoutputdevice/authorizationmethod/password.md) — A text password.
- [`none`](mediaoutputdevice/authorizationmethod/none.md) — No authorization required.

The system collects the person’s input and delivers it to [`connectUsingPairingCode(_:to:session:)`](mediadeviceextension/connectusingpairingcode(_:to:session:).md):

```swift
func activateDevice(
    _ device: MediaOutputDevice,
    session: MediaOutputSession,
    for deviceFeatures: MediaOutputDevice.Capabilities
) {
    if myProtocolClient.requiresPairing(device) {
        routingManager.requestPairingCode(
            for: device,
            session: session,
            reason: "Enter the code shown on your TV.",
            authorizationMethod: .numericCode(length: .fourCharacter)
        )
    } else {
        // Handle regular device activation here.
        do {
            try myProtocolClient.connect(to: device)
            routingManager.activatedDevice(device, session: session)
        } catch {
            routingManager.failedToActivateDevice(
                device,
                session: session,
                error: MediaDeviceError(.connectionFailed)
            )
        }
    }
}

func connectUsingPairingCode(
    _ pairingCode: String?,
    to device: MediaOutputDevice,
    session: MediaOutputSession
) {
    guard let code = pairingCode else {
        // The person canceled pairing with their iPhone.
        routingManager.failedToActivateDevice(
            device,
            session: session,
            error: MediaDeviceError(.authorizationFailed)
        )
        return
    }

    do {
        try myProtocolClient.authenticate(with: code, device: device)
        routingManager.activatedDevice(device, session: session)
    } catch {
        routingManager.failedToActivateDevice(
            device,
            session: session,
            error: MediaDeviceError(.authorizationFailed)
        )
    }
}
```

#### Start Media Playback

After activation, the system calls [`startSession(_:identifier:url:)`](mediadeviceextension/startsession(_:identifier:url:).md) to begin playback. Send the URL to the device and report success through [`routingManager(for:)`](mediadeviceroutingmanager/routingmanager(for:).md):

```swift
func startSession(
    _ session: MediaOutputSession,
    identifier: String?,
    url: URL
) {
    do {
        let playbackControl = try myProtocolClient.startPlayback(
            url: url,
            applicationIdentifier: identifier
        )
        routingManager.started(
            application: identifier,
            playbackControl: playbackControl,
            session: session
        )
    } catch {
        routingManager.sessionFailed(
            session,
            error: MediaDeviceError(.sessionFailed)
        )
    }
}

func stopSession(_ session: MediaOutputSession) {
    myProtocolClient.stopPlayback()
}
```

The `playbackControl` parameter conforms to doc://com.apple.documentation/documentation/avkit/avinterfacecontrollable-1wpdy, which models the full playback state of the remote session. Update its properties to keep the system in sync as playback progresses: for example, `isPlaying`, `state`, `currentPlaybackPosition`, `playbackSpeed`, `timeRange`, and `metadata`.

The system observes these properties and drives the shared playback UI from them, including Now Playing, the media device picker, and any controls surfaced by media apps. The system also uses the object’s conformance to `AVInterfacePlaybackControllable` to deliver play, pause, and seek commands back to your extension.

##### Stream Real Time Samples

Some devices receive audio or video samples directly instead of fetching a URL. Real-time sample delivery is orthogonal to URL playback, and a device can support any combination of the two:

- For devices that receive audio samples directly, set the device’s capabilities to include [`realtimeAudioStreaming`](mediaoutputdevice/capabilities-swift.struct/realtimeaudiostreaming.md). The system routes audio destined for that device through your extension.
- For devices that receive video frames directly to support screen-mirroring, set the device’s capabilities to include [`realtimeVideoStreaming`](mediaoutputdevice/capabilities-swift.struct/realtimevideostreaming.md). The system routes screen frames to your extension only while screen mirroring is active.

Ensure your extension class conforms to [`RealtimeSampleHandling`](realtimesamplehandling.md). The system calls [`startRealtimeSampleDelivery(session:)`](realtimesamplehandling/startrealtimesampledelivery(session:).md) when samples start flowing, and [`stopRealtimeSampleDelivery(session:)`](realtimesamplehandling/stoprealtimesampledelivery(session:).md) to stop them.

To capture the samples themselves, use the appropriate system framework:

- For audio, use [`AudioDriverKit`](https://developer.apple.com/documentation/AudioDriverKit/AudioDriverKit) to receive system audio, then [`Audio Toolbox`](https://developer.apple.com/documentation/AudioToolbox) to encode it.
- For video, use [`ScreenCaptureKit`](https://developer.apple.com/documentation/ScreenCaptureKit) to receive system video, then [`Video Toolbox`](https://developer.apple.com/documentation/VideoToolbox) to encode it.

```swift
@main
@available(iOS 27.0, *)
class MyDeviceExtension: MediaDeviceExtension, RealtimeSampleHandling {

    // Implement the `MediaDeviceExtension` requirements above.

    func startRealtimeSampleDelivery(session: MediaOutputSession) {
        // Start capturing samples and send them to the remote device.
    }

    func stopRealtimeSampleDelivery(session: MediaOutputSession) {
        // Stop capturing samples and remove any encoders.
    }
}
```

#### Provide Volume Control

Configure volume support when you create a [`MediaOutputDevice`](mediaoutputdevice.md) by setting its [`MediaOutputDevice.VolumeControl`](mediaoutputdevice/volumecontrol-swift.enum.md) mode:

- [`MediaOutputDevice.VolumeControl.absolute`](mediaoutputdevice/volumecontrol-swift.enum/absolute.md) — The device supports direct volume levels. The system calls [`setVolume(_:for:)`](mediadeviceextension/setvolume(_:for:).md) and [`volume(for:)`](mediadeviceextension/volume(for:).md) to set and read the volume.
- [`MediaOutputDevice.VolumeControl.relative`](mediaoutputdevice/volumecontrol-swift.enum/relative.md) — The device supports only incremental adjustments. The system calls [`changeVolume(by:for:)`](mediadeviceextension/changevolume(by:for:).md) to raise or lower the volume.
- [`MediaOutputDevice.VolumeControl.none`](mediaoutputdevice/volumecontrol-swift.enum/none.md) — The device doesn’t support volume control.

Absolute volume levels must be represented in the range of 0.0 - 1.0.

```swift
func setVolume(_ volume: Float, for device: MediaOutputDevice) {
    myProtocolClient.setVolume(volume, on: device)
}

func volume(for device: MediaOutputDevice) -> Float {
    myProtocolClient.currentVolume(for: device)
}

func changeVolume(by increments: Int, for device: MediaOutputDevice) {
    myProtocolClient.adjustVolume(by: increments, on: device)
}

func muteDevice(_ device: MediaOutputDevice) {
    myProtocolClient.mute(device)
}

func isDeviceMuted(_ device: MediaOutputDevice) -> Bool {
    myProtocolClient.isMuted(device)
}
```

> ❗ **Important**: Only call [`volumeChanged(for:)`](mediadeviceroutingmanager/volumechanged(for:).md) when the device’s volume changes externally, such as from a physical button press or another app. Don’t call it in response to system-initiated calls like [`setVolume(_:for:)`](mediadeviceextension/setvolume(_:for:).md) or [`changeVolume(by:for:)`](mediadeviceextension/changevolume(by:for:).md).

## See Also

- [Routing media to third-party devices](../AVSystemRouting/routing-media-to-third-party-devices.md)
  Respond to routing events and control playback on a TV, speaker, or other media device.
- [protocol MediaDeviceExtension](mediadeviceextension.md)
  A protocol that defines the requirements of a media device extension that discovers, activates, and plays media on a remote device.
- [protocol MediaDeviceExtensionConfiguration](mediadeviceextensionconfiguration.md)
  Configuration for the app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/creating-a-media-device-extension)*