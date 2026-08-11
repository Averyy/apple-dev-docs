# Routing and streaming media to remote devices

**Framework**: AVSystemRouting

Send media from an app to nearby remote playback devices.

#### Overview

To stream media on a remote device, you create an extension that connects to a device’s media application. To present options and updates for that stream to a person, you adopt audio-visual interface and session components in your app. The streaming content travels an audio-visual *route* through the app, the system, and the extension.

Discover devices and playback control in the extension, observe routes, start a media session in the app, and take advantage of the shared data channel and real-time streaming capabilities of the extension and the app working together.

Using a dedicated app that you create, your extension discovers nearby devices through the network, Wi-Fi, or Bluetooth, and reports the devices to the system. Don’t add functionality to your app bundling a media extension other than deployment of the extension and instruction for someone using it. After a session starts, the app displays a playback control interface and the system creates a data channel between the extension and an application on the streaming device if it exists. Your app integrates with the media device’s app to observe route-activation events, then begins playback on a discovered route. The extension announces devices, the system presents them in the route-picker interface, and a person’s selection drives the connection.

> ❗ **Important**: The AVSystemRouting and MediaDevice frameworks require iOS 27.0 or later. These frameworks are unavailable on Mac Catalyst and visionOS.

##### Discover and Report Nearby Devices

