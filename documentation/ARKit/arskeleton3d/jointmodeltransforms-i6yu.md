# jointModelTransforms

**Framework**: ARKit  
**Kind**: property

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

- [var jointLocalTransforms: [simd_float4x4]](arskeleton3d/jointlocaltransforms-66gbm.md)
  The local space transforms for each joint.
- [func localTransform(for: ARSkeleton.JointName) -> simd_float4x4?](arskeleton3d/localtransform(for:).md)
  Returns the local transform for a joint with a given name.
- [func modelTransform(for: ARSkeleton.JointName) -> simd_float4x4?](arskeleton3d/modeltransform(for:).md)
  Returns the model transform for a joint with a given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskeleton3d/jointmodeltransforms-i6yu)*