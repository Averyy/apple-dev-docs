# AVPlayerItemErrorLog

**Framework**: AVFoundation  
**Kind**: class

The error log associated with a player item.

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
class AVPlayerItemErrorLog
```

## Topics

### Accessing Error Data
- [var events: [AVPlayerItemErrorLogEvent]](avplayeritemerrorlog/events.md)
  A chronologically ordered array of player item error log event objects.
- [func extendedLogData() -> Data?](avplayeritemerrorlog/extendedlogdata.md)
  Returns a serialized representation of the error log in the Extended Log File Format.
- [var extendedLogDataStringEncoding: UInt](avplayeritemerrorlog/extendedlogdatastringencoding.md)
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

## See Also

- [func accessLog() -> AVPlayerItemAccessLog?](avplayeritem/accesslog.md)
  Returns an object that represents a snapshot of the network access log.
- [class AVPlayerItemAccessLog](avplayeritemaccesslog.md)
  An object used to retrieve the access log associated with a player item.
- [class AVPlayerItemAccessLogEvent](avplayeritemaccesslogevent.md)
  A single entry in a player item’s access log.
- [func errorLog() -> AVPlayerItemErrorLog?](avplayeritem/errorlog.md)
  Returns an object that represents a snapshot of the error log.
- [class AVPlayerItemErrorLogEvent](avplayeritemerrorlogevent.md)
  A single item in a player item’s error log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlog)*