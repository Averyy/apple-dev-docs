# modelTransform(for:)

**Framework**: ARKit  
**Kind**: method

Returns the model transform for a joint with a given name.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
@nonobjc
func modelTransform(for jointName: ARSkeleton.JointName) -> simd_float4x4?
```

#### Discussion

Model space refers to the joint’s position relative to its hip joint. If an invalid joint name is passed in, the returned matrix will be filled with `NaN` values.

## See Also

- [var jointLocalTransforms: [simd_float4x4]](arskeleton3d/jointlocaltransforms-66gbm.md)
  The local space transforms for each joint.
- [var jointModelTransforms: [simd_float4x4]](arskeleton3d/jointmodeltransforms-i6yu.md)
  The model space transforms for each joint.
- [func localTransform(for: ARSkeleton.JointName) -> simd_float4x4?](arskeleton3d/localtransform(for:).md)
  Returns the local transform for a joint with a given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskeleton3d/modeltransform(for:))*