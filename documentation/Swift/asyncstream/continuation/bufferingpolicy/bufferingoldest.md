# AsyncStream.Continuation.BufferingPolicy.bufferingOldest(_:)

**Framework**: Swift  
**Kind**: case

When the buffer is full, discard the newly received element.

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
case bufferingOldest(Int)
```

#### Discussion

This strategy enforces keeping at most the specified number of oldest values.

> **Note**: If the specified number is zero or negative, no elements are buffered. In that case, an iterator receives an element only if it is already awaiting a value when the continuation yields.

## See Also

- [AsyncStream.Continuation.BufferingPolicy.unbounded](asyncstream/continuation/bufferingpolicy/unbounded.md)
  Continue to add to the buffer, without imposing a limit on the number of buffered elements.
- [AsyncStream.Continuation.BufferingPolicy.bufferingNewest(_:)](asyncstream/continuation/bufferingpolicy/bufferingnewest(_:).md)
  When the buffer is full, discard the oldest element in the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncstream/continuation/bufferingpolicy/bufferingoldest(_:))*