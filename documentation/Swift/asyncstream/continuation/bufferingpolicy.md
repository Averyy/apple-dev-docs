# AsyncStream.Continuation.BufferingPolicy

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
- [AsyncStream.Continuation.BufferingPolicy.unbounded](./bufferingpolicy/unbounded.md)
  Continue to add to the buffer, without imposing a limit on the number of buffered elements.
- [AsyncStream.Continuation.BufferingPolicy.bufferingOldest(_:)](./bufferingpolicy/bufferingoldest%28_%29.md)
  When the buffer is full, discard the newly received element.
- [AsyncStream.Continuation.BufferingPolicy.bufferingNewest(_:)](./bufferingpolicy/bufferingnewest%28_%29.md)
  When the buffer is full, discard the oldest element in the buffer.

## Relationships

### Conforms To
- [Sendable](../../sendable.md)
- [SendableMetatype](../../sendablemetatype.md)

## See Also

### Creating a Continuation-Based Stream
- [init(Element.Type, bufferingPolicy: AsyncStream<Element>.Continuation.BufferingPolicy, (AsyncStream<Element>.Continuation) -> Void)](../init%28_,bufferingpolicy,_%29.md)
  Constructs an asynchronous stream for an element type, using the specified buffering policy and element-producing closure.
- [AsyncStream.Continuation](../continuation.md)
  A mechanism to interface between synchronous code and an asynchronous stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncstream/continuation/bufferingpolicy)*