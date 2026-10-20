# extendedLogDataStringEncoding

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The string encoding of the extended log data.

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
var extendedLogDataStringEncoding: UInt { get }
```

```objc
@property (nonatomic, readonly) NSStringEncoding extendedLogDataStringEncoding;
```

## See Also

### Accessing log data
- [var events: [AVPlayerItemAccessLogEvent]](./events.md)
  A chronologically ordered array of player item access log events.
- [func extendedLogData() -> Data?](./extendedlogdata%28%29.md)
  Returns a serialized representation of the access log in the Extended Log File Format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslog/extendedlogdatastringencoding)*