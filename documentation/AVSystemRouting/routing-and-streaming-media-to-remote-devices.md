# Routing and streaming media to remote devices

**Framework**: AVSystemRouting  
**Role**: Article

Send media from an app to nearby remote playback devices.

## Overview

To stream media on a remote device, you create an extension that connects to a device’s media application. To present options and updates for that stream to a person, you adopt audio-visual interface and session components in your app. The streaming content travels an audio-visual *route* through the app, the system, and the extension.

Discover devices and playback control in the extension, observe routes, start a media session in the app, and take advantage of the shared data channel and real-time streaming capabilities of the extension and the app working together.

Using a dedicated app that you create, your extension discovers nearby devices through the network, Wi-Fi, or Bluetooth, and reports the devices to the system. Don’t add functionality to your app bundling a media extension other than deployment of the extension and instruction for someone using it. After a session starts, the app displays a playback control interface and the system creates a data channel between the extension and an application on the streaming device if it exists. Your app integrates with the media device’s app to observe route-activation events, then begins playback on a discovered route. The extension announces devices, the system presents them in the route-picker interface, and a person’s selection drives the connection.

> ❗ **Important**: The AVSystemRouting and MediaDevice frameworks require iOS 27.0 or later. These frameworks are unavailable on Mac Catalyst and visionOS.

### Discover and report nearby devices

Your app extension’s entry point conforms to [`MediaDeviceExtension`](../MediaDevice/mediadeviceextension.md). Identify your extension’s protocol by declaring the `@main` struct and implementing its two properties, then indicate whether the extension can handle more than one active session at a time with [`supportsSimultaneousSessions`](../MediaDevice/mediadeviceextension/supportssimultaneoussessions.md). When a person opens a device picker UI, the system instantiates the extension and calls [`startDeviceDiscovery()`](../MediaDevice/mediadeviceextension/startdevicediscovery%28%29.md).

Inside `startDeviceDiscovery()`, use [`NWBrowser`](../Network/nwbrowser.md), [Core Bluetooth](../CoreBluetooth/CoreBluetooth.md), or [Wi-Fi Aware](../WiFiAware/WiFiAware.md) to scan for nearby devices. As you discover each device, construct a [`MediaOutputDevice`](../MediaDevice/mediaoutputdevice.md) value that describes it. The remote device provides a [`displayName`](../MediaDevice/mediaoutputdevice/displayname.md) to coordinate with other extensions the device might support.

> **Note**: Apps that use Core Bluetooth must include [`NSBluetoothAlwaysUsageDescription`](../BundleResources/information-property-list/nsbluetoothalwaysusagedescription.md) in the Info pane in Xcode, and an explanation to the person deciding about why the app needs Bluetooth access. Apps that use NWBrowser for local network discovery must also declare [`NSLocalNetworkUsageDescription`](../BundleResources/information-property-list/nslocalnetworkusagedescription.md) with an explanation of why the app needs local network access, and the appropriate [`NSBonjourServices`](../BundleResources/information-property-list/nsbonjourservices.md) entries, in the Info pane in Xcode.

Obtain a [`MediaDeviceRoutingManager`](../MediaDevice/mediadeviceroutingmanager.md) by calling [`routingManager(for:)`](../MediaDevice/mediadeviceroutingmanager/routingmanager%28for%29.md) inside your extension, not from a shared singleton. Then call [`foundDevice(_:)`](../MediaDevice/mediadeviceroutingmanager/founddevice%28_%29.md) to report each discovered device to the system:

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

As your discovery scan runs, call [`lostDevice(_:)`](../MediaDevice/mediadeviceroutingmanager/lostdevice%28_%29.md) when a previously reported device disappears, and [`updateDevices(_:)`](../MediaDevice/mediadeviceroutingmanager/updatedevices%28_%29.md) to refresh the full list at once. If discovery fails entirely, call [`discoveryFailed(_:)`](../MediaDevice/mediadeviceroutingmanager/discoveryfailed%28_%29.md) with a descriptive error. In [`stopDeviceDiscovery()`](../MediaDevice/mediadeviceextension/stopdevicediscovery%28%29.md), tear down your scan resources and stop advertising to conserve power.

### Activate and authenticate devices

