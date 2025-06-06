# SpatialEventCollection.Event.InputDevicePose

**Framework**: SwiftUI  
**Kind**: struct

A pose describing the input device like a hand controlling the event.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
struct InputDevicePose
```

## Topics

### Getting the event type
- [var altitude: Angle](spatialeventcollection/event/inputdevicepose-swift.struct/altitude.md)
  The altitude angle.
- [var azimuth: Angle](spatialeventcollection/event/inputdevicepose-swift.struct/azimuth.md)
  The azimuth angle.
- [var pose3D: Pose3D](spatialeventcollection/event/inputdevicepose-swift.struct/pose3d.md)
  The 3D pose of the input device.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var location: CGPoint](spatialeventcollection/event/location.md)
  The 2D location of the event.
- [var location3D: Point3D](spatialeventcollection/event/location3d.md)
  The 3D location of the touch.
- [var selectionRay: Ray3D?](spatialeventcollection/event/selectionray.md)
  The 3D ray used to target the touch.
- [var inputDevicePose: SpatialEventCollection.Event.InputDevicePose?](spatialeventcollection/event/inputdevicepose-swift.property.md)
  The 3D position and orientation of the device controlling the touch, if one exists.
- [var targetedEntity: Entity?](spatialeventcollection/event/targetedentity.md)
  The entity target for this touch, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spatialeventcollection/event/inputdevicepose-swift.struct)*