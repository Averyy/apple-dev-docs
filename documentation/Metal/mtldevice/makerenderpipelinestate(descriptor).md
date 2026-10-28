# makeRenderPipelineState(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Synchronously creates a render pipeline state.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor) throws -> any MTLRenderPipelineState
```

```objc
- (id<MTLRenderPipelineState>) newRenderPipelineStateWithDescriptor:(MTLRenderPipelineDescriptor *) descriptor error:(NSError **) error;
```

## Return Value

A new [`MTLRenderPipelineState`](../mtlrenderpipelinestate.md) instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

## Discussion

Use the graphics-rendering pipeline state to configure a render pass by calling the [`setRenderPipelineState(_:)`](../mtlrendercommandencoder/setrenderpipelinestate%28_%29.md) method of an [`MTLRenderCommandEncoder`](../mtlrendercommandencoder.md) instance.

## Parameters

- `descriptor`: An [`MTLRenderPipelineDescriptor`](../mtlrenderpipelinedescriptor.md) instance.

## See Also

### Creating render pipeline states with vertex shaders
- [func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor, completionHandler: ((any MTLRenderPipelineState)?, (any Error)?) -> Void)](./makerenderpipelinestate%28descriptor,completionhandler%29.md)
  Asynchronously creates a render pipeline state.
- [func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor, options: MTLPipelineOption) throws -> (any MTLRenderPipelineState, MTLRenderPipelineReflection?)](./makerenderpipelinestate%28descriptor,options%29-89vxc.md)
  Synchronously creates a render pipeline state and reflection information in a tuple.
- [func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor, options: MTLPipelineOption, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedRenderPipelineReflection?>?) throws -> any MTLRenderPipelineState](./makerenderpipelinestate%28descriptor,options,reflection%29.md)
  Synchronously creates a render pipeline state and reflection information.
- [func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor, options: MTLPipelineOption, completionHandler: ((any MTLRenderPipelineState)?, MTLRenderPipelineReflection?, (any Error)?) -> Void)](./makerenderpipelinestate%28descriptor,options,completionhandler%29-5gdww.md)
  Asynchronously creates a render pipeline state and reflection information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makerenderpipelinestate(descriptor:))*