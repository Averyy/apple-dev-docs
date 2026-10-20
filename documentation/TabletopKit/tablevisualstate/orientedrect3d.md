# TableVisualState.OrientedRect3D

**Framework**: TabletopKit  
**Kind**: struct  
**Role**: Structure

An object that represents the position and orientation of a 3D rectangle.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct OrientedRect3D
```

## Topics

### Creating 3D rectangle states
- [init()](./orientedrect3d/init%28%29.md)
- [init(pose: Pose3D, size: Size3D)](./orientedrect3d/init%28pose,size%29.md)
- [init(rotation: Rotation3D, rect: Rect3D)](./orientedrect3d/init%28rotation,rect%29.md)
### Getting 3D rectangle properties
- [var pose: Pose3D](./orientedrect3d/pose.md)
  The pose of the rectangle.
- [var size: Size3D](./orientedrect3d/size.md)
  The size of the rectangle.
### Default Implementations
- [Decodable Implementations](./orientedrect3d/decodable-implementations.md)
- [Encodable Implementations](./orientedrect3d/encodable-implementations.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Representing 3D states
- [func bounds(for: some Equipment) -> TableVisualState.OrientedRect3D?](./bounds%28for%29.md)
  Returns the current pose and extents of the bounding box for the given equipment. Returns `nil` if the equipment is not part of the game.
- [func bounds(forEquipment: some Equipment) -> TableVisualState.OrientedRect3D?](./bounds%28forequipment%29.md)
- [func bounds(matching: EquipmentIdentifier) -> TableVisualState.OrientedRect3D?](./bounds%28matching%29.md)
- [func goalBounds(forEquipment: some Equipment) -> TableVisualState.OrientedRect3D?](./goalbounds%28forequipment%29.md)
- [func goalBounds(matching: EquipmentIdentifier) -> TableVisualState.OrientedRect3D?](./goalbounds%28matching%29.md)
- [var tableBounds: TableVisualState.OrientedRect3D?](./tablebounds.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablevisualstate/orientedrect3d)*