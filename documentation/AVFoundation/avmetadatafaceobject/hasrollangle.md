# hasRollAngle

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) BOOL hasRollAngle;
```

#### Discussion

If the value of this property is [`false`](../../Swift/false.md), the value in the [`rollAngle`](./rollangle.md) property is invalid and must not be accessed.

## See Also

### Accessing the face detection data
- [var rollAngle: CGFloat](./rollangle.md)
  The roll angle of the face specified in degrees.
- [var hasYawAngle: Bool](./hasyawangle.md)
  A Boolean value indicating whether there is a valid yaw angle associated with the face.
- [var yawAngle: CGFloat](./yawangle.md)
  The yaw angle of the face specified in degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadatafaceobject/hasrollangle)*