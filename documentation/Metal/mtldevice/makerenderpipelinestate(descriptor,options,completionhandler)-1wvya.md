# makeRenderPipelineState(descriptor:options:completionHandler:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asynchronously creates a mesh render pipeline state and reflection information.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func makeRenderPipelineState(descriptor: MTLMeshRenderPipelineDescriptor, options: MTLPipelineOption, completionHandler: @escaping @Sendable ((any MTLRenderPipelineState)?, MTLRenderPipelineReflection?, (any Error)?) -> Void)
```

```swift
func makeRenderPipelineState(descriptor: MTLMeshRenderPipelineDescriptor, options: MTLPipelineOption) async throws -> (any MTLRenderPipelineState, MTLRenderPipelineReflection?)
```

```objc
- (void) newRenderPipelineStateWithMeshDescriptor:(MTLMeshRenderPipelineDescriptor *) descriptor options:(MTLPipelineOption) options completionHandler:(MTLNewRenderPipelineStateWithReflectionCompletionHandler) completionHandler;
```

#### Discussion

Use the graphics-rendering pipeline state to configure a render pass by calling the [`setRenderPipelineState(_:)`](../mtlrendercommandencoder/setrenderpipelinestate%28_%29.md) method of an [`MTLRenderCommandEncoder`](../mtlrendercommandencoder.md) instance.

## Parameters

- `descriptor`: An [`MTLMeshRenderPipelineDescriptor`](../mtlmeshrenderpipelinedescriptor.md) instance.
- `options`: An [`MTLPipelineOption`](../mtlpipelineoption.md) instance that represents the reflection information you want the method to generate.
- `completionHandler`: A Swift closure or an Objective-C block the method calls when it finishes creating the render pipeline state.

## Default Implementations

### MTLDevice Implementations
- [func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor, options: MTLPipelineOption) throws -> (any MTLRenderPipelineState, MTLRenderPipelineReflection?)](./makerenderpipelinestate%28descriptor,options%29-89vxc.md)
  Synchronously creates a render pipeline state and reflection information in a tuple.
- [func makeRenderPipelineState(descriptor: MTLMeshRenderPipelineDescriptor, options: MTLPipelineOption) throws -> (any MTLRenderPipelineState, MTLRenderPipelineReflection?)](./makerenderpipelinestate%28descriptor,options%29-yrak.md)
  Synchronously creates a mesh render pipeline state and reflection information in a tuple.

## See Also

### Creating render pipeline states with mesh shaders
- [func makeRenderPipelineState(descriptor: MTLMeshRenderPipelineDescriptor, options: MTLPipelineOption) throws -> (any MTLRenderPipelineState, MTLRenderPipelineReflection?)](./makerenderpipelinestate%28descriptor,options%29-yrak.md)
  Synchronously creates a mesh render pipeline state and reflection information in a tuple.
- [- newRenderPipelineStateWithMeshDescriptor:options:reflection:error:](./newrenderpipelinestatewithmeshdescriptor_options_reflection_error_.md)
  Synchronously creates a mesh render pipeline state and reflection information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makerenderpipelinestate(descriptor:options:completionhandler:)-1wvya)*