When someone selects a device from the route-picker interface, the system calls [`activateDevice(_:session:for:)`](../MediaDevice/mediadeviceextension/activatedevice%28_,session,for%29.md) on your extension. If the device requires no authentication, establish a connection to the remote device. Call [`activatedDevice(_:session:)`](../MediaDevice/mediadeviceroutingmanager/activateddevice%28_,session%29.md) after a successful connection to the remote device and any necessary pairing completes. If the connection to the device fails, call [`failedToActivateDevice(_:session:error:)`](../MediaDevice/mediadeviceroutingmanager/failedtoactivatedevice%28_,session,error%29.md) with a corresponding error code to inform the system of the failure.

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

Call [`requestPairingCode(for:session:reason:authorizationMethod:)`](../MediaDevice/mediadeviceroutingmanager/requestpairingcode%28for,session,reason,authorizationmethod%29.md) to present the pairing interface. Pass the appropriate [`MediaOutputDevice.AuthorizationMethod`](../MediaDevice/mediaoutputdevice/authorizationmethod.md), [`numericCode(length:)`](../MediaDevice/mediaoutputdevice/authorizationmethod/numericcode%28length%29.md) for PIN-based devices, or [`password`](../MediaDevice/mediaoutputdevice/authorizationmethod/password.md) for free-form passwords: When a description is found, check whether the device requires authentication:

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

After the person enters a pairing code, the system calls [`connectUsingPairingCode(_:to:session:)`](../MediaDevice/mediadeviceextension/connectusingpairingcode%28_,to,session%29.md). Validate the code and call either `activatedDevice(_:session:)` on success or `failedToActivateDevice(_:session:error:)` on failure:

```swift
if pairingCode == validPasscode {
    routingManager.activatedDevice(device, session: session)
} else {
    routingManager.failedToActivateDevice(
        device, session: session,
        error: MediaDeviceError(.authorizationFailed))
}
```

When the person deactivates a device or the system tears down the route, the system calls [`deactivateDevice(_:session:)`](../MediaDevice/mediadeviceextension/deactivatedevice%28_,session%29.md). Release any resources you allocated for that device and session.

### Start and control a session

When an app on the device starts a session to a route your extension manages, the system calls [`startSession(_:identifier:url:)`](../MediaDevice/mediadeviceextension/startsession%28_,identifier,url%29.md). At this point, create a `PlaybackControl` object that conforms to [`AVInterfaceControllable`](../AVKit/avinterfacecontrollable.md) and assign it locally:

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

`AVInterfaceControllable` is a composite protocol that combines playback state, time, volume, media selection, and metadata interfaces. Implement the subprotocols in your `PlaybackControl` class. The system reads and writes properties such as [`playing`](../AVKit/avinterfaceplaybackcontrollable/playing.md) and [`currentPlaybackPosition`](../AVKit/avinterfacetimecontrollable/currentplaybackposition.md) to command the remote device. When the property setter activates, translate the new value into a command you send to the remote device over your transport layer:

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

Implement the remaining [`AVInterfaceControllable`](../AVKit/avinterfacecontrollable.md) properties as stored properties that reflect the remote device’s current state. Update them whenever you receive status updates from the device. To ensure smooth UI updates across the system and media-playing apps, provide updates on a regular cadence and for changes in playback state.

When the session ends, the system calls [`stopSession(_:)`](../MediaDevice/mediadeviceextension/stopsession%28_%29.md). Stop remote playback, release resources associated with generating streaming data, and set your stored `PlaybackControl` reference to `nil`.

### Respond to volume changes

Declare volume support in [`MediaOutputDevice`](../MediaDevice/mediaoutputdevice.md) with [`volumeControl`](../MediaDevice/mediaoutputdevice/volumecontrol-swift.property.md). Set [`canMute`](../MediaDevice/mediaoutputdevice/canmute.md) to `true` when the device supports muting.

The system calls [`setVolume(_:for:)`](../MediaDevice/mediadeviceextension/setvolume%28_,for%29.md), [`changeVolume(by:for:)`](../MediaDevice/mediadeviceextension/changevolume%28by,for%29.md), and [`muteDevice(_:)`](../MediaDevice/mediadeviceextension/mutedevice%28_%29.md) on your extension when the person adjusts volume through system interface. Forward each call to the remote device over your transport layer. If the remote device initiates its own volume change, for example, through physical buttons, read the new level with [`volume(for:)`](../MediaDevice/mediadeviceextension/volume%28for%29.md) or check mute state with [`isDeviceMuted(_:)`](../MediaDevice/mediadeviceextension/isdevicemuted%28_%29.md), then call [`volumeChanged(for:)`](../MediaDevice/mediadeviceroutingmanager/volumechanged%28for%29.md) to notify the system so it can update its own interface.

