# setPositionOffsets(_:offset:)

**Framework**: RealityKit  
**Kind**: method

Sets the buffer containing blend-shape position offsets.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func setPositionOffsets(_ buffer: any MTLBuffer, offset: Int) throws
```

#### Discussion

The buffer must contain `targetCount × vertexCount` entries in the same format as the input mesh’s `.position` attribute.

> **Note**: If `offset` is out of bounds for `buffer`, or if the buffer is too small.

## Parameters

- `buffer`: The Metal buffer containing the blend-shape position offsets.
- `offset`: The byte offset into `buffer` where the data begins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/blendshape-swift.struct/setpositionoffsets(_:offset:))*