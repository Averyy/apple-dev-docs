# withUnsafeSampleBuffer(_:)

**Framework**: Core Media  
**Kind**: method

Access the underlying CMSampleBuffer instance.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func withUnsafeSampleBuffer<R>(_ body: (CMSampleBuffer) throws -> sending R) rethrows -> sending R where R : ~Copyable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmreadysamplebuffer/withunsafesamplebuffer(_:))*