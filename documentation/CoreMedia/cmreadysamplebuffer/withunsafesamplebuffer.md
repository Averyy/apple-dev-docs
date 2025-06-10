# withUnsafeSampleBuffer(_:)

**Framework**: Core Media  
**Kind**: method

Access the underlying CMSampleBuffer instance.

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
func withUnsafeSampleBuffer<R>(_ body: (CMSampleBuffer) throws -> sending R) rethrows -> sending R where R : ~Copyable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadysamplebuffer/withunsafesamplebuffer(_:))*