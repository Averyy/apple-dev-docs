# streamError

**Framework**: Foundation  
**Kind**: property

Returns an `NSError` object representing the stream error.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var streamError: (any Error)? { get }
```

#### Return Value

An `NSError` object representing the stream error, or `nil` if no error has been encountered.

## See Also

- [var streamStatus: Stream.Status](stream/streamstatus.md)
  Returns the receiver’s status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stream/streamerror)*