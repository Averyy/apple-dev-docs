# setPositionOffsets(_:offset:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Sets the buffer containing blend-shape position offsets.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func setPositionOffsets(_ buffer: any MTLBuffer, offset: Int) throws
```

## Discussion

The buffer must contain `targetCount × vertexCount` entries in the same format as the input mesh’s `.position` attribute.

> **Throws**: If `offset` is out of bounds for `buffer`, or if the buffer is too small.

## Parameters

- `buffer`: The Metal buffer containing the blend-shape position offsets.
- `offset`: The byte offset into `buffer` where the data begins.

## See Also

### Setting blend data
- [func setNormalOffsets(any MTLBuffer, offset: Int) throws](./setnormaloffsets%28_,offset%29.md)
  Sets the buffer containing blend-shape normal offsets.
- [func setTangentOffsets(any MTLBuffer, offset: Int) throws](./settangentoffsets%28_,offset%29.md)
  Sets the buffer containing blend-shape tangent offsets.
- [func setWeights(any MTLBuffer, offset: Int) throws](./setweights%28_,offset%29.md)
  Sets the buffer containing blend-shape weights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/blendshape-swift.struct/setpositionoffsets(_:offset:))*