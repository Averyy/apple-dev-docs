# makeRenderPipelineState(tileDescriptor:options:completionHandler:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Asynchronously creates a tile shader’s render pipeline state and reflection information.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
func makeRenderPipelineState(tileDescriptor descriptor: MTLTileRenderPipelineDescriptor, options: MTLPipelineOption) async throws -> (any MTLRenderPipelineState, MTLRenderPipelineReflection?)
```

## Parameters

- `descriptor`: An   instance.
- `options`: An   instance that represents the reflection information you want the method to generate.
- `completionHandler`: A Swift closure or an Objective-C block the method calls   when it finishes creating the render pipeline state.

## See Also

- [func makeRenderPipelineState(tileDescriptor: MTLTileRenderPipelineDescriptor, options: MTLPipelineOption) throws -> (any MTLRenderPipelineState, MTLRenderPipelineReflection?)](mtldevice/makerenderpipelinestate(tiledescriptor:options:).md)
  Synchronously creates a tile shader’s render pipeline state and reflection information in a tuple.
- [func makeRenderPipelineState(tileDescriptor: MTLTileRenderPipelineDescriptor, options: MTLPipelineOption, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedRenderPipelineReflection?>?) throws -> any MTLRenderPipelineState](mtldevice/makerenderpipelinestate(tiledescriptor:options:reflection:).md)
  Synchronously creates a tile shader’s render pipeline state and reflection information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makerenderpipelinestate(tiledescriptor:options:completionhandler:))*