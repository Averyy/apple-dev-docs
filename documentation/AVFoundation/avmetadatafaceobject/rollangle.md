# rollAngle

**Framework**: AVFoundation  
**Kind**: property

The roll angle of the face specified in degrees.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 14.0+
- macOS 10.10+
- tvOS 9.0+

## Declaration

```swift
var rollAngle: CGFloat { get }
```

#### Discussion

The roll angle represents the side-to-side tilt of the face relative to the metadata’s bounding rectangle. A value of `0.0` yields a face that is level relative to the picture, whereas a value of `90` yields a face that is perpendicular relative to the picture.

You must check the value of the [`hasRollAngle`](avmetadatafaceobject/hasrollangle.md) property before accessing this property. If the value in the [`hasRollAngle`](avmetadatafaceobject/hasrollangle.md) property is [`false`](https://developer.apple.com/documentation/Swift/false), reading the value in this property raises an exception.

## See Also

- [var hasRollAngle: Bool](avmetadatafaceobject/hasrollangle.md)
  A Boolean value indicating whether there is a valid roll angle associated with the face.
- [var hasYawAngle: Bool](avmetadatafaceobject/hasyawangle.md)
  A Boolean value indicating whether there is a valid yaw angle associated with the face.
- [var yawAngle: CGFloat](avmetadatafaceobject/yawangle.md)
  The yaw angle of the face specified in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadatafaceobject/rollangle)*