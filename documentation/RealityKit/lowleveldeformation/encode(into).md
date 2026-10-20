# encode(into:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Encodes the configured deformation passes into the given command encoder.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final func encode(into encoder: any MTLComputeCommandEncoder) throws
```

#### Discussion

Call `input.setVertices(_:offset:semantic:)` and `output.setVertices(_:offset:semantic:)` before calling this method each frame.

> **Throws**: If any required buffer has not been set, or if `encoder` uses concurrent dispatch.

## Parameters

- `encoder`: A serial Metal compute command encoder.

## See Also

### Encoding deformation work
- [LowLevelDeformation.Pipeline](./pipeline.md)
  A compiled compute pipeline for a specific combination of mesh layouts and deformer stages.
- [LowLevelDeformation.Error](./error.md)
  The error type thrown by every throwing method and initializer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/encode(into:))*