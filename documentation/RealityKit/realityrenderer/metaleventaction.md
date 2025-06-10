# RealityRenderer.MetalEventAction

**Framework**: RealityKit  
**Kind**: struct

The structure describing an event and value to be signaled or waited for.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
struct MetalEventAction
```

## Topics

### Instance Properties
- [let event: any MTLEvent](realityrenderer/metaleventaction/event.md)
  The metal event object to be signaled or waited for.
- [let value: UInt64](realityrenderer/metaleventaction/value.md)
  The value to be signaled or waited for.
### Type Methods
- [static func signal(any MTLEvent, value: UInt64) -> RealityRenderer.MetalEventAction](realityrenderer/metaleventaction/signal(_:value:).md)
  Returns an action that represents signaling event with the value.
- [static func wait(for: any MTLEvent, value: UInt64) -> RealityRenderer.MetalEventAction](realityrenderer/metaleventaction/wait(for:value:).md)
  Returns an action that represents waiting for an event to reach the value.

## See Also

- [class RealityRenderer](realityrenderer.md)
  A renderer that displays a RealityKit scene in an existing Metal workflow.
- [RealityRenderer.CameraSettings](realityrenderer/camerasettings-swift.struct.md)
  Settings for rendering with a camera.
- [RealityRenderer.CameraOutput](realityrenderer/cameraoutput.md)
  Output produced by rendering with a camera.
- [RealityRenderer.ImageBasedLight](realityrenderer/imagebasedlight.md)
  Describe the lighting properties for the scene.
- [RealityRenderer.EntityCollection](realityrenderer/entitycollection.md)
  A collection of entities in a [`RealityRenderer`](realityrenderer.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityrenderer/metaleventaction)*