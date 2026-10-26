# modelTransformForJointName:

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Returns the model transform for a joint with a given name.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```objc
- (simd_float4x4) modelTransformForJointName:(ARSkeletonJointName) jointName;
```

#### Discussion

Model space refers to the joint’s position relative to its hip joint. If an invalid joint name is passed in, the returned matrix will be filled with `NaN` values.

## See Also

### Getting a Joint’s Pose
- [jointLocalTransforms](./jointlocaltransforms-1m5a1.md)
  The local space transforms for each joint.
- [jointModelTransforms](./jointmodeltransforms-dno4.md)
  The model space transforms for each joint.
- [- localTransformForJointName:](./localtransformforjointname_.md)
  Returns the local transform for a joint with a given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskeleton3d/modeltransformforjointname:)*