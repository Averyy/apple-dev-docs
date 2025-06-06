# inputDevicePose

**Framework**: SwiftUI  
**Kind**: property

The 3D position and orientation of the device controlling the touch, if one exists.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 1.0+

## Declaration

```swift
var inputDevicePose: SpatialEventCollection.Event.InputDevicePose? { get set }
```

## See Also

- [var location: CGPoint](spatialeventcollection/event/location.md)
  The 2D location of the event.
- [var location3D: Point3D](spatialeventcollection/event/location3d.md)
  The 3D location of the touch.
- [var selectionRay: Ray3D?](spatialeventcollection/event/selectionray.md)
  The 3D ray used to target the touch.
- [SpatialEventCollection.Event.InputDevicePose](spatialeventcollection/event/inputdevicepose-swift.struct.md)
  A pose describing the input device like a hand controlling the event.
- [var targetedEntity: Entity?](spatialeventcollection/event/targetedentity.md)
  The entity target for this touch, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spatialeventcollection/event/inputdevicepose-swift.property)*