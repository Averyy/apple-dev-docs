# yield()

**Framework**: Swift  
**Kind**: method

Resume the task awaiting the next iteration point by having it return normally from its suspension point.

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
@discardableResult
func yield() -> AsyncThrowingStream<Element, Failure>.Continuation.YieldResult where Element == ()
```

#### Return Value

A `YieldResult` that indicates the success or failure of the yield operation.

#### Discussion

Use this method with `AsyncThrowingStream` instances whose `Element` type is `Void`. In this case, the `yield()` call unblocks the awaiting iteration; there is no value to return.

If you call this method repeatedly, each call returns immediately, without blocking for any awaiting consumption from the iteration.

## See Also

- [func yield(sending Element) -> AsyncThrowingStream<Element, Failure>.Continuation.YieldResult](asyncthrowingstream/continuation/yield(_:).md)
  Resume the task awaiting the next iteration point by having it return normally from its suspension point with a given element.
- [func yield(with: sending Result<Element, Failure>) -> AsyncThrowingStream<Element, Failure>.Continuation.YieldResult](asyncthrowingstream/continuation/yield(with:).md)
  Resume the task awaiting the next iteration point by having it return normally or throw, based on a given result.
- [AsyncThrowingStream.Continuation.YieldResult](asyncthrowingstream/continuation/yieldresult.md)
  A type that indicates the result of yielding a value to a client, by way of the continuation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingstream/continuation/yield())*