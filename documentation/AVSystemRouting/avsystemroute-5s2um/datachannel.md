# AVSystemRoute.DataChannel

**Framework**: AVSystemRouting  
**Kind**: class

An object that manages bidirectional data communication with a remote application.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final class DataChannel
```

## Topics

### Instance Properties
- [var dataDelegate: (any AVSystemRouteDataDelegate)?](avsystemroute-5s2um/datachannel/datadelegate.md)
  The delegate that handles incoming data from a remote application.
### Instance Methods
- [func send(Data) async throws](avsystemroute-5s2um/datachannel/send(_:).md)
  Sends data to a remote application.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class AVSystemRouteMediaSession](avsystemroutemediasession-98ioq.md)
  An object that provides playback controls and a data channel for a session running on a remote device.
- [protocol AVSystemRouteDataDelegate](avsystemroutedatadelegate-7vt4b.md)
  A protocol for handling data from a remote application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroute-5s2um/datachannel)*