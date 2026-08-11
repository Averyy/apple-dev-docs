# render(using:_:)

**Framework**: RealityKit  
**Kind**: method

Encodes draw calls for the frame into the given command buffer using a caller-controlled render callback.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func render(using commandBuffer: any MTLCommandBuffer, _ callback: @_lifetime(0: copy 0) (inout LowLevelRenderer.RenderState) -> ())
```

#### Discussion

Inside the callback, call `state.render(meshInstancesArrayIndex:meshInstanceIndex:)` or `state.render(meshInstancesArrayIndex:range:)` to encode draw calls in any order. You control which instances are drawn and in what sequence — use `sortMeshInstances(_:indices:configuration:)` for built-in depth sorting, `cullMeshInstances(_:indices:configuration:)` to remove instances outside the view frustum before drawing, or supply your own ordering.

You are responsible for committing the command buffer after this call returns.

## Parameters

- `commandBuffer`: The Metal command buffer to encode draw calls into.
- `callback`: A closure that receives a `RenderState` and issues draw calls.

## See Also

- [LowLevelRenderer.RenderState](lowlevelrenderer/renderstate.md)
  The per-frame render state passed to the `render(using:_:)` callback.
- [LowLevelRenderer.Resources](lowlevelrenderer/resources.md)
  Prepared GPU resources for a renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/render(using:_:))*