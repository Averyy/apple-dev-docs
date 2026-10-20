# TableVisualState.Point2D

**Framework**: TabletopKit  
**Kind**: struct  
**Role**: Structure

An object that represents a point on the XZ plane.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct Point2D
```

## Topics

### Creating 2D point states
- [init()](./point2d/init%28%29.md)
- [init(projecting: Point3D)](./point2d/init%28projecting%29.md)
  Initializes this point as the projection of the given 3D point on the XZ plane
- [init(x: Double, z: Double)](./point2d/init%28x,z%29.md)
### Getting 2D point properties
- [var x: Double](./point2d/x.md)
- [var z: Double](./point2d/z.md)
- [static let zero: TableVisualState.Point2D](./point2d/zero.md)
### Default Implementations
- [Decodable Implementations](./point2d/decodable-implementations.md)
- [Encodable Implementations](./point2d/encodable-implementations.md)

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
- [TableVisualState.Pose2D](./pose2d.md)
  An object that represents a 2D position and orientation on the XZ plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablevisualstate/point2d)*