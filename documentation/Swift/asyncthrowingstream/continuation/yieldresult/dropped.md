# AsyncThrowingStream.Continuation.YieldResult.dropped(_:)

**Framework**: Swift  
**Kind**: case

The stream didn’t enqueue the element because the buffer was full.

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
case dropped(Element)
```

#### Discussion

The associated element for this case is the element that the stream dropped.

## See Also

- [AsyncThrowingStream.Continuation.YieldResult.enqueued(remaining:)](asyncthrowingstream/continuation/yieldresult/enqueued(remaining:).md)
  The stream successfully enqueued the element.
- [AsyncThrowingStream.Continuation.YieldResult.terminated](asyncthrowingstream/continuation/yieldresult/terminated.md)
  The stream didn’t enqueue the element because the stream was in a terminal state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingstream/continuation/yieldresult/dropped(_:))*