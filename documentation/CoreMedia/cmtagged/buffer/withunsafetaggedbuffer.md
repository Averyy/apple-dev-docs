# withUnsafeTaggedBuffer(_:)

**Framework**: Core Media  
**Kind**: method

Access the underlying CMTaggedBuffer instance.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func withUnsafeTaggedBuffer<R>(_ body: (CMTaggedBuffer) throws -> sending R) rethrows -> sending R
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtagged/buffer/withunsafetaggedbuffer(_:))*