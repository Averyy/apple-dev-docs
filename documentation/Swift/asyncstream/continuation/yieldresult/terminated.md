# AsyncStream.Continuation.YieldResult.terminated

**Framework**: Swift  
**Kind**: case

The stream didn’t enqueue the element because the stream was in a terminal state.

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
case terminated
```

#### Discussion

This indicates the stream terminated prior to calling `yield`, either because the stream finished normally or through cancellation.

## See Also

- [AsyncStream.Continuation.YieldResult.enqueued(remaining:)](asyncstream/continuation/yieldresult/enqueued(remaining:).md)
  The stream successfully enqueued the element.
- [AsyncStream.Continuation.YieldResult.dropped(_:)](asyncstream/continuation/yieldresult/dropped(_:).md)
  The stream didn’t enqueue the element because the buffer was full.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncstream/continuation/yieldresult/terminated)*