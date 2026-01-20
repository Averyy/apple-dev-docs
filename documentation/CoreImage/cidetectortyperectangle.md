# CIDetectorTypeRectangle

**Framework**: Core Image  
**Kind**: var

A detector that searches for rectangular areas in a still image or video, returning [`CIRectangleFeature`](cirectanglefeature.md) objects that provide information about detected regions.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
let CIDetectorTypeRectangle: String
```

#### Discussion

The rectangle detector finds areas that are likely to represent rectangular objects that appear in perspective in the image, such as papers or books seen on a desktop.

## See Also

- [let CIDetectorTypeFace: String](cidetectortypeface.md)
  A detector that searches for faces in a still image or video, returning [`CIFaceFeature`](cifacefeature.md) objects that provide information about detected faces.
- [let CIDetectorTypeQRCode: String](cidetectortypeqrcode.md)
  A detector that searches for Quick Response codes (a type of 2D barcode) in a still image or video, returning [`CIQRCodeFeature`](ciqrcodefeature.md) objects that provide information about detected barcodes.
- [let CIDetectorTypeText: String](cidetectortypetext.md)
  A detector that searches for text in a still image or video, returning [`CITextFeature`](citextfeature.md) objects that provide information about detected regions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidetectortyperectangle)*