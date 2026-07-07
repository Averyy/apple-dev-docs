# nominalFocalLengthIn35mmFilm

**Framework**: AVFoundation  
**Kind**: property

The nominal 35mm equivalent focal length of the capture device’s lens.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var nominalFocalLengthIn35mmFilm: Float { get }
```

#### Discussion

This value represents a nominal measurement of the device’s field of view, expressed as a 35mm equivalent focal length, measured diagonally. The value is similar to the `FocalLengthIn35mmFormat` EXIF entry (see [`kCGImagePropertyExifFocalLenIn35mmFilm`](https://developer.apple.com/documentation/ImageIO/kCGImagePropertyExifFocalLenIn35mmFilm)) for a photo captured using the device’s format where [`isHighestPhotoQualitySupported`](avcapturedevice/format/ishighestphotoqualitysupported.md) is `true` or when you’ve configured the session with the [`photo`](avcapturesession/preset/photo.md) preset.

This property value is `0` for virtual devices and external cameras.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/nominalfocallengthin35mmfilm)*