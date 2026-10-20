# AVSystemRouteDataDelegate

**Framework**: AVSystemRouting  
**Kind**: protocol  
**Role**: Protocol

A protocol for handling data from a remote application.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
protocol AVSystemRouteDataDelegate : AnyObject
```

## Mentions

- [Routing and streaming media to remote devices](./routing-and-streaming-media-to-remote-devices.md)
- [Routing media to third-party devices](./routing-media-to-third-party-devices.md)

## Topics

### Instance Methods
- [func receive(Data) async throws](./avsystemroutedatadelegate-7vt4b/receive%28_%29.md)
  Receives data sent from a connected remote applicaiton.

## See Also

### Playback and communication
- [class AVSystemRouteMediaSession](./avsystemroutemediasession-98ioq.md)
  An object that provides playback controls and a data channel for a session running on a remote device.
- [AVSystemRoute.DataChannel](./avsystemroute-5s2um/datachannel.md)
  An object that manages bidirectional data communication with a remote application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutedatadelegate-7vt4b)*