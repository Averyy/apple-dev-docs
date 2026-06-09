# UnsafeThrowingContinuation

**Framework**: Swift  
**Kind**: typealias

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
typealias UnsafeThrowingContinuation<T> = UnsafeContinuation<T, any Error>
```

## See Also

- [struct CheckedContinuation](checkedcontinuation.md)
  A mechanism to interface between synchronous and asynchronous code, logging correctness violations.
- [func withCheckedContinuation<T>(isolation: isolated (any Actor)?, function: String, (CheckedContinuation<T, Never>) -> Void) async -> sending T](withcheckedcontinuation(isolation:function:_:).md)
  Source-compatibility overload; replaced by [`withCheckedContinuation(function:_:)`](withcheckedcontinuation(function:_:).md).
- [func withCheckedThrowingContinuation<T>(isolation: isolated (any Actor)?, function: String, (CheckedContinuation<T, any Error>) -> Void) async throws -> sending T](withcheckedthrowingcontinuation(isolation:function:_:).md)
  Source-compatibility overload; replaced by `withCheckedThrowingContinuation(function:_:)`.
- [struct UnsafeContinuation](unsafecontinuation.md)
  A mechanism to interface between synchronous and asynchronous code, without correctness checking.
- [func withUnsafeContinuation<T>(isolation: isolated (any Actor)?, (UnsafeContinuation<T, Never>) -> Void) async -> sending T](withunsafecontinuation(isolation:_:).md)
  Source-compatibility overload; replaced by [`withUnsafeContinuation(_:)`](withunsafecontinuation(_:).md).
- [func withUnsafeThrowingContinuation<T>(isolation: isolated (any Actor)?, (UnsafeContinuation<T, any Error>) -> Void) async throws -> sending T](withunsafethrowingcontinuation(isolation:_:).md)
  Source-compatibility overload; replaced by `withUnsafeThrowingContinuation(_:)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafethrowingcontinuation)*