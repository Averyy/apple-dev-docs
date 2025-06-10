# isDependedOnByOthers

**Framework**: Core Media  
**Kind**: property

Indicates whether other samples depend on this sample for decoding.

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
var isDependedOnByOthers: Bool? { get set }
```

#### Discussion

This key has no default value. If this key is not present, dependency information for the sample is unknown. If this key is present and its value is false, the frame is considered droppable.

This attachment is read from and written to media files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/sampleattachments-swift.struct/isdependedonbyothers)*