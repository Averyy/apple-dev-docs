# makeDeformation(pipeline:descriptor:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Creates a deformation bound to a compiled pipeline.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final func makeDeformation(pipeline: LowLevelDeformation.Pipeline, descriptor: LowLevelDeformation.Descriptor) throws -> LowLevelDeformation
```

## Discussion

The pipeline must originate from this context.

> **Throws**: If the pipeline belongs to a different context, or if the descriptor is invalid.

## Parameters

- `pipeline`: The compiled pipeline to bind the deformation to.
- `descriptor`: An object that describes the per-frame data requirements.

## See Also

### Creating deformation pipelines
- [func makePipeline(LowLevelDeformation.Pipeline.Descriptor) throws -> LowLevelDeformation.Pipeline](./makepipeline%28_%29-5mxko.md)
  Creates a compute pipeline synchronously.
- [func makePipeline(LowLevelDeformation.Pipeline.Descriptor) async throws -> LowLevelDeformation.Pipeline](./makepipeline%28_%29-6625d.md)
  Creates a compute pipeline asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformationcontext/makedeformation(pipeline:descriptor:))*