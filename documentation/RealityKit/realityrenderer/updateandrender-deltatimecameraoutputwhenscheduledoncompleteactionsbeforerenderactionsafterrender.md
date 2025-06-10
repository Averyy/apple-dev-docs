# updateAndRender(deltaTime:cameraOutput:whenScheduled:onComplete:actionsBeforeRender:actionsAfterRender:)

**Framework**: RealityKit  
**Kind**: method

Tick the simulation and render using activeCamera and the camera rendering output.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func updateAndRender(deltaTime: TimeInterval, cameraOutput: RealityRenderer.CameraOutput, whenScheduled: ((RealityRenderer) -> Void)? = nil, onComplete: ((RealityRenderer) -> Void)? = nil, actionsBeforeRender: [RealityRenderer.MetalEventAction] = [], actionsAfterRender: [RealityRenderer.MetalEventAction] = []) throws
```

## Parameters

- `deltaTime`: The delta time to advance the simulation
- `cameraOutput`: Specifies output for rendering with 
- `whenScheduled`: A handler that is called when the corresponding MTLCommandBuffer is scheduled
- `onComplete`: A handler that is called when the corresponding MTLCommandBuffer is complete
- `actionsBeforeRender`: Array of events and values to wait before GPU rendering work
- `actionsAfterRender`: Array of events and values to signal after GPU rendering work


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityrenderer/updateandrender(deltatime:cameraoutput:whenscheduled:oncomplete:actionsbeforerender:actionsafterrender:))*