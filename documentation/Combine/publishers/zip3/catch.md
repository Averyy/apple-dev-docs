# catch(_:)

**Framework**: Combine  
**Kind**: method

Handles errors from an upstream publisher by replacing it with another publisher.

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
func `catch`<P>(_ handler: @escaping (Self.Failure) -> P) -> Publishers.Catch<Self, P> where P : Publisher, Self.Output == P.Output
```

#### Return Value

A publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher.

#### Discussion

Use `catch()` to replace an error from an upstream publisher with a new publisher.

In the example below, the `catch()` operator handles the `SimpleError` thrown by the upstream publisher by replacing the error with a `Just` publisher. This continues the stream by publishing a single value and completing normally.

```swift
struct SimpleError: Error {}
let numbers = [5, 4, 3, 2, 1, 0, 9, 8, 7, 6]
cancellable = numbers.publisher
    .tryLast(where: {
        guard $0 != 0 else {throw SimpleError()}
        return true
    })
    .catch({ (error) in
        Just(-1)
    })
    .sink { print("\($0)") }
    // Prints: -1
```

Backpressure note: This publisher passes through `request` and `cancel` to the upstream. After receiving an error, the publisher sends sends any unfulfilled demand to the new `Publisher`. SeeAlso: `replaceError`

## Parameters

- `handler`: A closure that accepts the upstream failure as input and returns a publisher to replace the upstream publisher.

## See Also

- [func assertNoFailure(String, file: StaticString, line: UInt) -> Publishers.AssertNoFailure<Self>](publishers/zip3/assertnofailure(_:file:line:).md)
  Raises a fatal error when its upstream publisher fails, and otherwise republishes all received input.
- [func tryCatch<P>((Self.Failure) throws -> P) -> Publishers.TryCatch<Self, P>](publishers/zip3/trycatch(_:).md)
  Handles errors from an upstream publisher by either replacing it with another publisher or throwing a new error.
- [func retry(Int) -> Publishers.Retry<Self>](publishers/zip3/retry(_:).md)
  Attempts to recreate a failed subscription with the upstream publisher up to the number of times you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/zip3/catch(_:))*