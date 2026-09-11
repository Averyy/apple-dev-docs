# CVImageChromaField.SampleLocation

**Framework**: Core Video  
**Kind**: enum

Indicates the locations of the chroma sample in the image buffer.

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
enum SampleLocation
```

## Topics

### Enumeration Cases
- [CVImageChromaField.SampleLocation.bottom](cvimagechromafield/samplelocation/bottom.md)
  Chroma sample is horizontally centered, but is co-sited with the bottom row of luma samples.
- [CVImageChromaField.SampleLocation.bottomLeft](cvimagechromafield/samplelocation/bottomleft.md)
  Chroma sample is co-sited with the bottom-left luma sample.
- [CVImageChromaField.SampleLocation.center](cvimagechromafield/samplelocation/center.md)
  Chroma sample is fully centered.
- [CVImageChromaField.SampleLocation.dv420](cvimagechromafield/samplelocation/dv420.md)
  The Cr and Cb samples are alternatingly co-sited with the left luma samples of the same field.
- [CVImageChromaField.SampleLocation.left](cvimagechromafield/samplelocation/left.md)
  Chroma sample is horizontally co-sited with the left column of luma samples, but centered vertically.
- [CVImageChromaField.SampleLocation.top](cvimagechromafield/samplelocation/top.md)
  Chroma sample is horizontally centered, but is co-sited with the top row of luma samples.
- [CVImageChromaField.SampleLocation.topLeft](cvimagechromafield/samplelocation/topleft.md)
  Chroma sample is co-sited with the top-left luma sample.

## Relationships

### Conforms To
- [CVAttachmentValueRepresentable](cvattachmentvaluerepresentable.md)
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagechromafield/samplelocation)*