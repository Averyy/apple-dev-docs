# transform

**Framework**: ARKit  
**Kind**: property

The position and orientation of the camera in world coordinate space.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var transform: simd_float4x4 { get }
```

## Mentions

- [Managing Session Life Cycle and Tracking Quality](managing-session-life-cycle-and-tracking-quality.md)

#### Discussion

World coordinate space in ARKit always follows a right-handed convention, but is oriented based on the session configuration. For details, see [`Understanding World Tracking`](understanding-world-tracking.md).

This transform creates a local coordinate space for the camera that is constant with respect to device orientation. In camera space, the x-axis points to the right when the device is in [`UIDeviceOrientation.landscapeLeft`](https://developer.apple.com/documentation/UIKit/UIDeviceOrientation/landscapeLeft) orientation—that is, the x-axis always points along the long axis of the device, from the front-facing camera toward the Home button. The y-axis points upward (with respect to [`UIDeviceOrientation.landscapeLeft`](https://developer.apple.com/documentation/UIKit/UIDeviceOrientation/landscapeLeft) orientation), and the z-axis points away from the device on the screen side.

## See Also

- [var eulerAngles: simd_float3](arcamera/eulerangles.md)
  The orientation of the camera, expressed as roll, pitch, and yaw values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcamera/transform)*