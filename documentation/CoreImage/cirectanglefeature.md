# CIRectangleFeature

**Framework**: Core Image  
**Kind**: class

Information about a rectangular region detected in a still or video image.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class CIRectangleFeature
```

#### Overview

> **Note**: In macOS 10.13, iOS 11, and tvOS 11 or later, the Vision framework replaces these classes for identifying and analyzing image features. See [`VNDetectFaceRectanglesRequest`](https://developer.apple.com/documentation/Vision/VNDetectFaceRectanglesRequest))

A detected rectangle feature is not necessarily rectangular in the plane of the image; rather, the feature identifies a shape that may be rectangular in space (for example a book on a desk) but which appears as a four-sided polygon in the image. The properties of a `CIRectangleFeature` object identify its four corners in image coordinates.

You can use rectangle feature detection together with the `CIPerspectiveCorrection` filter to transform the feature to a normal orientation.

To detect rectangles in an image or video, choose [`CIDetectorTypeRectangle`](cidetectortyperectangle.md) when initializing a [`CIDetector`](cidetector.md) object, and use the `CIDetectorAspectRatio` and `CIDetectorFocalLength` options to specify the approximate shape of rectangular features to search for. The detector returns at most one rectangle feature, the most prominent found in the image.

## Topics

### Locating a Detected Feature
- [var bounds: CGRect](cirectanglefeature/bounds-swift.property.md)
  A rectangle indicating the position and extent of the feature in image coordinates.
### Identifying the Corners of a Detected Rectangle
- [var bottomLeft: CGPoint](cirectanglefeature/bottomleft-swift.property.md)
  The lower-left corner of the detected rectangle, in image coordinates.
- [var bottomRight: CGPoint](cirectanglefeature/bottomright-swift.property.md)
  The lower-right corner of the detected rectangle, in image coordinates.
- [var topLeft: CGPoint](cirectanglefeature/topleft-swift.property.md)
  The upper-left corner of the detected rectangle, in image coordinates.
- [var topRight: CGPoint](cirectanglefeature/topright-swift.property.md)
  The upper-right corner of the detected rectangle, in image coordinates.

## Relationships

### Inherits From
- [CIFeature](cifeature.md)
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
- [class CIFeature](cifeature.md)
  The abstract superclass for objects representing notable features detected in an image.
- [class CIFaceFeature](cifacefeature.md)
  Information about a face detected in a still or video image.
- [class CITextFeature](citextfeature.md)
  Information about a text that was detected in a still or video image.
- [class CIQRCodeFeature](ciqrcodefeature.md)
  Information about a Quick Response code detected in a still or video image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirectanglefeature)*