# withUnsafeTaggedBuffers(_:)

**Framework**: Swift  
**Kind**: method

Access the underlying CMTaggedBuffers.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func withUnsafeTaggedBuffers<R>(_ body: ([CMTaggedBuffer]) throws -> sending R) rethrows -> sending R where R : ~Copyable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/withunsafetaggedbuffers(_:))*