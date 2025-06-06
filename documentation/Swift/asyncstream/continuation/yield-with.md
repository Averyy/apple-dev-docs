# yield(with:)

**Framework**: Swift  
**Kind**: method

Resume the task awaiting the next iteration point by having it return normally from its suspension point with a given result’s success value.

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
func yield(with result: sending Result<Element, Never>) -> AsyncStream<Element>.Continuation.YieldResult
```

#### Return Value

A `YieldResult` that indicates the success or failure of the yield operation.

#### Discussion

If nothing is awaiting the next value, the method attempts to buffer the result’s element.

If you call this method repeatedly, each call returns immediately, without blocking for any awaiting consumption from the iteration.

## Parameters

- `result`: A result to yield from the continuation.

## See Also

- [func yield(sending Element) -> AsyncStream<Element>.Continuation.YieldResult](asyncstream/continuation/yield(_:).md)
  Resume the task awaiting the next iteration point by having it return normally from its suspension point with a given element.
- [func yield() -> AsyncStream<Element>.Continuation.YieldResult](asyncstream/continuation/yield.md)
  Resume the task awaiting the next iteration point by having it return normally from its suspension point.
- [AsyncStream.Continuation.YieldResult](asyncstream/continuation/yieldresult.md)
  A type that indicates the result of yielding a value to a client, by way of the continuation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncstream/continuation/yield(with:))*