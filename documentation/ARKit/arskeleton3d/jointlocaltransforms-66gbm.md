# jointLocalTransforms

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The local space transforms for each joint.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
@nonobjc
var jointLocalTransforms: [simd_float4x4] { get }
```

## Discussion

Local space refers to a joint’s position relative to its parent joint.

## See Also

### Getting a Joint’s Pose
- [var jointModelTransforms: [simd_float4x4]](./jointmodeltransforms-i6yu.md)
  The model space transforms for each joint.
- [func localTransform(for: ARSkeleton.JointName) -> simd_float4x4?](./localtransform%28for%29.md)
  Returns the local transform for a joint with a given name.
- [func modelTransform(for: ARSkeleton.JointName) -> simd_float4x4?](./modeltransform%28for%29.md)
  Returns the model transform for a joint with a given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskeleton3d/jointlocaltransforms-66gbm)*