# AVPlayerItemAccessLog

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVPlayerItemAccessLog : NSObject
```

## Overview

An `AVPlayerItemAccessLog` object accumulates key metrics about network playback and presents them as a collection of [`AVPlayerItemAccessLogEvent`](./avplayeritemaccesslogevent.md) instances. Each event instance collates the data that relates to each uninterrupted period of playback.

## Topics

### Accessing log data
- [var events: [AVPlayerItemAccessLogEvent]](./avplayeritemaccesslog/events.md)
  A chronologically ordered array of player item access log events.
- [func extendedLogData() -> Data?](./avplayeritemaccesslog/extendedlogdata%28%29.md)
  Returns a serialized representation of the access log in the Extended Log File Format.
- [var extendedLogDataStringEncoding: UInt](./avplayeritemaccesslog/extendedlogdatastringencoding.md)
  The string encoding of the extended log data.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing logging information
- [func accessLog() -> AVPlayerItemAccessLog?](./avplayeritem/accesslog%28%29.md)
  Returns an object that represents a snapshot of the network access log.
- [class AVPlayerItemAccessLogEvent](./avplayeritemaccesslogevent.md)
  A single entry in a player item’s access log.
- [func errorLog() -> AVPlayerItemErrorLog?](./avplayeritem/errorlog%28%29.md)
  Returns an object that represents a snapshot of the error log.
- [class AVPlayerItemErrorLog](./avplayeritemerrorlog.md)
  The error log associated with a player item.
- [class AVPlayerItemErrorLogEvent](./avplayeritemerrorlogevent.md)
  A single item in a player item’s error log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslog)*