# GaussianSplatResource

**Framework**: RealityKit  
**Kind**: class

A component that renders 3D Gaussian splat data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class GaussianSplatResource
```

#### Overview

Use `GaussianSplatComponent` to display volumetric imagery captured from real environments, coalesced into 3D Gaussian splats (3DGS). Gaussian splatting is a rendering technique that represents a scene as a collection of 3D Gaussian primitives, each with a position, scale, rotation, opacity, and color defined by spherical harmonic coefficients. The result is a high-fidelity reproduction of a captured scene that people can view from novel angles.

Unlike mesh-based rendering with `ModelComponent`, a `GaussianSplatComponent` doesn’t use developer-visible shaders. Instead, the framework renders each splat as an ellipsoid during the transparency render pass, blending splats back-to-front according to the resource’s sorting mode.

> ❗ **Important**: Scene lighting doesn’t affect a Gaussian splat asset. The color of the rendered output reflects the lighting conditions present during the original capture.

#### Providing Splat Data

You supply splat data to the component through a [`GaussianSplatResource`](gaussiansplatresource.md). Initially, the only supported resource type is a [`GaussianSplatResource.BufferResource`](gaussiansplatresource/bufferresource-swift.struct.md). A buffer resource describes per-splat properties stored in one or more `LowLevelBuffer` instances. Each property is described using a [`GaussianSplatResource.BufferDescriptor`](gaussiansplatresource/bufferdescriptor.md) that specifies the low level buffer, data format, byte offset, and stride.

A single splat requires the following properties:

| Property | Values | Format |
| --- | --- | --- |
| Position | x, y, z | 3 floats |
| Scale | x, y, z | 3 floats |
| Rotation | r, x, y, z (quaternion) | 4 floats |
| Opacity | single value | 1 float |
| Spherical harmonics | varies by degree | 3+ floats |

Using half instead of float is also supported.

You can lay out these properties as interleaved data in a single buffer (array of structs) or use separate buffers for each property (struct of arrays). The framework doesn’t load files directly, so you parse your source format — PLY, USD, or any other container — and populate the buffers yourself.

#### Creating a Splat Entity

The following example reads splat data from a PLY file, populates a buffer resource, and adds the component to the scene:

```swift
// Parse your splat source data.
let bunny: PlyData = readDataFromPLY("bunny.ply")

// Allocate a LowLevelBuffer with your interleaved splat data.
let floatSize = MemoryLayout<Float>.size
let stride = 15 * floatSize

var buffer = try LowLevelBuffer(descriptor: .init(capacity: ((bunny.data.length + 15) & ~0xF), sizeMultiple: 16))
buffer.withUnsafeMutableBytes { ptr in
    ptr.copyBytes(from: bunny.bytes, count: bunny.data.length)
}

// Describe each property's location within the buffer.
let position = GaussianSplatResource.BufferDescriptor(
    buffer: buffer, format: .float3, stride: stride, offset: 0)
let scale = GaussianSplatResource.BufferDescriptor(
    buffer: buffer, format: .float3, stride: stride, offset: floatSize * 3)
let rotation = GaussianSplatResource.BufferDescriptor(
    buffer: buffer, format: .float4, stride: stride, offset: floatSize * 6)
let opacity = GaussianSplatResource.BufferDescriptor(
    buffer: buffer, format: .float, stride: stride, offset: floatSize * 10)
let sh = GaussianSplatResource.BufferDescriptor(
    buffer: buffer, format: .float3, stride: stride, offset: floatSize * 11)

// Create the buffer resource and wrap it in a GaussianSplatResource.
let bufferResource = try GaussianSplatResource.BufferResource(
    count: bunny.count,
    position: position,
    scale: scale,
    rotation: rotation,
    opacity: opacity,
    sphericalHarmonics: (sh, .zero)
)
let resource = GaussianSplatResource(bufferResource)

// Attach the component to an entity.
let splatEntity = Entity()
let component = GaussianSplatComponent(resource)
splatEntity.components.set(component)
```

#### Grounding Shadows

If the entity also contains a `GroundingShadowComponent`, the framework generates an approximate grounding shadow using a spherical proxy mesh. This provides visual grounding in the scene but is only an approximate shape, based on the bounds of the point cloud data.

#### Performance Considerations

Rendering cost correlates with splat count and overdraw. The framework enforces an internal limit on the total number of splats, and the BufferResource initializer will throw, if exceeded. To address this, you can:

- Reduce splat count through pruning during the training pipeline.
- Minimize overdraw by culling low-opacity splats before providing data to the component.

## Topics

### Structures
- [GaussianSplatResource.BufferDescriptor](gaussiansplatresource/bufferdescriptor.md)
  The buffer descriptor specifies the details for each part of a BufferResource. The stride and offset should be expressed in bytes.
- [GaussianSplatResource.BufferResource](gaussiansplatresource/bufferresource-swift.struct.md)
  Use a BufferResource to provide your 3DGS data for rendering. Each aspect of the data is expressed using a BufferDescriptor. The data may all come from the same LowLevelBuffer with different offsets, or separate LowLevelBuffers for each descriptor.
### Initializers
- [init(GaussianSplatResource.BufferResource)](gaussiansplatresource/init(_:).md)
### Instance Properties
- [let bufferResource: GaussianSplatResource.BufferResource?](gaussiansplatresource/bufferresource-swift.property.md)
- [var colorSpace: CGColorSpace](gaussiansplatresource/colorspace.md)
- [var opacityActivation: GaussianSplatResource.ActivationFunction](gaussiansplatresource/opacityactivation.md)
- [var projectionMode: GaussianSplatResource.ProjectionMode](gaussiansplatresource/projectionmode-swift.property.md)
- [var scaleActivation: GaussianSplatResource.ActivationFunction](gaussiansplatresource/scaleactivation.md)
- [var sortingMode: GaussianSplatResource.SortingMode](gaussiansplatresource/sortingmode-swift.property.md)
### Enumerations
- [GaussianSplatResource.ActivationFunction](gaussiansplatresource/activationfunction.md)
  Raw scale and opacity values from a trained Gaussian splat model often need a mathematical transformation before rendering. The [`GaussianSplatResource.ActivationFunction`](gaussiansplatresource/activationfunction.md) enumeration defines these transformations:
- [GaussianSplatResource.ProjectionMode](gaussiansplatresource/projectionmode-swift.enum.md)
  Controls how 2D splat footprints are computed from 3D Gaussian primitives:
- [GaussianSplatResource.SortingMode](gaussiansplatresource/sortingmode-swift.enum.md)
  Correct blending of splat opacity requires rendering them in a specific order. You may sort by:
- [GaussianSplatResource.SphericalHarmonicDegree](gaussiansplatresource/sphericalharmonicdegree.md)
  Spherical harmonic (SH) coefficients encode view-dependent color information. Higher degrees produce higher frequency variance at the cost of additional data per splat:


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/gaussiansplatresource)*