# withCheckedThrowingContinuation(function:_:)

**Framework**: Swift  
**Kind**: func

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
@abi(nonisolated(nonsending) func withCheckedThrowingContinuationNonisolatedNonsending<T>(function: String, _ body: (CheckedContinuation<T, any Error>) -> Void) async throws -> sending T) nonisolated(nonsending) func withCheckedThrowingContinuation<T>(function: String = #function, _ body: (CheckedContinuation<T, any Error>) -> Void) async throws -> sending T
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/withcheckedthrowingcontinuation(function:_:)-13yf6)*