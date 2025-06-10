# Resource

**Framework**: RealityKit  
**Kind**: protocol

A shared resource you use to configure a component, like a material, mesh, or texture.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@preconcurrency
protocol Resource : Sendable
```

#### Overview

Resources can be costly to load or create. Share and reuse resources as much as possible.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [AnimationResource](animationresource.md)
- [AudioBufferResource](audiobufferresource.md)
- [AudioFileGroupResource](audiofilegroupresource.md)
- [AudioFileResource](audiofileresource.md)
- [AudioResource](audioresource.md)
- [BlendShapeWeightsMapping](blendshapeweightsmapping.md)
- [EnvironmentResource](environmentresource.md)
- [IKResource](ikresource.md)
- [MeshResource](meshresource.md)
- [PhysicsMaterialResource](physicsmaterialresource.md)
- [ShapeResource](shaperesource.md)
- [TextureResource](textureresource.md)

## See Also

- [Improving the Performance of a RealityKit App](improving-the-performance-of-a-realitykit-app.md)
  Measure CPU and GPU utilization to find ways to improve your app’s performance.
- [Reducing GPU Utilization in Your RealityKit App](reducing-gpu-utilization-in-your-realitykit-app.md)
  Prevent the GPU from limiting your app’s frame rate by reducing the complexity of your render.
- [Reducing CPU Utilization in Your RealityKit App](reducing-cpu-utilization-in-your-realitykit-app.md)
  Target specific CPU metrics with adjustments to your app and its content.
- [Construct an immersive environment for visionOS](construct-an-immersive-environment-for-visionos.md)
  Build efficient custom worlds for your app.
- [Passing Metal command objects around your application](passing-metal-command-objects-around-your-application.md)
  Build a system that creates and passes Metal command objects to entities dispatching Metal compute shaders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/resource)*