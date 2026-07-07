# windForce

**Framework**: RealityKit  
**Kind**: property

The wind force applied to particles inside the volume.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var windForce: SIMD3<Float>
```

#### Discussion

This force depends on the angle between the force direction and the face normals of the cloth body. Full force is applied when the force direction is perpendicular to the face (aligned with the normal), and no force is applied when the force direction is parallel to the face.

## See Also

- [var constantForce: SIMD3<Float>](clothforcevolumecomponent/constantforce.md)
  The constant force applied to particles inside the volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothforcevolumecomponent/windforce)*