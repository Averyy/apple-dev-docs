# CVImageChromaField.ChromaSubsampling

**Framework**: Core Video  
**Kind**: enum  
**Role**: Enumeration

Original format of subsampled data in the image buffer before conversion to 422/2vuy format.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
enum ChromaSubsampling
```

## Overview

Note: To use these values, ensure that the image buffer data was converted to 4:2:2 format using simple pixel replication.

## Topics

### Enumeration Cases
- [CVImageChromaField.ChromaSubsampling.4:1:1](./chromasubsampling/api-4_1_1.md)
  The original chroma-subsampled data used 4:1:1 formatting.
- [CVImageChromaField.ChromaSubsampling.4:2:0](./chromasubsampling/api-4_2_0.md)
  The original chroma-subsampled data used 4:2:0 formatting.
- [CVImageChromaField.ChromaSubsampling.4:2:2](./chromasubsampling/api-4_2_2.md)
  The original chroma-subsampled data used 4:2:2 formatting.

## Relationships

### Conforms To
- [CVAttachmentValueRepresentable](../cvattachmentvaluerepresentable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagechromafield/chromasubsampling)*