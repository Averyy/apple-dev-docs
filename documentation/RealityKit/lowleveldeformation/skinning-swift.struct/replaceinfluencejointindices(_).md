# replaceInfluenceJointIndices(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Fills the influence joint index buffer using the given closure.    /// After the closure returns, the framework validates every index. An out-of-range index causes a throw.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func replaceInfluenceJointIndices<R>(_ body: @_lifetime(0: copy 0) (inout MutableRawSpan) -> R) throws -> R where R : ~Copyable
```

## Return Value

The value returned by `body`.

## Discussion

> **Throws**: If any index is outside `[0, skinning.jointTransformCount)`.

## Parameters

- `body`: A closure that receives a mutable span over the buffer.

## See Also

### Configuring skinning data
- [func setJointTransforms(any MTLBuffer, offset: Int) throws](./setjointtransforms%28_,offset%29.md)
  Sets the buffer containing joint transform matrices.
- [func setInfluenceWeights(any MTLBuffer, offset: Int) throws](./setinfluenceweights%28_,offset%29.md)
  Sets the buffer containing per-vertex influence weights.
- [func setInverseBindPoses(any MTLBuffer, offset: Int) throws](./setinversebindposes%28_,offset%29.md)
  Sets the buffer containing inverse bind-pose matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/skinning-swift.struct/replaceinfluencejointindices(_:))*