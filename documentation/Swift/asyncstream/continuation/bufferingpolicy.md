# AsyncStream.Continuation.BufferingPolicy

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
- [AsyncStream.Continuation.BufferingPolicy.unbounded](asyncstream/continuation/bufferingpolicy/unbounded.md)
  Continue to add to the buffer, without imposing a limit on the number of buffered elements.
- [AsyncStream.Continuation.BufferingPolicy.bufferingOldest(_:)](asyncstream/continuation/bufferingpolicy/bufferingoldest(_:).md)
  When the buffer is full, discard the newly received element.
- [AsyncStream.Continuation.BufferingPolicy.bufferingNewest(_:)](asyncstream/continuation/bufferingpolicy/bufferingnewest(_:).md)
  When the buffer is full, discard the oldest element in the buffer.

## Relationships

### Conforms To
- [Sendable](sendable.md)

## See Also

- [init(Element.Type, bufferingPolicy: AsyncStream<Element>.Continuation.BufferingPolicy, (AsyncStream<Element>.Continuation) -> Void)](asyncstream/init(_:bufferingpolicy:_:).md)
  Constructs an asynchronous stream for an element type, using the specified buffering policy and element-producing closure.
- [AsyncStream.Continuation](asyncstream/continuation.md)
  A mechanism to interface between synchronous code and an asynchronous stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncstream/continuation/bufferingpolicy)*