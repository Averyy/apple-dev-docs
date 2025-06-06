# init(continuation:function:)

**Framework**: Swift  
**Kind**: init

Creates a checked continuation from an unsafe continuation.

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
init(continuation: UnsafeContinuation<T, E>, function: String = #function)
```

#### Discussion

Instead of calling this initializer, most code calls the `withCheckedContinuation(function:_:)` or `withCheckedThrowingContinuation(function:_:)` function instead. You only need to initialize your own `CheckedContinuation<T, E>` if you already have an `UnsafeContinuation` you want to impose checking on.

## Parameters

- `continuation`: An instance of    that hasn’t yet been resumed.   After passing the unsafe continuation to this initializer,   don’t use it outside of this object.
- `function`: A string identifying the declaration that is the notional   source for the continuation, used to identify the continuation in   runtime diagnostics related to misuse of this continuation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/checkedcontinuation/init(continuation:function:))*