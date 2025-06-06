# makeStream(of:bufferingPolicy:)

**Framework**: Swift  
**Kind**: method

Initializes a new [`AsyncStream`](asyncstream.md) and an [`AsyncStream.Continuation`](asyncstream/continuation.md).

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@backDeployed(before: macOS 14.0, iOS 17.0, watchOS 10.0, tvOS 17.0)
static func makeStream(of elementType: Element.Type = Element.self, bufferingPolicy limit: AsyncStream<Element>.Continuation.BufferingPolicy = .unbounded) -> (stream: AsyncStream<Element>, continuation: AsyncStream<Element>.Continuation)
```

#### Return Value

A tuple containing the stream and its continuation. The continuation should be passed to the producer while the stream should be passed to the consumer.

## Parameters

- `elementType`: The element type of the stream.
- `limit`: The buffering policy that the stream should use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncstream/makestream(of:bufferingpolicy:))*