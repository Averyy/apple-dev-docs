# location

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The 2D location of the event.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
var location: CGPoint
```

## See Also

### Locating the event
- [var location3D: Point3D](./location3d.md)
  The 3D location of the touch.
- [var selectionRay: Ray3D?](./selectionray.md)
  The 3D ray used to target the touch.
- [var inputDevicePose: SpatialEventCollection.Event.InputDevicePose?](./inputdevicepose-swift.property.md)
  The 3D position and orientation of the device controlling the touch, if one exists.
- [SpatialEventCollection.Event.InputDevicePose](./inputdevicepose-swift.struct.md)
  A pose describing the input device like a hand controlling the event.
- [var targetedEntity: Entity?](./targetedentity.md)
  The entity target for this touch, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/spatialeventcollection/event/location)*