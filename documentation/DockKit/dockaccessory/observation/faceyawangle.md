# faceYawAngle

**Framework**: DockKit  
**Kind**: property

The angle of the face in radians.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
let faceYawAngle: Measurement<UnitAngle>?
```

#### Discussion

A value of `0` indicates the face of the subject in the frame is looking directly at the camera. A negative value indicates the subject’s face is oriented to the left, while positive value indicates the face is oriented to the right.

## See Also

- [let rect: CGRect](dockaccessory/observation/rect.md)
  The coordinates of the subject in the frame.
- [let type: DockAccessory.Observation.ObservationType](dockaccessory/observation/type.md)
  The type of subject in the frame.
- [let identifier: Int](dockaccessory/observation/identifier.md)
  A unique identifier representing the subject in the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dockkit/dockaccessory/observation/faceyawangle)*