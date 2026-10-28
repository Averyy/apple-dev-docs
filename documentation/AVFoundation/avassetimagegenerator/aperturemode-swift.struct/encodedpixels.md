# encodedPixels

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A mode that applies neither pixel aspect ratio nor clean aperture.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let encodedPixels: AVAssetImageGenerator.ApertureMode
```

```c
extern AVAssetImageGeneratorApertureMode const AVAssetImageGeneratorApertureModeEncodedPixels;
```

## Discussion

The image isn’t cropped to the clean aperture region and isn’t scaled according to the pixel aspect ratio. It displays the image according to its encoded dimensions.

## See Also

### Aperture modes
- [static let cleanAperture: AVAssetImageGenerator.ApertureMode](./cleanaperture.md)
  A mode that applies both pixel aspect ratio and clean aperture.
- [static let productionAperture: AVAssetImageGenerator.ApertureMode](./productionaperture.md)
  A mode that applies only pixel aspect ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/aperturemode-swift.struct/encodedpixels)*