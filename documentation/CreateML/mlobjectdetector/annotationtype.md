# MLObjectDetector.AnnotationType

**Framework**: Create ML  
**Kind**: enum

The available types of image annotations.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum AnnotationType
```

## Mentions

- [Building an object detector data source](building-an-object-detector-data-source.md)

#### Overview

Use [`MLObjectDetector.AnnotationType`](mlobjectdetector/annotationtype.md) to tell Create ML how to interpret your object annotations.

## Topics

### Bounding box annotations
- [case boundingBox(units: MLBoundingBoxUnits, origin: MLBoundingBoxCoordinatesOrigin, anchor: MLBoundingBoxAnchor)](mlobjectdetector/annotationtype/boundingbox(units:origin:anchor:).md)
  An annotation type that defines a rectangle around an object within an image.
- [enum MLBoundingBoxUnits](mlboundingboxunits.md)
  The units a bounding box annotation uses to define its position and size.
- [enum MLBoundingBoxAnchor](mlboundingboxanchor.md)
  A location within a bounding box that an annotation’s coordinates use as their reference point.
- [enum MLBoundingBoxCoordinatesOrigin](mlboundingboxcoordinatesorigin.md)
  The location within an image that an annotation’s coordinates use as their origin.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [MLObjectDetector.DataSource](mlobjectdetector/datasource.md)
  A data source for an object detector.
- [MLObjectDetector.ModelParameters](mlobjectdetector/modelparameters-swift.struct.md)
  Parameters that affect the process of training an object detection model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/annotationtype)*