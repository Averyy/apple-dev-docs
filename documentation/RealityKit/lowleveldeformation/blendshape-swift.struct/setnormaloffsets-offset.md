# setNormalOffsets(_:offset:)

**Framework**: RealityKit  
**Kind**: method

Sets the buffer containing blend-shape normal offsets.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func setNormalOffsets(_ buffer: any MTLBuffer, offset: Int) throws
```

#### Discussion

The buffer must contain `targetCount × vertexCount` entries in the same format as the input mesh’s `.normal` attribute.

> **Note**: If `offset` is out of bounds for `buffer`, or if the buffer is too small.

## Parameters

- `buffer`: The Metal buffer containing the blend-shape normal offsets.
- `offset`: The byte offset into `buffer` where the data begins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/blendshape-swift.struct/setnormaloffsets(_:offset:))*