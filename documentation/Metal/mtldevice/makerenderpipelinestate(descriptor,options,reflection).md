# makeRenderPipelineState(descriptor:options:reflection:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Synchronously creates a render pipeline state and reflection information.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor, options: MTLPipelineOption, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedRenderPipelineReflection?>?) throws -> any MTLRenderPipelineState
```

```objc
- (id<MTLRenderPipelineState>) newRenderPipelineStateWithDescriptor:(MTLRenderPipelineDescriptor *) descriptor options:(MTLPipelineOption) options reflection:(MTLAutoreleasedRenderPipelineReflection*) reflection error:(NSError **) error;
```

## Return Value

A new [`MTLRenderPipelineState`](../mtlrenderpipelinestate.md) instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

## Discussion

Use the graphics-rendering pipeline state to configure a render pass by calling the [`setRenderPipelineState(_:)`](../mtlrendercommandencoder/setrenderpipelinestate%28_%29.md) method of an [`MTLRenderCommandEncoder`](../mtlrendercommandencoder.md) instance.

## Parameters

- `descriptor`: An [`MTLRenderPipelineDescriptor`](../mtlrenderpipelinedescriptor.md) instance.
- `options`: An [`MTLPipelineOption`](../mtlpipelineoption.md) instance that represents the reflection information you want the method to generate.
- `reflection`: In Swift, an optional pointer to an [`MTLAutoreleasedRenderPipelineReflection`](../mtlautoreleasedrenderpipelinereflection.md) optional. In Objective-C, a pointer to an [`MTLAutoreleasedRenderPipelineReflection`](../mtlautoreleasedrenderpipelinereflection.md) instance.

  Pass `nil` in either language when you don’t need reflection data. Otherwise on return, if the method completes successfully, it assigns an [`MTLRenderPipelineReflection`](../mtlrenderpipelinereflection.md) instance to the pointee, which contains the details about the function arguments.

## See Also

### Creating render pipeline states with vertex shaders
- [func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor) throws -> any MTLRenderPipelineState](./makerenderpipelinestate%28descriptor%29.md)
  Synchronously creates a render pipeline state.
- [func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor, completionHandler: ((any MTLRenderPipelineState)?, (any Error)?) -> Void)](./makerenderpipelinestate%28descriptor,completionhandler%29.md)
  Asynchronously creates a render pipeline state.
- [func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor, options: MTLPipelineOption) throws -> (any MTLRenderPipelineState, MTLRenderPipelineReflection?)](./makerenderpipelinestate%28descriptor,options%29-89vxc.md)
  Synchronously creates a render pipeline state and reflection information in a tuple.
- [func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor, options: MTLPipelineOption, completionHandler: ((any MTLRenderPipelineState)?, MTLRenderPipelineReflection?, (any Error)?) -> Void)](./makerenderpipelinestate%28descriptor,options,completionhandler%29-5gdww.md)
  Asynchronously creates a render pipeline state and reflection information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makerenderpipelinestate(descriptor:options:reflection:))*