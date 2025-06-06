# events

**Framework**: AVFoundation  
**Kind**: property

A chronologically ordered array of player item error log event objects.

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
var events: [AVPlayerItemErrorLogEvent] { get }
```

#### Discussion

The array contains [`AVPlayerItemErrorLogEvent`](avplayeritemerrorlogevent.md) objects that represent the chronological sequence of events contained in the error log.

This property isn’t observable. For more information about key-value observing, see [`Using Key-Value Observing in Swift`](https://developer.apple.com/documentation/Swift/using-key-value-observing-in-swift).

## See Also

- [func extendedLogData() -> Data?](avplayeritemerrorlog/extendedlogdata.md)
  Returns a serialized representation of the error log in the Extended Log File Format.
- [var extendedLogDataStringEncoding: UInt](avplayeritemerrorlog/extendedlogdatastringencoding.md)
  The string encoding of the extended log data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlog/events)*