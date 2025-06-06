# makeRenderPipelineState(descriptor:options:)

**Framework**: Metal  
**Kind**: method

Synchronously creates a render pipeline state and reflection information in a tuple.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS ?+

## Declaration

```swift
func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor, options: MTLPipelineOption) throws -> (any MTLRenderPipelineState, MTLRenderPipelineReflection?)
```

#### Return Value

A tuple with a new [`MTLRenderPipelineState`](mtlrenderpipelinestate.md) instance and an [`MTLRenderPipelineReflection`](mtlrenderpipelinereflection.md) optional instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

#### Discussion

Use the graphics-rendering pipeline state to configure a render pass by calling the [`setRenderPipelineState(_:)`](mtlrendercommandencoder/setrenderpipelinestate(_:).md) method of an [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md) instance.

## Parameters

- `descriptor`: An   instance.
- `options`: An   instance that represents the reflection information you want the method to generate.

## See Also

- [func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor) throws -> any MTLRenderPipelineState](mtldevice/makerenderpipelinestate(descriptor:).md)
  Synchronously creates a render pipeline state.
- [func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor, completionHandler: MTLNewRenderPipelineStateCompletionHandler)](mtldevice/makerenderpipelinestate(descriptor:completionhandler:).md)
  Asynchronously creates a render pipeline state.
- [func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor, options: MTLPipelineOption, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedRenderPipelineReflection?>?) throws -> any MTLRenderPipelineState](mtldevice/makerenderpipelinestate(descriptor:options:reflection:).md)
  Synchronously creates a render pipeline state and reflection information.
- [func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor, options: MTLPipelineOption, completionHandler: MTLNewRenderPipelineStateWithReflectionCompletionHandler)](mtldevice/makerenderpipelinestate(descriptor:options:completionhandler:)-5gdww.md)
  Asynchronously creates a render pipeline state and reflection information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makerenderpipelinestate(descriptor:options:)-89vxc)*