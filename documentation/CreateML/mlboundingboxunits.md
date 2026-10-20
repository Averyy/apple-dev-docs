# MLBoundingBoxUnits

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

The units a bounding box annotation uses to define its position and size.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum MLBoundingBoxUnits
```

#### Overview

All bounding box annotations in an annotation file must use the same units for their coordinates and size. See [`MLObjectDetector.AnnotationType.boundingBox(units:origin:anchor:)`](./mlobjectdetector/annotationtype/boundingbox%28units,origin,anchor%29.md).

## Topics

### Designating units
- [MLBoundingBoxUnits.pixel](./mlboundingboxunits/pixel.md)
  A unit of measurement in pixels for an image.
- [MLBoundingBoxUnits.normalized](./mlboundingboxunits/normalized.md)
  A unit of measurement as a portion of an image’s overall width or height.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Bounding box annotations
- [case boundingBox(units: MLBoundingBoxUnits, origin: MLBoundingBoxCoordinatesOrigin, anchor: MLBoundingBoxAnchor)](./mlobjectdetector/annotationtype/boundingbox%28units,origin,anchor%29.md)
  An annotation type that defines a rectangle around an object within an image.
- [enum MLBoundingBoxAnchor](./mlboundingboxanchor.md)
  A location within a bounding box that an annotation’s coordinates use as their reference point.
- [enum MLBoundingBoxCoordinatesOrigin](./mlboundingboxcoordinatesorigin.md)
  The location within an image that an annotation’s coordinates use as their origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlboundingboxunits)*