# AVSystemRouteMediaSession

**Framework**: AVSystemRouting  
**Kind**: class

An object that provides playback controls and a data channel for a session running on a remote device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final class AVSystemRouteMediaSession
```

## Mentions

- [Routing and streaming media to remote devices](routing-and-streaming-media-to-remote-devices.md)
- [Routing media to third-party devices](routing-media-to-third-party-devices.md)

#### Overview

Use this object to access playback controls and a data channel for communicating with the remote application. Call [`start()`](avsystemroutesession-gp78/start().md) to get this object after adding a session to an [`AVSystemRoute`](avsystemroute-5s2um.md).

## Topics

### Instance Properties
- [var dataChannel: AVSystemRoute.DataChannel?](avsystemroutemediasession-98ioq/datachannel.md)
  The data channel for sending and receiving data with the remote app.
- [var playbackControl: (any AVPlaybackUserInterfaceControllable)?](avsystemroutemediasession-98ioq/playbackcontrol.md)
  The playback control interface for the remote session.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [AVSystemRoute.DataChannel](avsystemroute-5s2um/datachannel.md)
  An object that manages bidirectional data communication with a remote application.
- [protocol AVSystemRouteDataDelegate](avsystemroutedatadelegate-7vt4b.md)
  A protocol for handling data from a remote application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutemediasession-98ioq)*