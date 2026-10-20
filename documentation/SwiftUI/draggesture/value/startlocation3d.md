# startLocation3D

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The 3D start location of the drag gesture.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var startLocation3D: Point3D { get }
```

## See Also

### Getting 3D position
- [var location3D: Point3D](./location3d.md)
  The 3D location of the drag gesture.
- [var predictedEndLocation3D: Point3D](./predictedendlocation3d.md)
  A prediction of where the final location would be if dragging stopped now, based on the current drag velocity.
- [var translation3D: Vector3D](./translation3d.md)
  The translation of the drag gesture from `startLocation3D` to `location3D`.
- [var predictedEndTranslation3D: Vector3D](./predictedendtranslation3d.md)
  A prediction of what the final translation would be if dragging stopped now, based on the current drag velocity.
- [var startInputDevicePose3D: Pose3D?](./startinputdevicepose3d.md)
  The starting 3D pose of the device driving the drag, if one exists.
- [var inputDevicePose3D: Pose3D?](./inputdevicepose3d.md)
  The 3D pose of the device driving the drag, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/draggesture/value/startlocation3d)*