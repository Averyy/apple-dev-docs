# jointModelTransforms

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The model space transforms for each joint.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```objc
@property (nonatomic, readonly) const simd_float4x4 * jointModelTransforms;
```

## Discussion

Model space refers to a joint’s position relative to the hip joint. Note, the hip joint is located at the body anchor’s origin.

## See Also

### Getting a Joint’s Pose
- [jointLocalTransforms](./jointlocaltransforms-1m5a1.md)
  The local space transforms for each joint.
- [- localTransformForJointName:](./localtransformforjointname_.md)
  Returns the local transform for a joint with a given name.
- [- modelTransformForJointName:](./modeltransformforjointname_.md)
  Returns the model transform for a joint with a given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskeleton3d/jointmodeltransforms-dno4)*