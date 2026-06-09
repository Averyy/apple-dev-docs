# LowLevelDeformation.Skinning

**Framework**: RealityKit  
**Kind**: struct

An accessor for the skinning buffers of a [`LowLevelDeformation`](lowleveldeformation.md).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Skinning
```

## Topics

### Configuring skinning data
- [func setJointTransforms(any MTLBuffer, offset: Int) throws(LowLevelDeformation.Error)](lowleveldeformation/skinning-swift.struct/setjointtransforms(_:offset:).md)
  Sets the buffer containing joint transform matrices.
- [func setInfluenceWeights(any MTLBuffer, offset: Int) throws(LowLevelDeformation.Error)](lowleveldeformation/skinning-swift.struct/setinfluenceweights(_:offset:).md)
  Sets the buffer containing per-vertex influence weights.
- [func setInverseBindPoses(any MTLBuffer, offset: Int) throws(LowLevelDeformation.Error)](lowleveldeformation/skinning-swift.struct/setinversebindposes(_:offset:).md)
  Sets the buffer containing inverse bind-pose matrices.
- [func replaceInfluenceJointIndices<R>((inout MutableRawSpan) -> R) throws(LowLevelDeformation.Error) -> R](lowleveldeformation/skinning-swift.struct/replaceinfluencejointindices(_:).md)
  Fills the influence joint index buffer using the given closure.

## See Also

- [var skinning: LowLevelDeformation.Skinning](lowleveldeformation/skinning-swift.property.md)
  The skinning data accessors for this deformation.
- [var blending: LowLevelDeformation.Blending](lowleveldeformation/blending-swift.property.md)
  The blend-shape data accessors for this deformation.
- [LowLevelDeformation.Blending](lowleveldeformation/blending-swift.struct.md)
  An accessor for the blend-shape buffers of a [`LowLevelDeformation`](lowleveldeformation.md).
- [var renormalizing: LowLevelDeformation.Renormalizing](lowleveldeformation/renormalizing-swift.property.md)
  The renormalization data accessors for this deformation.
- [LowLevelDeformation.Renormalizing](lowleveldeformation/renormalizing-swift.struct.md)
  An accessor for the renormalization buffers of a [`LowLevelDeformation`](lowleveldeformation.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/skinning-swift.struct)*