Your app extension’s entry point conforms to [`MediaDeviceExtension`](https://developer.apple.com/documentation/MediaDevice/MediaDeviceExtension). Identify your extension’s protocol by declaring the `@main` struct and implementing its two properties, then indicate whether the extension can handle more than one active session at a time with [`supportsSimultaneousSessions`](https://developer.apple.com/documentation/MediaDevice/MediaDeviceExtension/supportsSimultaneousSessions). When a person opens a device picker UI, the system instantiates the extension and calls [`startDeviceDiscovery()`](https://developer.apple.com/documentation/MediaDevice/MediaDeviceExtension/startDeviceDiscovery()).

Inside `startDeviceDiscovery()`, use [`NWBrowser`](https://developer.apple.com/documentation/Network/NWBrowser), [`Core Bluetooth`](https://developer.apple.com/documentation/CoreBluetooth), or [`Wi-Fi Aware`](https://developer.apple.com/documentation/WiFiAware) to scan for nearby devices. As you discover each device, construct a [`MediaOutputDevice`](https://developer.apple.com/documentation/MediaDevice/MediaOutputDevice) value that describes it. The remote device provides a [`displayName`](https://developer.apple.com/documentation/MediaDevice/MediaOutputDevice/displayName) to coordinate with other extensions the device might support.

> **Note**: Apps that use Core Bluetooth must include [`NSBluetoothAlwaysUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSBluetoothAlwaysUsageDescription) in the Info pane in Xcode, and an explanation to the person deciding about why the app needs Bluetooth access. Apps that use NWBrowser for local network discovery must also declare [`NSLocalNetworkUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSLocalNetworkUsageDescription) with an explanation of why the app needs local network access, and the appropriate [`NSBonjourServices`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSBonjourServices) entries, in the Info pane in Xcode.

Obtain a [`MediaDeviceRoutingManager`](https://developer.apple.com/documentation/MediaDevice/MediaDeviceRoutingManager) by calling [`routingManager(for:)`](https://developer.apple.com/documentation/MediaDevice/MediaDeviceRoutingManager/routingManager(for:)) inside your extension, not from a shared singleton. Then call [`foundDevice(_:)`](https://developer.apple.com/documentation/MediaDevice/MediaDeviceRoutingManager/foundDevice(_:)) to report each discovered device to the system:

```swift
func startDeviceDiscovery() {
    let device = MediaOutputDevice(
        id: "5B5A455A-5FBA-55A7-9558-5155AB75A5B5",
        displayName: "Living Room TV",
        capabilities: [.realtimeAudioStreaming, .urlPlayback],
        deviceType: .tv
    )
    routingManager.foundDevice(device)
}
```

As your discovery scan runs, call [`lostDevice(_:)`](https://developer.apple.com/documentation/MediaDevice/MediaDeviceRoutingManager/lostDevice(_:)) when a previously reported device disappears, and [`updateDevices(_:)`](https://developer.apple.com/documentation/MediaDevice/MediaDeviceRoutingManager/updateDevices(_:)) to refresh the full list at once. If discovery fails entirely, call [`discoveryFailed(_:)`](https://developer.apple.com/documentation/MediaDevice/MediaDeviceRoutingManager/discoveryFailed(_:)) with a descriptive error. In [`stopDeviceDiscovery()`](https://developer.apple.com/documentation/MediaDevice/MediaDeviceExtension/stopDeviceDiscovery()), tear down your scan resources and stop advertising to conserve power.

##### Activate and Authenticate Devices

When someone selects a device from the route-picker interface, the system calls [`activateDevice(_:session:for:)`](https://developer.apple.com/documentation/MediaDevice/MediaDeviceExtension/activateDevice(_:session:for:)) on your extension. If the device requires no authentication, establish a connection to the remote device. Call [`activatedDevice(_:session:)`](https://developer.apple.com/documentation/MediaDevice/MediaDeviceRoutingManager/activatedDevice(_:session:)) after a successful connection to the remote device and any necessary pairing completes. If the connection to the device fails, call [`failedToActivateDevice(_:session:error:)`](https://developer.apple.com/documentation/MediaDevice/MediaDeviceRoutingManager/failedToActivateDevice(_:session:error:)) with a corresponding error code to inform the system of the failure.

```swift
func activateDevice(
    _ device: MediaOutputDevice,
    session: MediaOutputSession,
    for deviceFeatures: MediaOutputDevice.Capabilities
) {
    // Connect to device.
    
    guard let description = deviceDescriptions[device.id] else {
        routingManager.failedToActivateDevice(
            device, session: session,
            error: MediaDeviceError(.connectionFailed))
        return
    }
```

Call [`requestPairingCode(for:session:reason:authorizationMethod:)`](https://developer.apple.com/documentation/MediaDevice/MediaDeviceRoutingManager/requestPairingCode(for:session:reason:authorizationMethod:)) to present the pairing interface. Pass the appropriate [`MediaOutputDevice.AuthorizationMethod`](https://developer.apple.com/documentation/MediaDevice/MediaOutputDevice/AuthorizationMethod), [`numericCode(length:)`](https://developer.apple.com/documentation/MediaDevice/MediaOutputDevice/AuthorizationMethod/numericCode(length:)) for PIN-based devices, or [`password`](https://developer.apple.com/documentation/MediaDevice/MediaOutputDevice/AuthorizationMethod/password) for free-form passwords: When a description is found, check whether the device requires authentication:

```swift
    if description.authType == .none {
        routingManager.activatedDevice(device, session: session)
    } else {
        routingManager.requestPairingCode(
            for: device, session: session,
            reason: "Passcode Required",
            authorizationMethod: description.authType)
    }
}
```

After the person enters a pairing code, the system calls [`connectUsingPairingCode(_:to:session:)`](https://developer.apple.com/documentation/MediaDevice/MediaDeviceExtension/connectUsingPairingCode(_:to:session:)). Validate the code and call either `activatedDevice(_:session:)` on success or `failedToActivateDevice(_:session:error:)` on failure:

```swift
if pairingCode == validPasscode {
    routingManager.activatedDevice(device, session: session)
} else {
    routingManager.failedToActivateDevice(
        device, session: session,
        error: MediaDeviceError(.authorizationFailed))
}
```

When the person deactivates a device or the system tears down the route, the system calls [`deactivateDevice(_:session:)`](https://developer.apple.com/documentation/MediaDevice/MediaDeviceExtension/deactivateDevice(_:session:)). Release any resources you allocated for that device and session.

##### Start and Control a Session

When an app on the device starts a session to a route your extension manages, the system calls [`startSession(_:identifier:url:)`](https://developer.apple.com/documentation/MediaDevice/MediaDeviceExtension/startSession(_:identifier:url:)). At this point, create a `PlaybackControl` object that conforms to [`AVInterfaceControllable`](https://developer.apple.com/documentation/AVKit/AVInterfaceControllable) and assign it locally:

```swift
func startSession(
    _ session: MediaOutputSession,
    identifier: String?,
    url: URL
) {
    self.playbackControl = PlaybackControl()
```

Pass the control object to the routing manager to hand it to the system:

```swift
    routingManager.started(
        application: identifier,
        playbackControl: self.playbackControl,
        session: session)
}
```

`AVInterfaceControllable` is a composite protocol that combines playback state, time, volume, media selection, and metadata interfaces. Implement the subprotocols in your `PlaybackControl` class. The system reads and writes properties such as [`playing`](https://developer.apple.com/documentation/AVKit/AVInterfacePlaybackControllable/playing) and [`currentPlaybackPosition`](https://developer.apple.com/documentation/AVKit/AVInterfaceTimeControllable/currentPlaybackPosition) to command the remote device. When the property setter activates, translate the new value into a command you send to the remote device over your transport layer:

```swift
var isPlaying: Bool {
    get { _isPlaying }
    set {
        _isPlaying = newValue
        // Send play or pause command to the remote device.
    }
}
```

Apply the same pattern to other settable properties, such as `currentPlaybackPosition`:

```swift
var currentPlaybackPosition: CMTime {
    get { _currentPlaybackPosition }
    set {
        _currentPlaybackPosition = newValue
        // Send seek command to the remote device.
    }
}
```

Implement the remaining [`AVInterfaceControllable`](https://developer.apple.com/documentation/AVKit/AVInterfaceControllable) properties as stored properties that reflect the remote device’s current state. Update them whenever you receive status updates from the device. To ensure smooth UI updates across the system and media-playing apps, provide updates on a regular cadence and for changes in playback state.

When the session ends, the system calls [`stopSession(_:)`](https://developer.apple.com/documentation/MediaDevice/MediaDeviceExtension/stopSession(_:)). Stop remote playback, release resources associated with generating streaming data, and set your stored `PlaybackControl` reference to `nil`.

##### Respond to Volume Changes

Declare volume support in [`MediaOutputDevice`](https://developer.apple.com/documentation/MediaDevice/MediaOutputDevice) with [`volumeControl`](https://developer.apple.com/documentation/MediaDevice/MediaOutputDevice/volumeControl-swift.property). Set [`canMute`](https://developer.apple.com/documentation/MediaDevice/MediaOutputDevice/canMute) to `true` when the device supports muting.

The system calls [`setVolume(_:for:)`](https://developer.apple.com/documentation/MediaDevice/MediaDeviceExtension/setVolume(_:for:)), [`changeVolume(by:for:)`](https://developer.apple.com/documentation/MediaDevice/MediaDeviceExtension/changeVolume(by:for:)), and [`muteDevice(_:)`](https://developer.apple.com/documentation/MediaDevice/MediaDeviceExtension/muteDevice(_:)) on your extension when the person adjusts volume through system interface. Forward each call to the remote device over your transport layer. If the remote device initiates its own volume change, for example, through physical buttons, read the new level with [`volume(for:)`](https://developer.apple.com/documentation/MediaDevice/MediaDeviceExtension/volume(for:)) or check mute state with [`isDeviceMuted(_:)`](https://developer.apple.com/documentation/MediaDevice/MediaDeviceExtension/isDeviceMuted(_:)), then call [`volumeChanged(for:)`](https://developer.apple.com/documentation/MediaDevice/MediaDeviceRoutingManager/volumeChanged(for:)) to notify the system so it can update its own interface.

##### Stream Real Time Audio and Video

When your extension needs to receive raw media samples rather than a URL for the device to fetch independently, extend your conformance to include [`RealtimeSampleHandling`](https://developer.apple.com/documentation/MediaDevice/RealtimeSampleHandling). This protocol extends [`MediaDeviceExtension`](https://developer.apple.com/documentation/MediaDevice/MediaDeviceExtension), so your base conformance must already be in place. Declare support by including [`realtimeAudioStreaming`](https://developer.apple.com/documentation/MediaDevice/MediaOutputDevice/Capabilities-swift.struct/realtimeAudioStreaming) and [`realtimeVideoStreaming`](https://developer.apple.com/documentation/MediaDevice/MediaOutputDevice/Capabilities-swift.struct/realtimeVideoStreaming) in the [`MediaOutputDevice.Capabilities`](https://developer.apple.com/documentation/MediaDevice/MediaOutputDevice/Capabilities-swift.struct) of your [`MediaOutputDevice`](https://developer.apple.com/documentation/MediaDevice/MediaOutputDevice).

The system calls [`startRealtimeSampleDelivery(session:)`](https://developer.apple.com/documentation/MediaDevice/RealtimeSampleHandling/startRealtimeSampleDelivery(session:)) when sample delivery begins. Use [`ScreenCaptureKit`](https://developer.apple.com/documentation/ScreenCaptureKit) to capture video frames, then encode them with [`Video Toolbox`](https://developer.apple.com/documentation/VideoToolbox) and transmit them to the remote device. Set up [`Audio Toolbox`](https://developer.apple.com/documentation/AudioToolbox) encoders for audio samples in the same step.

> **Note**: Include `NSScreenCaptureUsageDescription` in your app’s Info pane in Xcode with a description of why screen recording access is needed. Your extension must request a person’s permission before starting capture and capture only the content necessary for streaming.

When the system calls [`stopRealtimeSampleDelivery(session:)`](https://developer.apple.com/documentation/MediaDevice/RealtimeSampleHandling/stopRealtimeSampleDelivery(session:)), stop all capture and encoding, release the encoder resources, and halt transmission.

##### Route Media From Your App

To receive route events, add [`MDESupportedProtocols`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/MDESupportedProtocols) to your app’s Info pane in Xcode with the [`UTType`](https://developer.apple.com/documentation/UniformTypeIdentifiers/UTType-swift.struct) string your extension declares in [`protocolType`](https://developer.apple.com/documentation/MediaDevice/MediaDeviceExtension/protocolType). Then register an observer with [`shared`](avsystemroutecontroller-18ns8/shared.md):

```swift
let added = AVSystemRouteController.shared.addObserver(routeObserver)
```

`addObserver` returns `false` if the observer has already registered it. For example, if the same observer is already registered or if the route controller is unavailable. Check the return value and handle the failure before proceeding.

Implement [`AVSystemRouteControllerObserver`](avsystemroutecontrollerobserver-5syvg.md) to handle route events. Prefer the `async` variant of [`systemRouteController(_:handle:)`](AVSystemRouteControllerObserver-5syvg/systemRouteController(_:handle:).md) over the callback form. The [`reason`](avsystemrouteevent-1r0st/reason.md) property tells you whether the event is an `.activate` or `.deactivate`:

```swift
switch event.reason {
case .activate:
    activeRoute = event.route
    return true
case .deactivate:
    activeRoute = nil
    return true
@unknown default:
    return false
}
```

On [`AVSystemRouteEvent.Reason.activate`](avsystemrouteevent-2elr5/reason-swift.enum/activate.md), store [`route`](avsystemrouteevent-2elr5/route.md) as your [`AVSystemRoute`](avsystemroute-5s2um.md) reference. The route’s `protocolType` identifies which device extension protocol is in use. Use [`routeDisplayName`](avsystemroute-5s2um/routedisplayname.md) and [`routeSymbolName`](avsystemroute-5s2um/routesymbolname.md) to reflect the destination in your app’s interface.

##### Start a Media Session

With an active [`AVSystemRoute`](avsystemroute-5s2um.md), create an [`AVSystemRouteSession`](avsystemroutesession-gp78.md) using the content URL and a launch mode. Choose [`AVSystemRoute.LaunchMode.application`](avsystemroute-5s2um/launchmode/application.md) when you want your app’s counterpart process on the device to handle playback and when you need a data channel between the extension and an application on the streaming device. Choose [`AVSystemRoute.LaunchMode.player`](avsystemroute-5s2um/launchmode/player.md) when you want the device’s default media player to handle playback.

Before starting, call [`addSession(_:)`](avsystemroute-5s2um/addsession(_:).md) and check its return value. A `false` result means the route can’t accept the session, so return early rather than proceeding:

```swift
let session = AVSystemRouteSession(url: contentURL, mode: .application)
guard activeRoute.addSession(session) else { return }
```

Then start the session and await the [`AVSystemRouteMediaSession`](avsystemroutemediasession-98ioq.md):

```swift
do {
    let mediaSession = try await session.start()
    // Use `mediaSession.playbackControl` to send commands to the remote device.
    // Use `mediaSession.dataChannel` for app-to-extension messaging.
} catch {
    activeRoute.removeSession(session)
}
```

[`playbackControl`](avsystemroutemediasession-98ioq/playbackcontrol.md) provides an object conforming to [`AVInterfaceControllable`](https://developer.apple.com/documentation/AVKit/AVInterfaceControllable), the same interface the extension implemented. Use it to read playback state and issue commands. When someone stops playback, call [`stop()`](avsystemroutesession-gp78/stop().md) and then [`removeSession(_:)`](avsystemroute-5s2um/removesession(_:).md) to clean up.

##### Communicate Between App and Extension

[`AVSystemRoute`](avsystemroute-5s2um.md) exposes a route-level data channel through [`routeDataChannel`](avsystemroute-5s2um/routedatachannel.md). This channel is available as soon as the route is active, independent of any session. Set its [`dataDelegate`](avsystemroute-5s2um/datachannel/datadelegate.md) to an object conforming to [`AVSystemRouteDataDelegate`](avsystemroutedatadelegate-7vt4b.md) to receive incoming messages, then call [`send(_:)`](avsystemroute-5s2um/datachannel/send(_:).md) to transmit data:

```swift
let routeChannel = activeRoute.routeDataChannel
routeChannel.dataDelegate = myDelegate
try await routeChannel.send(data)
```

In [`AVSystemRoute.LaunchMode.application`](avsystemroute-5s2um/launchmode/application.md) and [`AVSystemRoute.LaunchMode.player`](avsystemroute-5s2um/launchmode/player.md) modes, [`AVSystemRouteMediaSession`](avsystemroutemediasession-98ioq.md) exposes a session-scoped [`dataChannel`](avsystemroutemediasession-98ioq/datachannel.md). This channel is `nil` in `.player` mode, so check for `nil` before using it. On the extension side, call [`sendData(_:toApplication:session:)`](https://developer.apple.com/documentation/MediaDevice/MediaDeviceExtension/sendData(_:toApplication:session:)) to send data toward the app, and implement [`receiveData(_:fromApplication:session:)`](https://developer.apple.com/documentation/MediaDevice/MediaDeviceRoutingManager/receiveData(_:fromApplication:session:)) to handle messages arriving from the app. The routing manager delivers those messages through [`receiveData(_:fromApplication:session:)`](https://developer.apple.com/documentation/MediaDevice/MediaDeviceRoutingManager/receiveData(_:fromApplication:session:)).

##### Stream Real Time Audio

The current route may support real-time audio if both the extension and media device support it. In this scenario, your app can also play audio through [`AVFoundation`](https://developer.apple.com/documentation/AVFoundation). The system hands the audio directly to the extension, which delivers it to the device for playback.

## See Also

- [Routing media to third-party devices](routing-media-to-third-party-devices.md)
  Respond to routing events and control playback on a TV, speaker, or other media device.
- [class AVSystemRouteController](avsystemroutecontroller-18ns8.md)
  An object that manages interaction with system routes.
- [protocol AVSystemRouteControllerObserver](avsystemroutecontrollerobserver-5syvg.md)
  A protocol for observers of a system routing controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/routing-and-streaming-media-to-remote-devices)*