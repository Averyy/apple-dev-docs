# localTransformForJointName:

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Returns the local transform for a joint with a given name.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```objc
- (simd_float4x4) localTransformForJointName:(ARSkeletonJointName) jointName;
```

## Discussion

Local space refers to the joints position relative to its parent joint. If an invalid joint name is passed the returned matrix will be filled with `NaN` values.

## See Also

### Getting a Joint’s Pose
- [jointLocalTransforms](./jointlocaltransforms-1m5a1.md)
  The local space transforms for each joint.
- [jointModelTransforms](./jointmodeltransforms-dno4.md)
  The model space transforms for each joint.
- [- modelTransformForJointName:](./modeltransformforjointname_.md)
  Returns the model transform for a joint with a given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskeleton3d/localtransformforjointname:)*