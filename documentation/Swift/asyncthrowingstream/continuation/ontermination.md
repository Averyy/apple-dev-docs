# onTermination

**Framework**: Swift  
**Kind**: property

A callback to invoke when canceling iteration of an asynchronous stream.

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
var onTermination: ((AsyncThrowingStream<Element, Failure>.Continuation.Termination) -> Void)? { get nonmutating set }
```

#### Discussion

If an `onTermination` callback is set, using task cancellation to terminate iteration of an `AsyncThrowingStream` results in a call to this callback.

Canceling an active iteration invokes the `onTermination` callback first, and then resumes by yielding `nil` or throwing an error from the iterator. This means that you can perform needed cleanup in the cancellation handler. After reaching a terminal state, the `AsyncThrowingStream` disposes of the callback.

## See Also

- [AsyncThrowingStream.Continuation.Termination](asyncthrowingstream/continuation/termination.md)
  A type that indicates how the stream terminated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingstream/continuation/ontermination)*