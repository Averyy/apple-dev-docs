# MLBoundingBoxCoordinatesOrigin

**Framework**: Create ML  
**Kind**: enum

The location within an image that an annotation’s coordinates use as their origin.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum MLBoundingBoxCoordinatesOrigin
```

## Topics

### Designating origins
- [MLBoundingBoxCoordinatesOrigin.topLeft](mlboundingboxcoordinatesorigin/topleft.md)
  An origin at the image’s top-left corner.
- [MLBoundingBoxCoordinatesOrigin.bottomLeft](mlboundingboxcoordinatesorigin/bottomleft.md)
  An origin at the image’s bottom-left corner.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case boundingBox(units: MLBoundingBoxUnits, origin: MLBoundingBoxCoordinatesOrigin, anchor: MLBoundingBoxAnchor)](mlobjectdetector/annotationtype/boundingbox(units:origin:anchor:).md)
  An annotation type that defines a rectangle around an object within an image.
- [enum MLBoundingBoxUnits](mlboundingboxunits.md)
  The units a bounding box annotation uses to define its position and size.
- [enum MLBoundingBoxAnchor](mlboundingboxanchor.md)
  A location within a bounding box that an annotation’s coordinates use as their reference point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlboundingboxcoordinatesorigin)*