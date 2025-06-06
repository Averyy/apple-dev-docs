# translation3D

**Framework**: SwiftUI  
**Kind**: property

The translation of the drag gesture from `startLocation3D` to `location3D`.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var translation3D: Vector3D { get }
```

## See Also

- [var startLocation3D: Point3D](draggesture/value/startlocation3d.md)
  The 3D start location of the drag gesture.
- [var location3D: Point3D](draggesture/value/location3d.md)
  The 3D location of the drag gesture.
- [var predictedEndLocation3D: Point3D](draggesture/value/predictedendlocation3d.md)
  A prediction of where the final location would be if dragging stopped now, based on the current drag velocity.
- [var predictedEndTranslation3D: Vector3D](draggesture/value/predictedendtranslation3d.md)
  A prediction of what the final translation would be if dragging stopped now, based on the current drag velocity.
- [var startInputDevicePose3D: Pose3D?](draggesture/value/startinputdevicepose3d.md)
  The starting 3D pose of the device driving the drag, if one exists.
- [var inputDevicePose3D: Pose3D?](draggesture/value/inputdevicepose3d.md)
  The 3D pose of the device driving the drag, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/draggesture/value/translation3d)*