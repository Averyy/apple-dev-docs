# StreamDelegate

**Framework**: Foundation  
**Kind**: protocol

An interface that delegates of a stream instance use to handle events on the stream.

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
protocol StreamDelegate : NSObjectProtocol
```

## Mentions

- [Uploading streams of data](uploading-streams-of-data.md)

## Topics

### Using Streams
- [func stream(Stream, handle: Stream.Event)](streamdelegate/stream(_:handle:).md)
  The delegate receives this message when a given event has occurred on a given stream.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class Stream](stream.md)
  An abstract class representing a stream.
- [class InputStream](inputstream.md)
  A stream that provides read-only stream functionality.
- [class OutputStream](outputstream.md)
  A stream that provides write-only stream functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/streamdelegate)*