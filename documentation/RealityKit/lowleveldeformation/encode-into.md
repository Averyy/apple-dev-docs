# encode(into:)

**Framework**: RealityKit  
**Kind**: method

Encodes the configured deformation passes into the given command encoder.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func encode(into encoder: any MTLComputeCommandEncoder) throws(LowLevelDeformation.Error)
```

#### Discussion

Call `input.setVertices(_:offset:semantic:)` and `output.setVertices(_:offset:semantic:)` before calling this method each frame.

> **Note**: If any required buffer has not been set, or if `encoder` uses concurrent dispatch.

## Parameters

- `encoder`: A serial Metal compute command encoder.

## See Also

- [LowLevelDeformation.Pipeline](lowleveldeformation/pipeline.md)
  A compiled compute pipeline for a specific combination of mesh layouts and deformer stages.
- [LowLevelDeformation.Error](lowleveldeformation/error.md)
  The error type thrown by every throwing method and initializer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/encode(into:))*