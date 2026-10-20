# jointModelTransforms

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The model space transforms for each joint.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
@nonobjc
var jointModelTransforms: [simd_float4x4] { get }
```

#### Discussion

Model space refers to a joint’s position relative to the hip joint. Note, the hip joint is located at the body anchor’s origin.

## See Also

### Getting a Joint’s Pose
- [var jointLocalTransforms: [simd_float4x4]](./jointlocaltransforms-66gbm.md)
  The local space transforms for each joint.
- [func localTransform(for: ARSkeleton.JointName) -> simd_float4x4?](./localtransform%28for%29.md)
  Returns the local transform for a joint with a given name.
- [func modelTransform(for: ARSkeleton.JointName) -> simd_float4x4?](./modeltransform%28for%29.md)
  Returns the model transform for a joint with a given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskeleton3d/jointmodeltransforms-i6yu)*