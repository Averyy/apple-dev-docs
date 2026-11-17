# eulerAngles

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The orientation of the camera, expressed as roll, pitch, and yaw values.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
var eulerAngles: simd_float3 { get }
```

```objc
@property (nonatomic, readonly) simd_float3 eulerAngles;
```

## Discussion

The order of components in this vector matches the axes of rotation:

1. Pitch (the x component) is the rotation about the node’s x-axis (in radians)
2. Yaw   (the y component) is the rotation about the node’s y-axis (in radians)
3. Roll  (the z component) is the rotation about the node’s z-axis (in radians) ARKit applies these rotations in the following order:
4. first roll
5. then pitch
6. then yaw

## See Also

### Examining Camera Geometry
- [var transform: simd_float4x4](./transform.md)
  The position and orientation of the camera in world coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arcamera/eulerangles)*