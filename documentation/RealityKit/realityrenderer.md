# RealityRenderer

**Framework**: RealityKit  
**Kind**: class

A renderer that displays a RealityKit scene in an existing Metal workflow.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
class RealityRenderer
```

#### Overview

All RealityKit APIs for loading resources, creating entities and adding components are compatible and work with `RealityRenderer`.

## Topics

### Structures
- [RealityRenderer.CameraOutput](realityrenderer/cameraoutput.md)
  Output produced by rendering with a camera.
- [RealityRenderer.CameraSettings](realityrenderer/camerasettings-swift.struct.md)
  Settings for rendering with a camera.
- [RealityRenderer.EntityCollection](realityrenderer/entitycollection.md)
  A collection of entities in a [`RealityRenderer`](realityrenderer.md).
- [RealityRenderer.ImageBasedLight](realityrenderer/imagebasedlight.md)
  Describe the lighting properties for the scene.
- [RealityRenderer.MetalEventAction](realityrenderer/metaleventaction.md)
  The structure describing an event and value to be signaled or waited for.
### Initializers
- [init() throws](realityrenderer/init.md)
### Instance Properties
- [var activeCamera: Entity?](realityrenderer/activecamera.md)
  The camera to be used for rendering.
- [var cameraSettings: RealityRenderer.CameraSettings](realityrenderer/camerasettings-swift.property.md)
  The settings to be used for rendering with `activeCamera`.
- [var entities: RealityRenderer.EntityCollection](realityrenderer/entities.md)
  A collection of RealityKit entities that this renderer renders within the scene.
- [var extendedDynamicRangeHeadroom: Float](realityrenderer/extendeddynamicrangeheadroom.md)
  The amount of headroom available for extended dynamic range content.
- [var extendedDynamicRangeOutput: Bool](realityrenderer/extendeddynamicrangeoutput.md)
  Specify whether the target Metal layer has been configured for EDR output.
- [var lighting: RealityRenderer.ImageBasedLight](realityrenderer/lighting.md)
  The lighting used in the environment of a particular scene.
### Instance Methods
- [func subscribe<E>(to: E.Type, on: (any EventSource)?, componentType: (any Component.Type)?, (E) -> Void) -> EventSubscription](realityrenderer/subscribe(to:on:componenttype:_:).md)
  Subscribes to an event type, optionally limited to events affecting a source entity or scene, or limited to a specific component type for component events.
- [func update(TimeInterval) throws](realityrenderer/update(_:).md)
  Tick the simulation
- [func updateAndRender(deltaTime: TimeInterval, cameraOutput: RealityRenderer.CameraOutput, whenScheduled: ((RealityRenderer) -> Void)?, onComplete: ((RealityRenderer) -> Void)?, actionsBeforeRender: [RealityRenderer.MetalEventAction], actionsAfterRender: [RealityRenderer.MetalEventAction]) throws](realityrenderer/updateandrender(deltatime:cameraoutput:whenscheduled:oncomplete:actionsbeforerender:actionsafterrender:).md)
  Tick the simulation and render using activeCamera and the camera rendering output.

## See Also

- [RealityRenderer.CameraSettings](realityrenderer/camerasettings-swift.struct.md)
  Settings for rendering with a camera.
- [RealityRenderer.CameraOutput](realityrenderer/cameraoutput.md)
  Output produced by rendering with a camera.
- [RealityRenderer.ImageBasedLight](realityrenderer/imagebasedlight.md)
  Describe the lighting properties for the scene.
- [RealityRenderer.MetalEventAction](realityrenderer/metaleventaction.md)
  The structure describing an event and value to be signaled or waited for.
- [RealityRenderer.EntityCollection](realityrenderer/entitycollection.md)
  A collection of entities in a [`RealityRenderer`](realityrenderer.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityrenderer)*