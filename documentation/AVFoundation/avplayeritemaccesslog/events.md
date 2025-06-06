# events

**Framework**: AVFoundation  
**Kind**: property

A chronologically ordered array of player item access log events.

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
var events: [AVPlayerItemAccessLogEvent] { get }
```

#### Discussion

The array contains [`AVPlayerItemAccessLogEvent`](avplayeritemaccesslogevent.md) objects that represent the chronological sequence of events contained in the access log.

This property isn’t observable. For more information about key-value observing, see [`Using Key-Value Observing in Swift`](https://developer.apple.com/documentation/Swift/using-key-value-observing-in-swift).

## See Also

- [func extendedLogData() -> Data?](avplayeritemaccesslog/extendedlogdata.md)
  Returns a serialized representation of the access log in the Extended Log File Format.
- [var extendedLogDataStringEncoding: UInt](avplayeritemaccesslog/extendedlogdatastringencoding.md)
  The string encoding of the extended log data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslog/events)*