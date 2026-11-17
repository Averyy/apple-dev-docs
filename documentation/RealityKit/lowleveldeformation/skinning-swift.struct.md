# LowLevelDeformation.Skinning

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An accessor for the skinning buffers of a [`LowLevelDeformation`](../lowleveldeformation.md).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Skinning
```

## Topics

### Configuring skinning data
- [func setJointTransforms(any MTLBuffer, offset: Int) throws](./skinning-swift.struct/setjointtransforms%28_,offset%29.md)
  Sets the buffer containing joint transform matrices.
- [func setInfluenceWeights(any MTLBuffer, offset: Int) throws](./skinning-swift.struct/setinfluenceweights%28_,offset%29.md)
  Sets the buffer containing per-vertex influence weights.
- [func setInverseBindPoses(any MTLBuffer, offset: Int) throws](./skinning-swift.struct/setinversebindposes%28_,offset%29.md)
  Sets the buffer containing inverse bind-pose matrices.
- [func replaceInfluenceJointIndices<R>((inout MutableRawSpan) -> R) throws -> R](./skinning-swift.struct/replaceinfluencejointindices%28_%29.md)
  Fills the influence joint index buffer using the given closure.    /// After the closure returns, the framework validates every index. An out-of-range index causes a throw.
### Instance Properties
- [var geometryBindTransform: simd_float4x4](./skinning-swift.struct/geometrybindtransform.md)
  The geometry bind transform applied to vertex positions before the joint skinning math.

## See Also

### Configuring deformation stages
- [var skinning: LowLevelDeformation.Skinning](./skinning-swift.property.md)
  The skinning data accessors for this deformation.
- [var blendShape: LowLevelDeformation.BlendShape](./blendshape-swift.property.md)
  The blend-shape data accessors for this deformation.
- [LowLevelDeformation.BlendShape](./blendshape-swift.struct.md)
  An accessor for the blend-shape buffers of a [`LowLevelDeformation`](../lowleveldeformation.md).
- [var renormalization: LowLevelDeformation.Renormalization](./renormalization-swift.property.md)
  The renormalization data accessors for this deformation.
- [LowLevelDeformation.Renormalization](./renormalization-swift.struct.md)
  An accessor for the renormalization buffers of a [`LowLevelDeformation`](../lowleveldeformation.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/skinning-swift.struct)*