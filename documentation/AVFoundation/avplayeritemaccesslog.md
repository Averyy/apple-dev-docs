# AVPlayerItemAccessLog

**Framework**: AVFoundation  
**Kind**: class

An object used to retrieve the access log associated with a player item.

**Availability**:
- iOS 4.3+
- iPadOS 4.3+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class AVPlayerItemAccessLog
```

#### Overview

An `AVPlayerItemAccessLog` object accumulates key metrics about network playback and presents them as a collection of [`AVPlayerItemAccessLogEvent`](avplayeritemaccesslogevent.md) instances. Each event instance collates the data that relates to each uninterrupted period of playback.

## Topics

### Accessing Log Data
- [var events: [AVPlayerItemAccessLogEvent]](avplayeritemaccesslog/events.md)
  A chronologically ordered array of player item access log events.
- [func extendedLogData() -> Data?](avplayeritemaccesslog/extendedlogdata.md)
  Returns a serialized representation of the access log in the Extended Log File Format.
- [var extendedLogDataStringEncoding: UInt](avplayeritemaccesslog/extendedlogdatastringencoding.md)
  The string encoding of the extended log data.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func accessLog() -> AVPlayerItemAccessLog?](avplayeritem/accesslog.md)
  Returns an object that represents a snapshot of the network access log.
- [class AVPlayerItemAccessLogEvent](avplayeritemaccesslogevent.md)
  A single entry in a player item’s access log.
- [func errorLog() -> AVPlayerItemErrorLog?](avplayeritem/errorlog.md)
  Returns an object that represents a snapshot of the error log.
- [class AVPlayerItemErrorLog](avplayeritemerrorlog.md)
  The error log associated with a player item.
- [class AVPlayerItemErrorLogEvent](avplayeritemerrorlogevent.md)
  A single item in a player item’s error log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslog)*