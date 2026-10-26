# newRenderPipelineStateWithMeshDescriptor:options:reflection:error:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Synchronously creates a mesh render pipeline state and reflection information.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
- (id<MTLRenderPipelineState>) newRenderPipelineStateWithMeshDescriptor:(MTLMeshRenderPipelineDescriptor *) descriptor options:(MTLPipelineOption) options reflection:(MTLAutoreleasedRenderPipelineReflection*) reflection error:(NSError **) error;
```

#### Return Value

A new [`MTLRenderPipelineState`](../mtlrenderpipelinestate.md) instance if the method completes successfully; otherwise, `nil`.

#### Discussion

Use the graphics-rendering pipeline state to configure a render pass by calling the [`setRenderPipelineState(_:)`](../mtlrendercommandencoder/setrenderpipelinestate%28_%29.md) method of an [`MTLRenderCommandEncoder`](../mtlrendercommandencoder.md) instance.

## Parameters

- `descriptor`: An [`MTLMeshRenderPipelineDescriptor`](../mtlmeshrenderpipelinedescriptor.md) instance.
- `options`: An [`MTLPipelineOption`](../mtlpipelineoption.md) instance that represents the reflection information you want the method to generate.
- `reflection`: In Swift, an optional pointer to an [`MTLAutoreleasedRenderPipelineReflection`](../mtlautoreleasedrenderpipelinereflection.md) optional. In Objective-C, a pointer to an [`MTLAutoreleasedRenderPipelineReflection`](../mtlautoreleasedrenderpipelinereflection.md) instance.

  Pass `nil` in either language when you don’t need reflection data. Otherwise on return, if the method completes successfully, it assigns an [`MTLRenderPipelineReflection`](../mtlrenderpipelinereflection.md) instance to the pointee, which contains the details about the function arguments.
- `error`: On return, if an error occurs, a pointer to an error information instance; otherwise, `nil`.

## See Also

### Creating render pipeline states with mesh shaders
- [func makeRenderPipelineState(descriptor: MTLMeshRenderPipelineDescriptor, options: MTLPipelineOption, completionHandler: ((any MTLRenderPipelineState)?, MTLRenderPipelineReflection?, (any Error)?) -> Void)](./makerenderpipelinestate%28descriptor,options,completionhandler%29-1wvya.md)
  Asynchronously creates a mesh render pipeline state and reflection information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/newrenderpipelinestatewithmeshdescriptor:options:reflection:error:)*