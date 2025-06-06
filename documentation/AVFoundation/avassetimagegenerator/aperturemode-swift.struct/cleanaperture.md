# cleanAperture

**Framework**: AVFoundation  
**Kind**: property

A mode that applies both pixel aspect ratio and clean aperture.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let cleanAperture: AVAssetImageGenerator.ApertureMode
```

#### Discussion

An image’s clean aperture is a region of video free from transition artifacts caused by the encoding of the signal.

## See Also

- [static let encodedPixels: AVAssetImageGenerator.ApertureMode](avassetimagegenerator/aperturemode-swift.struct/encodedpixels.md)
  A mode that applies neither pixel aspect ratio nor clean aperture.
- [static let productionAperture: AVAssetImageGenerator.ApertureMode](avassetimagegenerator/aperturemode-swift.struct/productionaperture.md)
  A mode that applies only pixel aspect ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/aperturemode-swift.struct/cleanaperture)*