# Routing media to third-party devices

**Framework**: AVSystemRouting

Respond to routing events and control playback on a TV, speaker, or other media device.

#### Overview

When people select a media device, your app receives a routing event. You respond by creating a session that delivers media to that device. This article describes the full workflow, from registering an observer to controlling remote playback.

#### Register an Observer

People can switch media routes at any time by selecting a device. To respond, register an observer with the shared [`AVSystemRouteController`](avsystemroutecontroller-18ns8.md).

Your observer conforms to [`AVSystemRouteControllerObserver`](avsystemroutecontrollerobserver-5syvg.md). When the controller activates or deactivates a route, it calls your observer with an event, and your observer returns a Boolean that indicates whether it handled the event:

```swift
class RouteObserver: AVSystemRouteControllerObserver {
    func systemRouteController(
        _ controller: AVSystemRouteController,
        handle event: AVSystemRouteEvent
    ) async -> Bool {
        switch event.reason {
        case .activate:
            return await startPlayback(on: event.route)
        case .deactivate:
            stopPlayback()
            return true
        @unknown default:
            return false
        }
    }
}

let observer = RouteObserver()
_ = AVSystemRouteController.shared.addObserver(observer)
```

#### Start a Url Based Playback Session

When you receive an [`AVSystemRouteEvent`](avsystemrouteevent-2elr5.md) with an [`AVSystemRouteEvent.Reason.activate`](avsystemrouteevent-2elr5/reason-swift.enum/activate.md) reason, create an [`AVSystemRouteSession`](avsystemroutesession-gp78.md) and start it on the route. Use [`AVSystemRoute.LaunchMode.player`](avsystemroute-5s2um/launchmode/player.md) to launch the system media player on the remote device:

```swift
func startPlayback(on route: AVSystemRoute) async -> Bool {
    let url = URL(string: "https://example.com/media.m3u8")!
    let session = AVSystemRouteSession(url: url, mode: .player)

    guard route.addSession(session) else {
        return false
    }

    do {
        let mediaSession = try await session.start()
        // Use `mediaSession.playbackControl` to build a playback UI.
        return true
    } catch {
        route.removeSession(session)
        return false
    }
}
```

The [`start()`](avsystemroutesession-gp78/start().md) method returns an [`AVSystemRouteMediaSession`](avsystemroutemediasession-98ioq.md) that your app uses to control playback and communicate with the remote device.

#### Control and Observe Remote Playback

Use the [`playbackControl`](avsystemroutemediasession-98ioq/playbackcontrol.md) property to drive playback on the remote device and observe its state. The control conforms to `AVInterfaceControllable` and is available for both [`AVSystemRoute.LaunchMode.player`](avsystemroute-5s2um/launchmode/player.md) and [`AVSystemRoute.LaunchMode.application`](avsystemroute-5s2um/launchmode/application.md) sessions.

Read properties to reflect remote playback state in your UI, and assign to mutable properties to send commands to the remote device:

```swift
func configurePlayback(for mediaSession: AVSystemRouteMediaSession) {
    guard let control = mediaSession.playbackControl else { return }

    // Read state to drive your UI.
    let title = control.metadata.title
    let duration = control.timeRange.duration
    let isPlaying = control.isPlaying

    // Send commands to the remote device.
    control.currentPlaybackPosition = CMTime(seconds: 30, preferredTimescale: 600)
    control.playbackSpeed = 1.0
    control.volume = 0.8
}
```

The `playbackControl` property supports [`Observation`](https://developer.apple.com/documentation/observation) in Swift, allowing SwiftUI views to update automatically as the remote playback state changes.

Report your playback metadata to `MPNowPlayingInfoCenter` so the system displays accurate now-playing information across the person’s devices.

#### Start an Application Session

Some streaming devices run dedicated apps on the remote device. Rather than playing a URL through the system media player, launch your companion app on the device and communicate with it directly. To enable bidirectional communication with the companion app through a data channel, use [`AVSystemRoute.LaunchMode.application`](avsystemroute-5s2um/launchmode/application.md) when creating the session:

```swift
let session = AVSystemRouteSession(url: url, mode: .application)
```

After starting an application session, use the [`AVSystemRouteMediaSession`](avsystemroutemediasession-98ioq.md) class’s [`dataChannel`](avsystemroutemediasession-98ioq/datachannel.md) to exchange data with the remote device. Assign an [`AVSystemRouteDataDelegate`](avsystemroutedatadelegate-7vt4b.md) to receive incoming data:

```swift
class DataHandler: AVSystemRouteDataDelegate {
    func receive(_ data: Data) async throws {
        // Process data from the remote device.
    }
}

let handler = DataHandler()

func configureDataChannel(_ mediaSession: AVSystemRouteMediaSession) {
    guard let dataChannel = mediaSession.dataChannel else { return }
    dataChannel.dataDelegate = handler
}
```

Send data to the remote device using the channel’s [`send(_:)`](avsystemroute-5s2um/datachannel/send(_:).md) method:

```swift
func sendCommand(_ command: Data, to mediaSession: AVSystemRouteMediaSession) async throws {
    guard let dataChannel = mediaSession.dataChannel else { return }
    try await dataChannel.send(command)
}
```

## See Also

- [Routing and streaming media to remote devices](routing-and-streaming-media-to-remote-devices.md)
  Send media from an app to nearby remote playback devices.
- [class AVSystemRouteController](avsystemroutecontroller-18ns8.md)
  An object that manages interaction with system routes.
- [protocol AVSystemRouteControllerObserver](avsystemroutecontrollerobserver-5syvg.md)
  A protocol for observers of a system routing controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/routing-media-to-third-party-devices)*