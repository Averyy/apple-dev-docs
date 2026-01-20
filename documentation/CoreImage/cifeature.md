# CIFeature

**Framework**: Core Image  
**Kind**: class

The abstract superclass for objects representing notable features detected in an image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class CIFeature
```

#### Overview

> **Note**: In macOS 10.13, iOS 11, and tvOS 11 or later, the Vision framework replaces these classes for identifying and analyzing image features. See [`VNObservation`](https://developer.apple.com/documentation/Vision/VNObservation))

A `CIFeature` object represents a portion of an image that a detector believes matches its criteria. Subclasses of CIFeature holds additional information specific to the detector that discovered the feature.

## Topics

### Feature Properties
- [var bounds: CGRect](cifeature/bounds.md)
  The rectangle that holds discovered feature.
- [var type: String](cifeature/type.md)
  The type of feature that was discovered.
### Feature Types
- [let CIFeatureTypeFace: String](cifeaturetypeface.md)
  A Core Image feature type for person’s face.
- [let CIFeatureTypeRectangle: String](cifeaturetyperectangle.md)
  A Core Image feature type for rectangular object.
- [let CIFeatureTypeQRCode: String](cifeaturetypeqrcode.md)
  A Core Image feature type for QR code object.
- [let CIFeatureTypeText: String](cifeaturetypetext.md)
  A Core Image feature type for text.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [CIFaceFeature](cifacefeature.md)
- [CIQRCodeFeature](ciqrcodefeature.md)
- [CIRectangleFeature](cirectanglefeature.md)
- [CITextFeature](citextfeature.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CIDetector](cidetector.md)
  An image processor that identifies notable features, such as faces and barcodes, in a still image or video.
- [class CIFaceFeature](cifacefeature.md)
  Information about a face detected in a still or video image.
- [class CIRectangleFeature](cirectanglefeature.md)
  Information about a rectangular region detected in a still or video image.
- [class CITextFeature](citextfeature.md)
  Information about a text that was detected in a still or video image.
- [class CIQRCodeFeature](ciqrcodefeature.md)
  Information about a Quick Response code detected in a still or video image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifeature)*