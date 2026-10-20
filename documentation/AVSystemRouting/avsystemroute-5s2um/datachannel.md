# AVSystemRoute.DataChannel

**Framework**: AVSystemRouting  
**Kind**: class  
**Role**: Class

An object that manages bidirectional data communication with a remote application.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
final class DataChannel
```

## Topics

### Instance Properties
- [var dataDelegate: (any AVSystemRouteDataDelegate)?](./datachannel/datadelegate.md)
  The delegate that handles incoming data from a remote application.
### Instance Methods
- [func send(Data) async throws](./datachannel/send%28_%29.md)
  Sends data to a remote application.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Playback and communication
- [class AVSystemRouteMediaSession](../avsystemroutemediasession-98ioq.md)
  An object that provides playback controls and a data channel for a session running on a remote device.
- [protocol AVSystemRouteDataDelegate](../avsystemroutedatadelegate-7vt4b.md)
  A protocol for handling data from a remote application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroute-5s2um/datachannel)*