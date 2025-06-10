# DragGesture.Value

**Framework**: SwiftUI  
**Kind**: struct

The attributes of a drag gesture.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct Value
```

## Topics

### Getting 2D position
- [var startLocation: CGPoint](draggesture/value/startlocation.md)
  The location of the drag gesture’s first event.
- [var location: CGPoint](draggesture/value/location.md)
  The location of the drag gesture’s current event.
- [var predictedEndLocation: CGPoint](draggesture/value/predictedendlocation.md)
  A prediction, based on the current drag velocity, of where the final location will be if dragging stopped now.
- [var translation: CGSize](draggesture/value/translation.md)
  The total translation from the start of the drag gesture to the current event of the drag gesture.
- [var predictedEndTranslation: CGSize](draggesture/value/predictedendtranslation.md)
  A prediction, based on the current drag velocity, of what the final translation will be if dragging stopped now.
### Getting 3D position
- [var startLocation3D: Point3D](draggesture/value/startlocation3d.md)
  The 3D start location of the drag gesture.
- [var location3D: Point3D](draggesture/value/location3d.md)
  The 3D location of the drag gesture.
- [var predictedEndLocation3D: Point3D](draggesture/value/predictedendlocation3d.md)
  A prediction of where the final location would be if dragging stopped now, based on the current drag velocity.
- [var translation3D: Vector3D](draggesture/value/translation3d.md)
  The translation of the drag gesture from `startLocation3D` to `location3D`.
- [var predictedEndTranslation3D: Vector3D](draggesture/value/predictedendtranslation3d.md)
  A prediction of what the final translation would be if dragging stopped now, based on the current drag velocity.
- [var startInputDevicePose3D: Pose3D?](draggesture/value/startinputdevicepose3d.md)
  The starting 3D pose of the device driving the drag, if one exists.
- [var inputDevicePose3D: Pose3D?](draggesture/value/inputdevicepose3d.md)
  The 3D pose of the device driving the drag, if one exists.
### Handling changes over time
- [var time: Date](draggesture/value/time.md)
  The time associated with the drag gesture’s current event.
- [var velocity: CGSize](draggesture/value/velocity.md)
  The current drag velocity.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/draggesture/value)*