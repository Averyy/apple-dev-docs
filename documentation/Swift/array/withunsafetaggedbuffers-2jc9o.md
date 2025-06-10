# withUnsafeTaggedBuffers(_:)

**Framework**: Swift  
**Kind**: method

Access the underlying CMTaggedBuffers.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func withUnsafeTaggedBuffers<R>(_ body: ([CMTaggedBuffer]) throws -> sending R) rethrows -> sending R where R : ~Copyable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/withunsafetaggedbuffers(_:)-2jc9o)*