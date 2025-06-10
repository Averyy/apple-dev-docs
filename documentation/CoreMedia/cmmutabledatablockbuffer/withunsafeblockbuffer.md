# withUnsafeBlockBuffer(_:)

**Framework**: Core Media  
**Kind**: method

Access the underlying CMBlockBuffer instance.

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
func withUnsafeBlockBuffer<R>(_ body: (CMBlockBuffer) throws -> sending R) rethrows -> sending R where R : ~Copyable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmmutabledatablockbuffer/withunsafeblockbuffer(_:))*