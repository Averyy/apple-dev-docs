# yawAngle

**Framework**: AVFoundation  
**Kind**: property

The yaw angle of the face specified in degrees.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 14.0+
- macOS 10.10+
- tvOS 9.0+

## Declaration

```swift
var yawAngle: CGFloat { get }
```

#### Discussion

The yaw angle represents the rotation of the face around the vertical axis. A value of `0.0` yields a face that is looking directly at the camera, whereas a yaw angle of `90` degrees yields a face whose eye line is perpendicular to that of the camera.

You must check the value of the [`hasYawAngle`](avmetadatafaceobject/hasyawangle.md) property before accessing this property. If the value in the [`hasYawAngle`](avmetadatafaceobject/hasyawangle.md) property is [`false`](https://developer.apple.com/documentation/Swift/false), reading the value in this property raises an exception.

## See Also

- [var hasRollAngle: Bool](avmetadatafaceobject/hasrollangle.md)
  A Boolean value indicating whether there is a valid roll angle associated with the face.
- [var rollAngle: CGFloat](avmetadatafaceobject/rollangle.md)
  The roll angle of the face specified in degrees.
- [var hasYawAngle: Bool](avmetadatafaceobject/hasyawangle.md)
  A Boolean value indicating whether there is a valid yaw angle associated with the face.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadatafaceobject/yawangle)*