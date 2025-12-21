# hasRollAngle

**Framework**: AVFoundation  
**Kind**: property

A Boolean value indicating whether there is a valid roll angle associated with the face.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 14.0+
- macOS 10.10+
- tvOS 9.0+

## Declaration

```swift
var hasRollAngle: Bool { get }
```

#### Discussion

If the value of this property is [`false`](https://developer.apple.com/documentation/Swift/false), the value in the [`rollAngle`](avmetadatafaceobject/rollangle.md) property is invalid and must not be accessed.

## See Also

- [var rollAngle: CGFloat](avmetadatafaceobject/rollangle.md)
  The roll angle of the face specified in degrees.
- [var hasYawAngle: Bool](avmetadatafaceobject/hasyawangle.md)
  A Boolean value indicating whether there is a valid yaw angle associated with the face.
- [var yawAngle: CGFloat](avmetadatafaceobject/yawangle.md)
  The yaw angle of the face specified in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadatafaceobject/hasrollangle)*