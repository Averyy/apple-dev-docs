# PostProcessEffect

**Framework**: RealityKit  
**Kind**: protocol  
**Role**: Protocol

A protocol that defines hooks for custom post processing effects.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
protocol PostProcessEffect : Sendable
```

#### Overview

RealityKit calls each method in this protocol at a predefined time. For example, RealityKit calls the [`postProcess(context:)`](./postprocesseffect/postprocess%28context%29.md) method every frame, after RealityKit renders the scene, but before displaying it in your app.

Adopt this protocol in a custom object and apply it to your [`RealityViewCameraContent`](./realityviewcameracontent.md) to apply fine-grained control over the render loop.

## Topics

### Instance Methods
- [func postProcess(context: borrowing PostProcessEffectContext<any MTLCommandBuffer>)](./postprocesseffect/postprocess%28context%29.md)
  A method where you can implement postprocess effects.
- [func prepare(for: any MTLDevice)](./postprocesseffect/prepare%28for%29.md)
  A method where you can prepare the metal device with initial setup work.

## Relationships

### Inherits From
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Postprocessing
- [Postprocessing effects](./postprocessing-effects.md)
  Create special rendering effects for your RealityKit scenes.
- [ARView.PostProcessContext](./arview/postprocesscontext.md)
  An object the framework uses to pass data to a postprocess callback.
- [ARView.RenderCallbacks](./arview/rendercallbacks-swift.struct.md)
  A container that holds the view’s render callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/postprocesseffect)*