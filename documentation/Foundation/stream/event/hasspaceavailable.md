# hasSpaceAvailable

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The stream can accept bytes for writing.

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
static var hasSpaceAvailable: Stream.Event { get }
```

```c
NSStreamEventHasSpaceAvailable
```

## Mentions

- [Uploading streams of data](../../uploading-streams-of-data.md)

## See Also

### Constants
- [static var openCompleted: Stream.Event](./opencompleted.md)
  The open has completed successfully.
- [static var hasBytesAvailable: Stream.Event](./hasbytesavailable.md)
  The stream has bytes to be read.
- [static var errorOccurred: Stream.Event](./erroroccurred.md)
  An error has occurred on the stream.
- [static var endEncountered: Stream.Event](./endencountered.md)
  The end of the stream has been reached.
- [NSStreamEventNone](../../nsstreamevent/nsstreameventnone.md)
  No event has occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stream/event/hasspaceavailable)*