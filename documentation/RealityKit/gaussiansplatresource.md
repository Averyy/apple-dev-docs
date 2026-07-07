# GaussianSplatResource

**Framework**: RealityKit  
**Kind**: class

A container for the splat data and rendering options that a Gaussian splat component displays.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class GaussianSplatResource
```

#### Overview

A Gaussian splat resource holds the per-splat data the framework renders, together with the options that control how it renders that data: the scale and opacity activation functions, the projection mode, the sorting mode, and the color space.

Create a resource from a [`GaussianSplatResource.BufferResource`](gaussiansplatresource/bufferresource-swift.struct.md) that describes your splat buffers, then attach it to an entity with a [`GaussianSplatComponent`](gaussiansplatcomponent.md):

```swift
let resource = GaussianSplatResource(bufferResource)
let entity = Entity()
entity.components.set(GaussianSplatComponent(resource))
```

For a complete example that builds the buffer resource from source data, see [`GaussianSplatComponent`](gaussiansplatcomponent.md).

The framework references the resource’s buffers rather than copying them, so you can update the contents of the underlying `LowLevelBuffer` instances to animate the splats over time.

## Topics

### Structures
- [GaussianSplatResource.BufferDescriptor](gaussiansplatresource/bufferdescriptor.md)
  A description of where one per-splat property lives within a buffer.
- [GaussianSplatResource.BufferResource](gaussiansplatresource/bufferresource-swift.struct.md)
  A set of buffer descriptors that supplies the per-splat data for rendering.
### Initializers
- [init(GaussianSplatResource.BufferResource)](gaussiansplatresource/init(_:).md)
  Creates a resource from a buffer resource.
### Instance Properties
- [let bufferResource: GaussianSplatResource.BufferResource?](gaussiansplatresource/bufferresource-swift.property.md)
  The buffer-based splat data the resource renders, if any.
- [var colorSpace: CGColorSpace](gaussiansplatresource/colorspace.md)
  The color space the framework uses to interpret splat colors.
- [var opacityActivation: GaussianSplatResource.ActivationFunction](gaussiansplatresource/opacityactivation.md)
  The transformation the framework applies to the opacity values before rendering.
- [var projectionMode: GaussianSplatResource.ProjectionMode](gaussiansplatresource/projectionmode-swift.property.md)
  The projection technique the framework uses for splat footprints.
- [var scaleActivation: GaussianSplatResource.ActivationFunction](gaussiansplatresource/scaleactivation.md)
  The transformation the framework applies to the scale values before rendering.
- [var sortingMode: GaussianSplatResource.SortingMode](gaussiansplatresource/sortingmode-swift.property.md)
  The order in which the framework draws splats to blend their opacity.
### Enumerations
- [GaussianSplatResource.ActivationFunction](gaussiansplatresource/activationfunction.md)
  A transformation the framework applies to raw scale or opacity values before rendering.
- [GaussianSplatResource.ProjectionMode](gaussiansplatresource/projectionmode-swift.enum.md)
  The technique the framework uses to project a 3D splat onto the 2D screen.
- [GaussianSplatResource.SortingMode](gaussiansplatresource/sortingmode-swift.enum.md)
  The available ways to order splats so the framework blends their opacity correctly.
- [GaussianSplatResource.SphericalHarmonicDegree](gaussiansplatresource/sphericalharmonicdegree.md)
  The amount of view-dependent color detail stored per splat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/gaussiansplatresource)*