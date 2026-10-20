# inputDevicePose

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The 3D position and orientation of the device controlling the touch, if one exists.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var inputDevicePose: SpatialEventCollection.Event.InputDevicePose? { get set }
```

## See Also

### Locating the event
- [var location: CGPoint](./location.md)
  The 2D location of the event.
- [var location3D: Point3D](./location3d.md)
  The 3D location of the touch.
- [var selectionRay: Ray3D?](./selectionray.md)
  The 3D ray used to target the touch.
- [SpatialEventCollection.Event.InputDevicePose](./inputdevicepose-swift.struct.md)
  A pose describing the input device like a hand controlling the event.
- [var targetedEntity: Entity?](./targetedentity.md)
  The entity target for this touch, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spatialeventcollection/event/inputdevicepose-swift.property)*