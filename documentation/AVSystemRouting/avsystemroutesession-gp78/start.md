# start()

**Framework**: AVSystemRouting  
**Kind**: method

Starts the session and initiates media playback on the remote device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final func start() async throws -> AVSystemRouteMediaSession
```

## Mentions

- [Routing media to third-party devices](routing-media-to-third-party-devices.md)

#### Return Value

An [`AVSystemRouteMediaSession`](avsystemroutemediasession-98ioq.md) for communicating with the remote device. Access its [`dataChannel`](avsystemroutemediasession-98ioq/datachannel.md) property to send and receive data between your app and the remote application. Access its [`playbackControl`](avsystemroutemediasession-98ioq/playbackcontrol.md) property to send and receive playback commands between your app and the remote application. For [`AVSystemRoute.LaunchMode.player`](avsystemroute-5s2um/launchmode/player.md), [`dataChannel`](avsystemroutemediasession-98ioq/datachannel.md) is `nil`.

#### Discussion

Call this function to begin the playback session after adding it to an [`AVSystemRoute`](avsystemroute-5s2um.md). The session uses the URL and launch mode specified during initialization to start playback on the remote device.

When using [`AVSystemRoute.LaunchMode.application`](avsystemroute-5s2um/launchmode/application.md), your app must declare supported protocol identifiers in the `MDESupportedProtocols` key in your `Info.plist` file. These identifiers enable the system to establish communication between your app and its counterpart on the remote device.

After a successful launch with [`AVSystemRoute.LaunchMode.application`](avsystemroute-5s2um/launchmode/application.md), the returned [`AVSystemRouteMediaSession`](avsystemroutemediasession-98ioq.md) provides access to a [`dataChannel`](avsystemroutemediasession-98ioq/datachannel.md) and a [`playbackControl`](avsystemroutemediasession-98ioq/playbackcontrol.md). Use these objects to send playback commands, state updates, or custom messages between your app and the remote application.

Report playback metadata to `MPNowPlayingInfoCenter` to ensure the system displays accurate information about the current media across a person’s devices.

> **Note**: An [`AVSystemRoutingError`](avsystemroutingerror-19zkj.md) with code [`AVSystemRoutingError.Code.connectionFailed`](avsystemroutingerror-7miya/code-swift.enum/connectionfailed.md) if the launch fails (for example, if the remote device is unreachable or the session is not added to a route).

> ❗ **Important**: Call [`stop()`](avsystemroutesession-gp78/stop().md) when playback ends to properly clean up the remote session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutesession-gp78/start())*