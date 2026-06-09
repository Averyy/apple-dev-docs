# replaceInfluenceJointIndices(_:)

**Framework**: RealityKit  
**Kind**: method

Fills the influence joint index buffer using the given closure.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func replaceInfluenceJointIndices<R>(_ body: @_lifetime(0: copy 0) (inout MutableRawSpan) -> R) throws(LowLevelDeformation.Error) -> R where R : ~Copyable
```

#### Return Value

The value returned by `body`.

#### Discussion

After the closure returns, the framework validates every index. An out-of-range index causes a throw.

> **Note**: If any index is outside `[0, skinning.jointTransformCount)`.

## Parameters

- `body`: A closure that receives a mutable span over the buffer.

## See Also

- [func setJointTransforms(any MTLBuffer, offset: Int) throws(LowLevelDeformation.Error)](lowleveldeformation/skinning-swift.struct/setjointtransforms(_:offset:).md)
  Sets the buffer containing joint transform matrices.
- [func setInfluenceWeights(any MTLBuffer, offset: Int) throws(LowLevelDeformation.Error)](lowleveldeformation/skinning-swift.struct/setinfluenceweights(_:offset:).md)
  Sets the buffer containing per-vertex influence weights.
- [func setInverseBindPoses(any MTLBuffer, offset: Int) throws(LowLevelDeformation.Error)](lowleveldeformation/skinning-swift.struct/setinversebindposes(_:offset:).md)
  Sets the buffer containing inverse bind-pose matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/skinning-swift.struct/replaceinfluencejointindices(_:))*