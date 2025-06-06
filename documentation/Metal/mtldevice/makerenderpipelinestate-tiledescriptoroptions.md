# makeRenderPipelineState(tileDescriptor:options:)

**Framework**: Metal  
**Kind**: method

Synchronously creates a tile shader’s render pipeline state and reflection information in a tuple.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.5+
- visionOS ?+

## Declaration

```swift
func makeRenderPipelineState(tileDescriptor: MTLTileRenderPipelineDescriptor, options: MTLPipelineOption) throws -> (any MTLRenderPipelineState, MTLRenderPipelineReflection?)
```

#### Return Value

A tuple with a new [`MTLTileRenderPipelineDescriptor`](mtltilerenderpipelinedescriptor.md) instance and an [`MTLRenderPipelineReflection`](mtlrenderpipelinereflection.md) optional instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

## Parameters

- `tileDescriptor`: An   instance.
- `options`: An   instance that represents the reflection information you want the method to generate.

## See Also

- [func makeRenderPipelineState(tileDescriptor: MTLTileRenderPipelineDescriptor, options: MTLPipelineOption, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedRenderPipelineReflection?>?) throws -> any MTLRenderPipelineState](mtldevice/makerenderpipelinestate(tiledescriptor:options:reflection:).md)
  Synchronously creates a tile shader’s render pipeline state and reflection information.
- [func makeRenderPipelineState(tileDescriptor: MTLTileRenderPipelineDescriptor, options: MTLPipelineOption, completionHandler: MTLNewRenderPipelineStateWithReflectionCompletionHandler)](mtldevice/makerenderpipelinestate(tiledescriptor:options:completionhandler:).md)
  Asynchronously creates a tile shader’s render pipeline state and reflection information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makerenderpipelinestate(tiledescriptor:options:))*