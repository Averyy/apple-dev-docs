# makeRenderPipelineStateBySpecialization(descriptor:pipeline:)

**Framework**: Metal  
**Kind**: method

Creates a new render pipeline state from another, previously unspecialized, pipeline state.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func makeRenderPipelineStateBySpecialization(descriptor: MTL4PipelineDescriptor, pipeline: any MTLRenderPipelineState) throws -> any MTLRenderPipelineState
```

#### Return Value

A fully-specialized pipeline state object upon success, otherwise this function throws.

#### Discussion

Metal specializes the pipeline state with new state values the descriptor provides, observing the following rules:

- The compiler only updates properties that were originally specified as . It doesn’t modify other already-specialized properties
- The compiler sets to their default behavior any unspecialized properties that your passed-in descriptor doesn’t specialize

Additionally, there are some cases where the Metal can’t specialize a pipeline:

- If the original pipeline state object doesn’t have any unspecialized properties
- You can’t re-specialize a previously specialized pipeline state object

## Parameters

- `descriptor`: A render pipeline state descriptor or any type: default, tile, or mesh render pipeline descriptor.
- `pipeline`: A render pipeline state containing unspecialized substate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4compiler/makerenderpipelinestatebyspecialization(descriptor:pipeline:)-2636j)*