# LowLevelDeformation.Blending

**Framework**: RealityKit  
**Kind**: struct

An accessor for the blend-shape buffers of a [`LowLevelDeformation`](lowleveldeformation.md).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Blending
```

## Topics

### Setting blend data
- [func setPositionOffsets(any MTLBuffer, offset: Int) throws(LowLevelDeformation.Error)](lowleveldeformation/blending-swift.struct/setpositionoffsets(_:offset:).md)
  Sets the buffer containing blend-shape position offsets.
- [func setNormalOffsets(any MTLBuffer, offset: Int) throws(LowLevelDeformation.Error)](lowleveldeformation/blending-swift.struct/setnormaloffsets(_:offset:).md)
  Sets the buffer containing blend-shape normal offsets.
- [func setTangentOffsets(any MTLBuffer, offset: Int) throws(LowLevelDeformation.Error)](lowleveldeformation/blending-swift.struct/settangentoffsets(_:offset:).md)
  Sets the buffer containing blend-shape tangent offsets.
- [func setWeights(any MTLBuffer, offset: Int) throws(LowLevelDeformation.Error)](lowleveldeformation/blending-swift.struct/setweights(_:offset:).md)
  Sets the buffer containing blend-shape weights.

## See Also

- [var skinning: LowLevelDeformation.Skinning](lowleveldeformation/skinning-swift.property.md)
  The skinning data accessors for this deformation.
- [LowLevelDeformation.Skinning](lowleveldeformation/skinning-swift.struct.md)
  An accessor for the skinning buffers of a [`LowLevelDeformation`](lowleveldeformation.md).
- [var blending: LowLevelDeformation.Blending](lowleveldeformation/blending-swift.property.md)
  The blend-shape data accessors for this deformation.
- [var renormalizing: LowLevelDeformation.Renormalizing](lowleveldeformation/renormalizing-swift.property.md)
  The renormalization data accessors for this deformation.
- [LowLevelDeformation.Renormalizing](lowleveldeformation/renormalizing-swift.struct.md)
  An accessor for the renormalization buffers of a [`LowLevelDeformation`](lowleveldeformation.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/blending-swift.struct)*