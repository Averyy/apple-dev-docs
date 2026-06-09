# withUnsafeThrowingContinuation(_:)

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
nonisolated
(nonsending) func withUnsafeThrowingContinuation<T>(_ fn: (UnsafeContinuation<T, any Error>) -> Void) async throws -> sending T
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/withunsafethrowingcontinuation(_:)-7zhvy)*