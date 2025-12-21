# endEncountered

**Framework**: Foundation  
**Kind**: property

The end of the stream has been reached.

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
static var endEncountered: Stream.Event { get }
```

## See Also

- [static var openCompleted: Stream.Event](stream/event/opencompleted.md)
  The open has completed successfully.
- [static var hasBytesAvailable: Stream.Event](stream/event/hasbytesavailable.md)
  The stream has bytes to be read.
- [static var hasSpaceAvailable: Stream.Event](stream/event/hasspaceavailable.md)
  The stream can accept bytes for writing.
- [static var errorOccurred: Stream.Event](stream/event/erroroccurred.md)
  An error has occurred on the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stream/event/endencountered)*