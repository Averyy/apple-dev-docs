# LowLevelDeformation.BlendShape

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An accessor for the blend-shape buffers of a [`LowLevelDeformation`](../lowleveldeformation.md).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct BlendShape
```

## Topics

### Setting blend data
- [func setPositionOffsets(any MTLBuffer, offset: Int) throws](./blendshape-swift.struct/setpositionoffsets%28_,offset%29.md)
  Sets the buffer containing blend-shape position offsets.
- [func setNormalOffsets(any MTLBuffer, offset: Int) throws](./blendshape-swift.struct/setnormaloffsets%28_,offset%29.md)
  Sets the buffer containing blend-shape normal offsets.
- [func setTangentOffsets(any MTLBuffer, offset: Int) throws](./blendshape-swift.struct/settangentoffsets%28_,offset%29.md)
  Sets the buffer containing blend-shape tangent offsets.
- [func setWeights(any MTLBuffer, offset: Int) throws](./blendshape-swift.struct/setweights%28_,offset%29.md)
  Sets the buffer containing blend-shape weights.

## See Also

### Configuring deformation stages
- [var skinning: LowLevelDeformation.Skinning](./skinning-swift.property.md)
  The skinning data accessors for this deformation.
- [LowLevelDeformation.Skinning](./skinning-swift.struct.md)
  An accessor for the skinning buffers of a [`LowLevelDeformation`](../lowleveldeformation.md).
- [var blendShape: LowLevelDeformation.BlendShape](./blendshape-swift.property.md)
  The blend-shape data accessors for this deformation.
- [var renormalization: LowLevelDeformation.Renormalization](./renormalization-swift.property.md)
  The renormalization data accessors for this deformation.
- [LowLevelDeformation.Renormalization](./renormalization-swift.struct.md)
  An accessor for the renormalization buffers of a [`LowLevelDeformation`](../lowleveldeformation.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/blendshape-swift.struct)*