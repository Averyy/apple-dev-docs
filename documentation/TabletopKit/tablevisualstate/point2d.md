# TableVisualState.Point2D

**Framework**: TabletopKit  
**Kind**: struct

An object that represents a point on the XZ plane.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct Point2D
```

## Topics

### Creating 2D point states
- [init()](tablevisualstate/point2d/init.md)
- [init(projecting: Point3D)](tablevisualstate/point2d/init(projecting:).md)
  Initializes this point as the projection of the given 3D point on the XZ plane
- [init(x: Double, z: Double)](tablevisualstate/point2d/init(x:z:).md)
### Getting 2D point properties
- [var x: Double](tablevisualstate/point2d/x.md)
- [var z: Double](tablevisualstate/point2d/z.md)
- [static let zero: TableVisualState.Point2D](tablevisualstate/point2d/zero.md)
### Default Implementations
- [Decodable Implementations](tablevisualstate/point2d/decodable-implementations.md)
- [Encodable Implementations](tablevisualstate/point2d/encodable-implementations.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [TableVisualState.Pose2D](tablevisualstate/pose2d.md)
  An object that represents a 2D position and orientation on the XZ plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablevisualstate/point2d)*