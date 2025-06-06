# stream(_:handle:)

**Framework**: Foundation  
**Kind**: method

The delegate receives this message when a given event has occurred on a given stream.

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
optional func stream(_ aStream: Stream, handle eventCode: Stream.Event)
```

## Mentions

- [Uploading streams of data](uploading-streams-of-data.md)

#### Discussion

The delegate receives this message only if `theStream` is scheduled on a run loop. The message is sent on the stream object’s thread. The delegate should examine `streamEvent` to determine the appropriate action it should take.

## Parameters

- `aStream`: The stream on which   occurred.
- `eventCode`: The stream event that occurred.

## See Also

- [Stream Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Streams/Streams.html#//apple_ref/doc/uid/10000188i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/streamdelegate/stream(_:handle:))*