# encodedPixels

**Framework**: AVFoundation  
**Kind**: property

The encoded dimensions of the image description are displayed.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static let encodedPixels: AVVideoApertureMode
```

#### Discussion

The image is not cropped to the clean aperture region and is not scaled according to the pixel aspect ratio.

## See Also

- [static let cleanAperture: AVVideoApertureMode](avvideoaperturemode/cleanaperture.md)
  The pixel aspect ratio and clean aperture will be applied.
- [static let productionAperture: AVVideoApertureMode](avvideoaperturemode/productionaperture.md)
  The pixel aspect ratio will be applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideoaperturemode/encodedpixels)*