### Stream real-time audio and video

When your extension needs to receive raw media samples rather than a URL for the device to fetch independently, extend your conformance to include [`RealtimeSampleHandling`](../MediaDevice/realtimesamplehandling.md). This protocol extends [`MediaDeviceExtension`](../MediaDevice/mediadeviceextension.md), so your base conformance must already be in place. Declare support by including [`realtimeAudioStreaming`](../MediaDevice/mediaoutputdevice/capabilities-swift.struct/realtimeaudiostreaming.md) and [`realtimeVideoStreaming`](../MediaDevice/mediaoutputdevice/capabilities-swift.struct/realtimevideostreaming.md) in the [`MediaOutputDevice.Capabilities`](../MediaDevice/mediaoutputdevice/capabilities-swift.struct.md) of your [`MediaOutputDevice`](../MediaDevice/mediaoutputdevice.md).

The system calls [`startRealtimeSampleDelivery(session:)`](../MediaDevice/realtimesamplehandling/startrealtimesampledelivery%28session%29.md) when sample delivery begins. Use [ScreenCaptureKit](../ScreenCaptureKit/ScreenCaptureKit.md) to capture video frames, then encode them with [Video Toolbox](../VideoToolbox/VideoToolbox.md) and transmit them to the remote device. Set up [Audio Toolbox](../AudioToolbox/AudioToolbox.md) encoders for audio samples in the same step.

> **Note**: Include `NSScreenCaptureUsageDescription` in your app’s Info pane in Xcode with a description of why screen recording access is needed. Your extension must request a person’s permission before starting capture and capture only the content necessary for streaming.

When the system calls [`stopRealtimeSampleDelivery(session:)`](../MediaDevice/realtimesamplehandling/stoprealtimesampledelivery%28session%29.md), stop all capture and encoding, release the encoder resources, and halt transmission.

### Route media from your app

To receive route events, add [`MDESupportedProtocols`](../BundleResources/information-property-list/mdesupportedprotocols.md) to your app’s Info pane in Xcode with the [`UTType`](../UniformTypeIdentifiers/uttype-swift.struct.md) string your extension declares in [`protocolType`](../MediaDevice/mediadeviceextension/protocoltype.md). Then register an observer with [`shared`](./avsystemroutecontroller-18ns8/shared.md):

```swift
let added = AVSystemRouteController.shared.addObserver(routeObserver)
```

`addObserver` returns `false` if the observer has already registered it. For example, if the same observer is already registered or if the route controller is unavailable. Check the return value and handle the failure before proceeding.

Implement [`AVSystemRouteControllerObserver`](./avsystemroutecontrollerobserver-5syvg.md) to handle route events. Prefer the `async` variant of [`systemRouteController(_:handle:)`](./avsystemroutecontrollerobserver-5syvg/systemroutecontroller%28_,handle%29.md) over the callback form. The [`reason`](./avsystemrouteevent-1r0st/reason.md) property tells you whether the event is an `.activate` or `.deactivate`:

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

On [`AVSystemRouteEvent.Reason.activate`](./avsystemrouteevent-2elr5/reason-swift.enum/activate.md), store [`route`](./avsystemrouteevent-2elr5/route.md) as your [`AVSystemRoute`](./avsystemroute-5s2um.md) reference. The route’s `protocolType` identifies which device extension protocol is in use. Use [`routeDisplayName`](./avsystemroute-5s2um/routedisplayname.md) and [`routeSymbolName`](./avsystemroute-5s2um/routesymbolname.md) to reflect the destination in your app’s interface.

### Start a media session

