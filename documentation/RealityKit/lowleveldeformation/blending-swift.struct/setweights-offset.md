# setWeights(_:offset:)

**Framework**: RealityKit  
**Kind**: method

Sets the buffer containing blend-shape weights.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func setWeights(_ buffer: any MTLBuffer, offset: Int) throws(LowLevelDeformation.Error)
```

#### Discussion

The buffer must contain `targetCount` Float values, one per blend-shape target.

> **Note**: If `offset` is out of bounds for `buffer`, or if the buffer is too small.

## Parameters

- `buffer`: The Metal buffer containing the blend weights.
- `offset`: The byte offset into `buffer` where the data begins.

## See Also

- [func setPositionOffsets(any MTLBuffer, offset: Int) throws(LowLevelDeformation.Error)](lowleveldeformation/blending-swift.struct/setpositionoffsets(_:offset:).md)
  Sets the buffer containing blend-shape position offsets.
- [func setNormalOffsets(any MTLBuffer, offset: Int) throws(LowLevelDeformation.Error)](lowleveldeformation/blending-swift.struct/setnormaloffsets(_:offset:).md)
  Sets the buffer containing blend-shape normal offsets.
- [func setTangentOffsets(any MTLBuffer, offset: Int) throws(LowLevelDeformation.Error)](lowleveldeformation/blending-swift.struct/settangentoffsets(_:offset:).md)
  Sets the buffer containing blend-shape tangent offsets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/blending-swift.struct/setweights(_:offset:))*