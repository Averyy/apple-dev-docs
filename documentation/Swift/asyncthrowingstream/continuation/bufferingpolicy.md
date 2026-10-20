# AsyncThrowingStream.Continuation.BufferingPolicy

**Framework**: Swift  
**Kind**: enum  
**Role**: Enumeration

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
- [AsyncThrowingStream.Continuation.BufferingPolicy.unbounded](./bufferingpolicy/unbounded.md)
  Continue to add to the buffer, without imposing a limit on the number of buffered elements.
- [AsyncThrowingStream.Continuation.BufferingPolicy.bufferingOldest(_:)](./bufferingpolicy/bufferingoldest%28_%29.md)
  When the buffer is full, discard the newly received element.
- [AsyncThrowingStream.Continuation.BufferingPolicy.bufferingNewest(_:)](./bufferingpolicy/bufferingnewest%28_%29.md)
  When the buffer is full, discard the oldest element in the buffer.

## Relationships

### Conforms To
- [Sendable](../../sendable.md)
- [SendableMetatype](../../sendablemetatype.md)

## See Also

### Creating a Continuation-Based Stream
- [init(Element.Type, bufferingPolicy: AsyncThrowingStream<Element, Failure>.Continuation.BufferingPolicy, (AsyncThrowingStream<Element, Failure>.Continuation) -> Void)](../init%28_,bufferingpolicy,_%29.md)
  Constructs an asynchronous stream for an element type, using the specified buffering policy and element-producing closure.
- [AsyncThrowingStream.Continuation](../continuation.md)
  A mechanism to interface between synchronous code and an asynchronous stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingstream/continuation/bufferingpolicy)*