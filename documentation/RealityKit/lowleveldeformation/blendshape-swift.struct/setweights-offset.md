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
func setWeights(_ buffer: any MTLBuffer, offset: Int) throws
```

#### Discussion

The buffer must contain `targetCount` Float values, one per blend-shape target.

> **Note**: If `offset` is out of bounds for `buffer`, or if the buffer is too small.

## Parameters

- `buffer`: The Metal buffer containing the blend weights.
- `offset`: The byte offset into `buffer` where the data begins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/blendshape-swift.struct/setweights(_:offset:))*