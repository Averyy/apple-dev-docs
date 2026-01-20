# Detector Types

**Framework**: Core Image

Strings used to declare the detector for which you are interested.

## Topics

### Constants
- [let CIDetectorTypeFace: String](cidetectortypeface.md)
  A detector that searches for faces in a still image or video, returning [`CIFaceFeature`](cifacefeature.md) objects that provide information about detected faces.
- [let CIDetectorTypeRectangle: String](cidetectortyperectangle.md)
  A detector that searches for rectangular areas in a still image or video, returning [`CIRectangleFeature`](cirectanglefeature.md) objects that provide information about detected regions.
- [let CIDetectorTypeQRCode: String](cidetectortypeqrcode.md)
  A detector that searches for Quick Response codes (a type of 2D barcode) in a still image or video, returning [`CIQRCodeFeature`](ciqrcodefeature.md) objects that provide information about detected barcodes.
- [let CIDetectorTypeText: String](cidetectortypetext.md)
  A detector that searches for text in a still image or video, returning [`CITextFeature`](citextfeature.md) objects that provide information about detected regions.

## See Also

- [Detector Configuration Keys](detector-configuration-keys.md)
  Keys used in the options dictionary to configure a detector.
- [Detector Accuracy Options](detector-accuracy-options.md)
  Value options used to specify the desired accuracy of the detector.
- [Feature Detection Keys](feature-detection-keys.md)
  Keys used in the options dictionary for [`features(in:options:)`](cidetector/features(in:options:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/detector-types)*