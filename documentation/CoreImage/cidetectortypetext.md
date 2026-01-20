# CIDetectorTypeText

**Framework**: Core Image  
**Kind**: var

A detector that searches for text in a still image or video, returning [`CITextFeature`](citextfeature.md) objects that provide information about detected regions.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
let CIDetectorTypeText: String
```

#### Discussion

The text detector finds areas that are likely to contain upright text, but does not perform optical character recognition.

## See Also

- [let CIDetectorTypeFace: String](cidetectortypeface.md)
  A detector that searches for faces in a still image or video, returning [`CIFaceFeature`](cifacefeature.md) objects that provide information about detected faces.
- [let CIDetectorTypeRectangle: String](cidetectortyperectangle.md)
  A detector that searches for rectangular areas in a still image or video, returning [`CIRectangleFeature`](cirectanglefeature.md) objects that provide information about detected regions.
- [let CIDetectorTypeQRCode: String](cidetectortypeqrcode.md)
  A detector that searches for Quick Response codes (a type of 2D barcode) in a still image or video, returning [`CIQRCodeFeature`](ciqrcodefeature.md) objects that provide information about detected barcodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidetectortypetext)*