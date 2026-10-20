# CIDetectorTypeQRCode

**Framework**: Core Image  
**Kind**: var  
**Role**: Global Variable

A detector that searches for Quick Response codes (a type of 2D barcode) in a still image or video, returning [`CIQRCodeFeature`](./ciqrcodefeature.md) objects that provide information about detected barcodes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+

## Declaration

```swift
let CIDetectorTypeQRCode: String
```

```c
extern NSString * const CIDetectorTypeQRCode;
```

## See Also

### Constants
- [let CIDetectorTypeFace: String](./cidetectortypeface.md)
  A detector that searches for faces in a still image or video, returning [`CIFaceFeature`](./cifacefeature.md) objects that provide information about detected faces.
- [let CIDetectorTypeRectangle: String](./cidetectortyperectangle.md)
  A detector that searches for rectangular areas in a still image or video, returning [`CIRectangleFeature`](./cirectanglefeature.md) objects that provide information about detected regions.
- [let CIDetectorTypeText: String](./cidetectortypetext.md)
  A detector that searches for text in a still image or video, returning [`CITextFeature`](./citextfeature.md) objects that provide information about detected regions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidetectortypeqrcode)*