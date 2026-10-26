# jointLocalTransforms

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The local space transforms for each joint.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```objc
@property (nonatomic, readonly) const simd_float4x4 * jointLocalTransforms;
```

#### Discussion

Local space refers to a joint’s position relative to its parent joint.

## See Also

### Getting a Joint’s Pose
- [jointModelTransforms](./jointmodeltransforms-dno4.md)
  The model space transforms for each joint.
- [- localTransformForJointName:](./localtransformforjointname_.md)
  Returns the local transform for a joint with a given name.
- [- modelTransformForJointName:](./modeltransformforjointname_.md)
  Returns the model transform for a joint with a given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskeleton3d/jointlocaltransforms-1m5a1)*