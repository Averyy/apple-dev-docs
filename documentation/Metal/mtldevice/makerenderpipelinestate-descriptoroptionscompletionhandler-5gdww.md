# makeRenderPipelineState(descriptor:options:completionHandler:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Asynchronously creates a render pipeline state and reflection information.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor, options: MTLPipelineOption) async throws -> (any MTLRenderPipelineState, MTLRenderPipelineReflection?)
```

#### Discussion

Use the graphics-rendering pipeline state to configure a render pass by calling the [`setRenderPipelineState(_:)`](mtlrendercommandencoder/setrenderpipelinestate(_:).md) method of an [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md) instance.

## Parameters

- `descriptor`: An   instance.
- `options`: An   instance that represents the reflection information you want the method to generate.
- `completionHandler`: A Swift closure or an Objective-C block the method calls when it finishes creating the render pipeline state.

## See Also

- [func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor) throws -> any MTLRenderPipelineState](mtldevice/makerenderpipelinestate(descriptor:).md)
  Synchronously creates a render pipeline state.
- [func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor, completionHandler: ((any MTLRenderPipelineState)?, (any Error)?) -> Void)](mtldevice/makerenderpipelinestate(descriptor:completionhandler:).md)
  Asynchronously creates a render pipeline state.
- [func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor, options: MTLPipelineOption) throws -> (any MTLRenderPipelineState, MTLRenderPipelineReflection?)](mtldevice/makerenderpipelinestate(descriptor:options:)-89vxc.md)
  Synchronously creates a render pipeline state and reflection information in a tuple.
- [func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor, options: MTLPipelineOption, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedRenderPipelineReflection?>?) throws -> any MTLRenderPipelineState](mtldevice/makerenderpipelinestate(descriptor:options:reflection:).md)
  Synchronously creates a render pipeline state and reflection information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makerenderpipelinestate(descriptor:options:completionhandler:)-5gdww)*