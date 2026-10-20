# yield(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Resume the task awaiting the next iteration point by having it return normally from its suspension point with a given element.

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
func yield(_ value: sending Element) -> AsyncThrowingStream<Element, Failure>.Continuation.YieldResult
```

#### Return Value

A `YieldResult` that indicates the success or failure of the yield operation.

#### Discussion

If nothing is awaiting the next value, the method attempts to buffer the result’s element.

This can be called more than once and returns to the caller immediately without blocking for any awaiting consumption from the iteration.

## Parameters

- `value`: The value to yield from the continuation.

## See Also

### Producing Elements
- [func yield(with: sending Result<Element, Failure>) -> AsyncThrowingStream<Element, Failure>.Continuation.YieldResult](./yield%28with%29.md)
  Resume the task awaiting the next iteration point by having it return normally or throw, based on a given result.
- [func yield() -> AsyncThrowingStream<Element, Failure>.Continuation.YieldResult](./yield%28%29.md)
  Resume the task awaiting the next iteration point by having it return normally from its suspension point.
- [AsyncThrowingStream.Continuation.YieldResult](./yieldresult.md)
  A type that indicates the result of yielding a value to a client, by way of the continuation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingstream/continuation/yield(_:))*