# openCompleted

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The open has completed successfully.

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
static var openCompleted: Stream.Event { get }
```

```c
NSStreamEventOpenCompleted
```

## See Also

### Constants
- [static var hasBytesAvailable: Stream.Event](./hasbytesavailable.md)
  The stream has bytes to be read.
- [static var hasSpaceAvailable: Stream.Event](./hasspaceavailable.md)
  The stream can accept bytes for writing.
- [static var errorOccurred: Stream.Event](./erroroccurred.md)
  An error has occurred on the stream.
- [static var endEncountered: Stream.Event](./endencountered.md)
  The end of the stream has been reached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stream/event/opencompleted)*