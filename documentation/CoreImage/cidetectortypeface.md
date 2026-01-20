# CIDetectorTypeFace

**Framework**: Core Image  
**Kind**: var

A detector that searches for faces in a still image or video, returning [`CIFaceFeature`](cifacefeature.md) objects that provide information about detected faces.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
let CIDetectorTypeFace: String
```

#### Discussion

For better accuracy and performance in face detection, use the [`CIDetectorImageOrientation`](cidetectorimageorientation.md) key to specify the image orientation when using the [`features(in:options:)`](cidetector/features(in:options:).md) method.

## See Also

- [let CIDetectorTypeRectangle: String](cidetectortyperectangle.md)
  A detector that searches for rectangular areas in a still image or video, returning [`CIRectangleFeature`](cirectanglefeature.md) objects that provide information about detected regions.
- [let CIDetectorTypeQRCode: String](cidetectortypeqrcode.md)
  A detector that searches for Quick Response codes (a type of 2D barcode) in a still image or video, returning [`CIQRCodeFeature`](ciqrcodefeature.md) objects that provide information about detected barcodes.
- [let CIDetectorTypeText: String](cidetectortypetext.md)
  A detector that searches for text in a still image or video, returning [`CITextFeature`](citextfeature.md) objects that provide information about detected regions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidetectortypeface)*