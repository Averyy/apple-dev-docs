# transform

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The position and orientation of the camera in world coordinate space.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
var transform: simd_float4x4 { get }
```

```objc
@property (nonatomic, readonly) simd_float4x4 transform;
```

## Mentions

- [Managing Session Life Cycle and Tracking Quality](../managing-session-life-cycle-and-tracking-quality.md)

#### Discussion

World coordinate space in ARKit always follows a right-handed convention, but is oriented based on the session configuration. For details, see [Understanding World Tracking](../understanding-world-tracking.md).

This transform creates a local coordinate space for the camera that is constant with respect to device orientation. In camera space, the x-axis points to the right when the device is in [`UIDeviceOrientation.landscapeLeft`](../../UIKit/uideviceorientation/landscapeleft.md) orientation—that is, the x-axis always points along the long axis of the device, from the front-facing camera toward the Home button. The y-axis points upward (with respect to [`UIDeviceOrientation.landscapeLeft`](../../UIKit/uideviceorientation/landscapeleft.md) orientation), and the z-axis points away from the device on the screen side.

## See Also

### Examining Camera Geometry
- [var eulerAngles: simd_float3](./eulerangles.md)
  The orientation of the camera, expressed as roll, pitch, and yaw values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcamera/transform)*