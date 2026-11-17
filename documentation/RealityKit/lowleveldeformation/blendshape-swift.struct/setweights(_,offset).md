# setWeights(_:offset:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Sets the buffer containing blend-shape weights.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func setWeights(_ buffer: any MTLBuffer, offset: Int) throws
```

## Discussion

The buffer must contain `targetCount` Float values, one per blend-shape target.

> **Throws**: If `offset` is out of bounds for `buffer`, or if the buffer is too small.

## Parameters

- `buffer`: The Metal buffer containing the blend weights.
- `offset`: The byte offset into `buffer` where the data begins.

## See Also

### Setting blend data
- [func setPositionOffsets(any MTLBuffer, offset: Int) throws](./setpositionoffsets%28_,offset%29.md)
  Sets the buffer containing blend-shape position offsets.
- [func setNormalOffsets(any MTLBuffer, offset: Int) throws](./setnormaloffsets%28_,offset%29.md)
  Sets the buffer containing blend-shape normal offsets.
- [func setTangentOffsets(any MTLBuffer, offset: Int) throws](./settangentoffsets%28_,offset%29.md)
  Sets the buffer containing blend-shape tangent offsets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/blendshape-swift.struct/setweights(_:offset:))*