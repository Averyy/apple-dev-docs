# AVSystemRouteSession

**Framework**: AVSystemRouting  
**Kind**: class

An object that manages a single media playback session on a remote device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final class AVSystemRouteSession
```

## Mentions

- [Routing and streaming media to remote devices](routing-and-streaming-media-to-remote-devices.md)
- [Routing media to third-party devices](routing-media-to-third-party-devices.md)

#### Overview

[`AVSystemRouteSession`](avsystemroutesession-gp78.md) manages a single media playback session on a remote device. Create a session to initiate playback on a connected device, communicate with a remote application, and control the lifecycle of the remote playback experience.

To use a session:

1. Create an [`AVSystemRouteSession`](avsystemroutesession-gp78.md) with a URL and launch mode
2. Add the session to an [`AVSystemRoute`](avsystemroute-5s2um.md) using [`addSession(_:)`](avsystemroute-5s2um/addsession(_:).md)
3. Start the session with [`start()`](avsystemroutesession-gp78/start().md)
4. Use the returned [`AVSystemRouteMediaSession`](avsystemroutemediasession-98ioq.md) to communicate with the remote device
5. Call [`stop()`](avsystemroutesession-gp78/stop().md) when playback ends to clean up resources

Sessions are single-use. After calling [`stop()`](avsystemroutesession-gp78/stop().md), the session cannot be restarted or added to another route. Create a new [`AVSystemRouteSession`](avsystemroutesession-gp78.md) for each new playback.

#### Reporting Playback Metadata

Report playback metadata to `MPNowPlayingInfoCenter` to ensure the system displays accurate information about the current media across a person’s devices and in system UI.

## Topics

### Initializers
- [init(url: URL, mode: AVSystemRoute.LaunchMode)](avsystemroutesession-gp78/init(url:mode:).md)
  Creates a session for initiating playback on a remote device.
### Instance Methods
- [func start() async throws -> AVSystemRouteMediaSession](avsystemroutesession-gp78/start.md)
  Starts the session and initiates media playback on the remote device.
- [func stop()](avsystemroutesession-gp78/stop.md)
  Stops the session and terminates media playback on the remote device.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class AVSystemRoute](avsystemroute-5s2um.md)
  An active media route to a remote device that manages connection and communication for media playback and data exchange.
- [AVSystemRoute.LaunchMode](avsystemroute-5s2um/launchmode.md)
  The mode that determines how media playback launches on a remote device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutesession-gp78)*