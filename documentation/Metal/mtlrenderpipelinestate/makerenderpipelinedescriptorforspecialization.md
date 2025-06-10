# makeRenderPipelineDescriptorForSpecialization()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a render pipeline descriptor from this pipeline that you can use for pipeline specialization.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func makeRenderPipelineDescriptorForSpecialization() -> MTL4PipelineDescriptor
```

#### Return Value

A new pipeline descriptor that you use for pipeline state specialization.

#### Discussion

Use this method to obtain a new [`MTL4PipelineDescriptor`](mtl4pipelinedescriptor.md) instance that you can use to specialize any unspecialized properties in this pipeline state object.

The returned descriptor contains every unspecialized field in the current pipeline state object, set to unspecialized. It may, however, not contain valid or accurate properties in any other field.

This descriptor is only valid for the purpose of calling specialization functions on the [`MTL4Compiler`](mtl4compiler.md) to specialize this pipeline, for example: [`newRenderPipelineStateBySpecializationWithDescriptor:pipeline:error:`](mtl4compiler/newrenderpipelinestatebyspecializationwithdescriptor:pipeline:error:.md).

Although this method returns the [`MTL4PipelineDescriptor`](mtl4pipelinedescriptor.md) base class, the concrete instance this method returns corresponds to the specific descriptor type for the creation of this pipeline state, for example if a [`MTL4Compiler`](mtl4compiler.md) instance creates this current pipeline form a [`MTLTileRenderPipelineDescriptor`](mtltilerenderpipelinedescriptor.md), this method returns a concrete [`MTLTileRenderPipelineDescriptor`](mtltilerenderpipelinedescriptor.md) instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/makerenderpipelinedescriptorforspecialization())*