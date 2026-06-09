# setJointTransforms(_:offset:)

**Framework**: RealityKit  
**Kind**: method

Sets the buffer containing joint transform matrices.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func setJointTransforms(_ buffer: any MTLBuffer, offset: Int) throws(LowLevelDeformation.Error)
```

#### Discussion

The buffer must contain `jointTransformCount` float4x4 matrices.

> **Note**: If `offset` is out of bounds for `buffer`, or if the buffer is too small.

## Parameters

- `buffer`: The Metal buffer containing the joint transform matrices.
- `offset`: The byte offset into `buffer` where the data begins.

## See Also

- [func setInfluenceWeights(any MTLBuffer, offset: Int) throws(LowLevelDeformation.Error)](lowleveldeformation/skinning-swift.struct/setinfluenceweights(_:offset:).md)
  Sets the buffer containing per-vertex influence weights.
- [func setInverseBindPoses(any MTLBuffer, offset: Int) throws(LowLevelDeformation.Error)](lowleveldeformation/skinning-swift.struct/setinversebindposes(_:offset:).md)
  Sets the buffer containing inverse bind-pose matrices.
- [func replaceInfluenceJointIndices<R>((inout MutableRawSpan) -> R) throws(LowLevelDeformation.Error) -> R](lowleveldeformation/skinning-swift.struct/replaceinfluencejointindices(_:).md)
  Fills the influence joint index buffer using the given closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/skinning-swift.struct/setjointtransforms(_:offset:))*