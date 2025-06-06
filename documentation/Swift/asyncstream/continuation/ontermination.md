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
var onTermination: ((AsyncStream<Element>.Continuation.Termination) -> Void)? { get nonmutating set }
```

#### Discussion

If an `onTermination` callback is set, using task cancellation to terminate iteration of an `AsyncStream` results in a call to this callback.

Canceling an active iteration invokes the `onTermination` callback first, then resumes by yielding `nil`. This means that you can perform needed cleanup in the cancellation handler. After reaching a terminal state as a result of cancellation, the `AsyncStream` sets the callback to `nil`.

## See Also

- [AsyncStream.Continuation.Termination](asyncstream/continuation/termination.md)
  A type that indicates how the stream terminated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncstream/continuation/ontermination)*