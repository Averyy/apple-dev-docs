# setInfluenceWeights(_:offset:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Sets the buffer containing per-vertex influence weights.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func setInfluenceWeights(_ buffer: any MTLBuffer, offset: Int) throws
```

## Discussion

The buffer must contain `influencesPerVertex × vertexCount` Float values.

> **Throws**: If `offset` is out of bounds for `buffer`, or if the buffer is too small.

## Parameters

- `buffer`: The Metal buffer containing the influence weights.
- `offset`: The byte offset into `buffer` where the data begins.

## See Also

### Configuring skinning data
- [func setJointTransforms(any MTLBuffer, offset: Int) throws](./setjointtransforms%28_,offset%29.md)
  Sets the buffer containing joint transform matrices.
- [func setInverseBindPoses(any MTLBuffer, offset: Int) throws](./setinversebindposes%28_,offset%29.md)
  Sets the buffer containing inverse bind-pose matrices.
- [func replaceInfluenceJointIndices<R>((inout MutableRawSpan) -> R) throws -> R](./replaceinfluencejointindices%28_%29.md)
  Fills the influence joint index buffer using the given closure.    /// After the closure returns, the framework validates every index. An out-of-range index causes a throw.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/skinning-swift.struct/setinfluenceweights(_:offset:))*