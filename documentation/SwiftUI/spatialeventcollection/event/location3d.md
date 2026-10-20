# location3D

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The 3D location of the touch.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var location3D: Point3D
```

## See Also

### Locating the event
- [var location: CGPoint](./location.md)
  The 2D location of the event.
- [var selectionRay: Ray3D?](./selectionray.md)
  The 3D ray used to target the touch.
- [var inputDevicePose: SpatialEventCollection.Event.InputDevicePose?](./inputdevicepose-swift.property.md)
  The 3D position and orientation of the device controlling the touch, if one exists.
- [SpatialEventCollection.Event.InputDevicePose](./inputdevicepose-swift.struct.md)
  A pose describing the input device like a hand controlling the event.
- [var targetedEntity: Entity?](./targetedentity.md)
  The entity target for this touch, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spatialeventcollection/event/location3d)*