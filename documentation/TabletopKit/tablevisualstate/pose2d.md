# TableVisualState.Pose2D

**Framework**: TabletopKit  
**Kind**: struct

An object that represents a 2D position and orientation on the XZ plane.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct Pose2D
```

## Topics

### Creating 2D pose objects
- [init()](tablevisualstate/pose2d/init.md)
- [init(position: TableVisualState.Point2D, rotation: Angle2D)](tablevisualstate/pose2d/init(position:rotation:).md)
- [init(projecting: Pose3D)](tablevisualstate/pose2d/init(projecting:).md)
  Initializes this pose as the 2D projection of the given pose on the XZ plane
### Getting 2D pose properties
- [var position: TableVisualState.Point2D](tablevisualstate/pose2d/position.md)
- [var rotation: Angle2D](tablevisualstate/pose2d/rotation.md)
### Getting the identifier
- [static var identity: TableVisualState.Pose2D](tablevisualstate/pose2d/identity.md)
  The identity pose
### Default Implementations
- [Decodable Implementations](tablevisualstate/pose2d/decodable-implementations.md)
- [Encodable Implementations](tablevisualstate/pose2d/encodable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [TableVisualState.Point2D](tablevisualstate/point2d.md)
  An object that represents a point on the XZ plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablevisualstate/pose2d)*