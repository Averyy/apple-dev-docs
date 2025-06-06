# TableVisualState.OrientedRect3D

**Framework**: TabletopKit  
**Kind**: struct

An object that represents the position and orientation of a 3D rectangle.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct OrientedRect3D
```

## Topics

### Creating 3D rectangle states
- [init()](tablevisualstate/orientedrect3d/init.md)
- [init(pose: Pose3D, size: Size3D)](tablevisualstate/orientedrect3d/init(pose:size:).md)
- [init(rotation: Rotation3D, rect: Rect3D)](tablevisualstate/orientedrect3d/init(rotation:rect:).md)
### Getting 3D rectangle properties
- [var pose: Pose3D](tablevisualstate/orientedrect3d/pose.md)
  The pose of the rectangle.
- [var size: Size3D](tablevisualstate/orientedrect3d/size.md)
  The size of the rectangle.
### Default Implementations
- [Decodable Implementations](tablevisualstate/orientedrect3d/decodable-implementations.md)
- [Encodable Implementations](tablevisualstate/orientedrect3d/encodable-implementations.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func bounds(forEquipment: some Equipment) -> TableVisualState.OrientedRect3D?](tablevisualstate/bounds(forequipment:).md)
- [func bounds(matching: EquipmentIdentifier) -> TableVisualState.OrientedRect3D?](tablevisualstate/bounds(matching:).md)
- [func goalBounds(forEquipment: some Equipment) -> TableVisualState.OrientedRect3D?](tablevisualstate/goalbounds(forequipment:).md)
- [func goalBounds(matching: EquipmentIdentifier) -> TableVisualState.OrientedRect3D?](tablevisualstate/goalbounds(matching:).md)
- [var tableBounds: TableVisualState.OrientedRect3D?](tablevisualstate/tablebounds.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablevisualstate/orientedrect3d)*