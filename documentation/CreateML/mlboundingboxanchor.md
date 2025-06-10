# MLBoundingBoxAnchor

**Framework**: Create ML  
**Kind**: enum

A location within a bounding box that an annotation’s coordinates use as their reference point.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum MLBoundingBoxAnchor
```

## Topics

### Designating anchors
- [MLBoundingBoxAnchor.center](mlboundingboxanchor/center.md)
  An anchor at the bounding box’s center point.
- [MLBoundingBoxAnchor.topLeft](mlboundingboxanchor/topleft.md)
  An anchor at the bounding box’s top-left corner.
- [MLBoundingBoxAnchor.bottomLeft](mlboundingboxanchor/bottomleft.md)
  An anchor at the bounding box’s bottom-left corner.
### Comparing errors
- [static func == (MLBoundingBoxAnchor, MLBoundingBoxAnchor) -> Bool](mlboundingboxanchor/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](mlboundingboxanchor/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Getting the hash value
- [func hash(into: inout Hasher)](mlboundingboxanchor/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](mlboundingboxanchor/hashvalue.md)
  The hash value.
### Default Implementations
- [Equatable Implementations](mlboundingboxanchor/equatable-implementations.md)

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
- [enum MLBoundingBoxCoordinatesOrigin](mlboundingboxcoordinatesorigin.md)
  The location within an image that an annotation’s coordinates use as their origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlboundingboxanchor)*