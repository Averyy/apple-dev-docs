# localTransform(for:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Returns the local transform for a joint with a given name.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
@nonobjc
func localTransform(for jointName: ARSkeleton.JointName) -> simd_float4x4?
```

## Return Value

The local space transformation matrix for the joint relative to its parent, or `nil` if the joint name is not found.

## Discussion

Local space refers to the joint’s position relative to its parent joint.

## Parameters

- `jointName`: The name of the joint.

## See Also

### Getting a Joint’s Pose
- [var jointLocalTransforms: [simd_float4x4]](./jointlocaltransforms-66gbm.md)
  The local space transforms for each joint.
- [var jointModelTransforms: [simd_float4x4]](./jointmodeltransforms-i6yu.md)
  The model space transforms for each joint.
- [func modelTransform(for: ARSkeleton.JointName) -> simd_float4x4?](./modeltransform%28for%29.md)
  Returns the model transform for a joint with a given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskeleton3d/localtransform(for:))*