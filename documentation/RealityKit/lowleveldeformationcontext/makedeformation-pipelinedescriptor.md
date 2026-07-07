# makeDeformation(pipeline:descriptor:)

**Framework**: RealityKit  
**Kind**: method

Creates a deformation bound to a compiled pipeline.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func makeDeformation(pipeline: LowLevelDeformation.Pipeline, descriptor: LowLevelDeformation.Descriptor) throws -> LowLevelDeformation
```

#### Discussion

The pipeline must originate from this context.

> **Note**: If the pipeline belongs to a different context, or if the descriptor is invalid.

## Parameters

- `pipeline`: The compiled pipeline to bind the deformation to.
- `descriptor`: An object that describes the per-frame data requirements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformationcontext/makedeformation(pipeline:descriptor:))*