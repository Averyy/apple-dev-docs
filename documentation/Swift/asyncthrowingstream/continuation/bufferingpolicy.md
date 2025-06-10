# AsyncThrowingStream.Continuation.BufferingPolicy

**Framework**: Swift  
**Kind**: enum

A strategy that handles exhaustion of a buffer’s capacity.

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
enum BufferingPolicy
```

## Topics

### Buffering Policies
- [AsyncThrowingStream.Continuation.BufferingPolicy.unbounded](asyncthrowingstream/continuation/bufferingpolicy/unbounded.md)
  Continue to add to the buffer, treating its capacity as infinite.
- [AsyncThrowingStream.Continuation.BufferingPolicy.bufferingOldest(_:)](asyncthrowingstream/continuation/bufferingpolicy/bufferingoldest(_:).md)
  When the buffer is full, discard the newly received element.
- [AsyncThrowingStream.Continuation.BufferingPolicy.bufferingNewest(_:)](asyncthrowingstream/continuation/bufferingpolicy/bufferingnewest(_:).md)
  When the buffer is full, discard the oldest element in the buffer.

## Relationships

### Conforms To
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [init(Element.Type, bufferingPolicy: AsyncThrowingStream<Element, Failure>.Continuation.BufferingPolicy, (AsyncThrowingStream<Element, Failure>.Continuation) -> Void)](asyncthrowingstream/init(_:bufferingpolicy:_:).md)
  Constructs an asynchronous stream for an element type, using the specified buffering policy and element-producing closure.
- [AsyncThrowingStream.Continuation](asyncthrowingstream/continuation.md)
  A mechanism to interface between synchronous code and an asynchronous stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingstream/continuation/bufferingpolicy)*