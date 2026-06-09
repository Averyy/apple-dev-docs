# CVImageChromaField.ChromaSubsampling

**Framework**: Core Video  
**Kind**: enum

Original format of subsampled data in the image buffer before conversion to 422/2vuy format.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum ChromaSubsampling
```

#### Overview

Note: To use these values, ensure that the image buffer data was converted to 4:2:2 format using simple pixel replication.

## Topics

### Enumeration Cases
- [CVImageChromaField.ChromaSubsampling.4:1:1](cvimagechromafield/chromasubsampling/4:1:1.md)
  The original chroma-subsampled data used 4:1:1 formatting.
- [CVImageChromaField.ChromaSubsampling.4:2:0](cvimagechromafield/chromasubsampling/4:2:0.md)
  The original chroma-subsampled data used 4:2:0 formatting.
- [CVImageChromaField.ChromaSubsampling.4:2:2](cvimagechromafield/chromasubsampling/4:2:2.md)
  The original chroma-subsampled data used 4:2:2 formatting.

## Relationships

### Conforms To
- [CVAttachmentValueRepresentable](cvattachmentvaluerepresentable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagechromafield/chromasubsampling)*