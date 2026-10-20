# vImageCVImageFormat.ChromaSiting

**Framework**: Accelerate  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the chrominance siting of a Core Video image format.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS
- watchOS 6.0+

## Declaration

```swift
enum ChromaSiting
```

## Topics

### Chrominance siting constants
- [vImageCVImageFormat.ChromaSiting.top](./chromasiting-swift.enum/top.md)
  The chrominance sample is horizontally centered, but co-sited with the top row of luminance samples.
- [vImageCVImageFormat.ChromaSiting.topLeft](./chromasiting-swift.enum/topleft.md)
  The chrominance sample is co-sited with the top-left luminance sample.
- [vImageCVImageFormat.ChromaSiting.bottom](./chromasiting-swift.enum/bottom.md)
  The chrominance sample is horizontally centered, but co-sited with the bottom row of luminance samples.
- [vImageCVImageFormat.ChromaSiting.bottomLeft](./chromasiting-swift.enum/bottomleft.md)
  The chrominance sample is co-sited with the bottom-left luminance sample.
- [vImageCVImageFormat.ChromaSiting.left](./chromasiting-swift.enum/left.md)
  The chrominance sample is horizontally co-sited with the left column of luminance samples, but centered vertically.
- [vImageCVImageFormat.ChromaSiting.center](./chromasiting-swift.enum/center.md)
  The chrominance sample is fully centered.
- [vImageCVImageFormat.ChromaSiting.dv420](./chromasiting-swift.enum/dv420.md)
  The Cr and Cb samples are alternately co-sited with the left luminance samples of the same field.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Supporting types
- [vImageCVImageFormat.Format](./format.md)
  Constants that specify the format of a Core Video image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat/chromasiting-swift.enum)*