# LowLevelDeformation.Pipeline

**Framework**: RealityKit  
**Kind**: class

A compiled compute pipeline for a specific combination of mesh layouts and deformer stages.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class Pipeline
```

#### Overview

Create a pipeline once and reuse it across frames.

## Topics

### Creating a pipeline
- [LowLevelDeformation.Pipeline.Descriptor](lowleveldeformation/pipeline/descriptor.md)
  An object that describes the vertex layouts and deformer stages for a pipeline.

## See Also

- [func encode(into: any MTLComputeCommandEncoder) throws](lowleveldeformation/encode(into:).md)
  Encodes the configured deformation passes into the given command encoder.
- [LowLevelDeformation.Error](lowleveldeformation/error.md)
  The error type thrown by every throwing method and initializer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/pipeline)*