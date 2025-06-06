# AsyncThrowingStream.Continuation.BufferingPolicy.unbounded

**Framework**: Swift  
**Kind**: case

Continue to add to the buffer, treating its capacity as infinite.

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
case unbounded
```

## See Also

- [AsyncThrowingStream.Continuation.BufferingPolicy.bufferingOldest(_:)](asyncthrowingstream/continuation/bufferingpolicy/bufferingoldest(_:).md)
  When the buffer is full, discard the newly received element.
- [AsyncThrowingStream.Continuation.BufferingPolicy.bufferingNewest(_:)](asyncthrowingstream/continuation/bufferingpolicy/bufferingnewest(_:).md)
  When the buffer is full, discard the oldest element in the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingstream/continuation/bufferingpolicy/unbounded)*