With an active [`AVSystemRoute`](./avsystemroute-5s2um.md), create an [`AVSystemRouteSession`](./avsystemroutesession-gp78.md) using the content URL and a launch mode. Choose [`AVSystemRoute.LaunchMode.application`](./avsystemroute-5s2um/launchmode/application.md) when you want your app’s counterpart process on the device to handle playback and when you need a data channel between the extension and an application on the streaming device. Choose [`AVSystemRoute.LaunchMode.player`](./avsystemroute-5s2um/launchmode/player.md) when you want the device’s default media player to handle playback.

Before starting, call [`addSession(_:)`](./avsystemroute-5s2um/addsession%28_%29.md) and check its return value. A `false` result means the route can’t accept the session, so return early rather than proceeding:

```swift
let session = AVSystemRouteSession(url: contentURL, mode: .application)
guard activeRoute.addSession(session) else { return }
```

Then start the session and await the [`AVSystemRouteMediaSession`](./avsystemroutemediasession-98ioq.md):

```swift
do {
    let mediaSession = try await session.start()
    // Use `mediaSession.playbackControl` to send commands to the remote device.
    // Use `mediaSession.dataChannel` for app-to-extension messaging.
} catch {
    activeRoute.removeSession(session)
}
```

[`playbackControl`](./avsystemroutemediasession-98ioq/playbackcontrol.md) provides an object conforming to [`AVInterfaceControllable`](../AVKit/avinterfacecontrollable.md), the same interface the extension implemented. Use it to read playback state and issue commands. When someone stops playback, call [`stop()`](./avsystemroutesession-gp78/stop%28%29.md) and then [`removeSession(_:)`](./avsystemroute-5s2um/removesession%28_%29.md) to clean up.

### Communicate between app and extension

[`AVSystemRoute`](./avsystemroute-5s2um.md) exposes a route-level data channel through [`routeDataChannel`](./avsystemroute-5s2um/routedatachannel.md). This channel is available as soon as the route is active, independent of any session. Set its [`dataDelegate`](./avsystemroute-5s2um/datachannel/datadelegate.md) to an object conforming to [`AVSystemRouteDataDelegate`](./avsystemroutedatadelegate-7vt4b.md) to receive incoming messages, then call [`send(_:)`](./avsystemroute-5s2um/datachannel/send%28_%29.md) to transmit data:

```swift
let routeChannel = activeRoute.routeDataChannel
routeChannel.dataDelegate = myDelegate
try await routeChannel.send(data)
```

In [`AVSystemRoute.LaunchMode.application`](./avsystemroute-5s2um/launchmode/application.md) and [`AVSystemRoute.LaunchMode.player`](./avsystemroute-5s2um/launchmode/player.md) modes, [`AVSystemRouteMediaSession`](./avsystemroutemediasession-98ioq.md) exposes a session-scoped [`dataChannel`](./avsystemroutemediasession-98ioq/datachannel.md). This channel is `nil` in `.player` mode, so check for `nil` before using it. On the extension side, call [`sendData(_:toApplication:session:)`](../MediaDevice/mediadeviceextension/senddata%28_,toapplication,session%29.md) to send data toward the app, and implement [`receiveData(_:fromApplication:session:)`](../MediaDevice/mediadeviceroutingmanager/receivedata%28_,fromapplication,session%29.md) to handle messages arriving from the app. The routing manager delivers those messages through [`receiveData(_:fromApplication:session:)`](../MediaDevice/mediadeviceroutingmanager/receivedata%28_,fromapplication,session%29.md).

### Stream real-time audio

The current route may support real-time audio if both the extension and media device support it. In this scenario, your app can also play audio through [AVFoundation](../AVFoundation/AVFoundation.md). The system hands the audio directly to the extension, which delivers it to the device for playback.

## See Also

### Essentials
- [Routing media to third-party devices](./routing-media-to-third-party-devices.md)
  Respond to routing events and control playback on a TV, speaker, or other media device.
- [class AVSystemRouteController](./avsystemroutecontroller-18ns8.md)
  An object that manages interaction with system routes.
- [protocol AVSystemRouteControllerObserver](./avsystemroutecontrollerobserver-5syvg.md)
  A protocol for observers of a system routing controller.
- [AVSystemRouteController](./avsystemroutecontroller-4teia.md)
  An object that manages interaction with system routes.
- [AVSystemRouteControllerObserver](./avsystemroutecontrollerobserver-7p7a5.md)
  A protocol for observers of a system routing controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/routing-and-streaming-media-to-remote-devices)*