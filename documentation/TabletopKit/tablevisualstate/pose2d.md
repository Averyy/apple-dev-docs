# TableVisualState.Pose2D

**Framework**: TabletopKit  
**Kind**: struct  
**Role**: Structure

An object that represents a 2D position and orientation on the XZ plane.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct Pose2D
```

## Topics

### Creating 2D pose objects
- [init()](./pose2d/init%28%29.md)
- [init(position: TableVisualState.Point2D, rotation: Angle2D)](./pose2d/init%28position,rotation%29.md)
- [init(projecting: Pose3D)](./pose2d/init%28projecting%29.md)
  Initializes this pose as the 2D projection of the given pose on the XZ plane
### Getting 2D pose properties
- [var position: TableVisualState.Point2D](./pose2d/position.md)
- [var rotation: Angle2D](./pose2d/rotation.md)
### Getting the identifier
- [static var identity: TableVisualState.Pose2D](./pose2d/identity.md)
  The identity pose
### Default Implementations
- [Decodable Implementations](./pose2d/decodable-implementations.md)
- [Encodable Implementations](./pose2d/encodable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Representing 2D states
- [TableVisualState.Point2D](./point2d.md)
  An object that represents a point on the XZ plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablevisualstate/pose2d)*