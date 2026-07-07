# GaussianSplatComponent

**Framework**: RealityKit  
**Kind**: struct

A component that renders 3D Gaussian splat data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct GaussianSplatComponent
```

#### Overview

Use a Gaussian splat component to display volumetric imagery captured from real environments, coalesced into 3D Gaussian splats (3DGS). Gaussian splatting is a rendering technique that represents a scene as a collection of 3D Gaussian primitives, each with a position, scale, rotation, opacity, and color defined by spherical harmonic coefficients. The result is a high-fidelity reproduction of a captured scene that people can view from novel angles.

Unlike mesh-based rendering with `ModelComponent`, this component doesn’t use developer-visible shaders. Instead, the framework renders each splat as an ellipsoid during the transparency render pass, blending splats back-to-front according to the resource’s sorting mode.

> ❗ **Important**: Scene lighting doesn’t affect a Gaussian splat asset. The color of the rendered output reflects the lighting conditions present during the original capture.

Gaussian splats require a device with Apple7 GPU family support.

#### Providing Splat Data

You supply splat data to the component through a [`GaussianSplatResource`](gaussiansplatresource.md). Initially, the only supported resource type is a [`GaussianSplatResource.BufferResource`](gaussiansplatresource/bufferresource-swift.struct.md). A buffer resource describes per-splat properties stored in one or more `LowLevelBuffer` instances. A [`GaussianSplatResource.BufferDescriptor`](gaussiansplatresource/bufferdescriptor.md) specifies the low-level buffer, data format, byte offset, and stride for each property.

A single splat requires the following properties:

| Property | Values | Format |
| --- | --- | --- |
| Position | x, y, z | 3 floats |
| Scale | x, y, z | 3 floats |
| Rotation | r, x, y, z (quaternion) | 4 floats |
| Opacity | single value | 1 float |
| Spherical harmonics | varies by degree | 3+ floats |

You can also use half-precision values instead of floats.

You can lay out these properties as interleaved data in a single buffer (array of structs) or use separate buffers for each property (struct of arrays). The framework doesn’t load files directly, so you parse your source format — PLY, USD, or any other container — and populate the buffers yourself.

#### Creating a Splat Entity

The following example reads splat data from a PLY file, populates a buffer resource, and adds the component to an entity:

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

If the entity also contains a `GroundingShadowComponent`, the framework generates an approximate grounding shadow using a spherical proxy mesh. This provides visual grounding in the scene but is only an approximate shape, based on the bounds of the point-cloud data.

#### Performance Considerations

Rendering cost correlates with splat count and overdraw. The framework enforces an internal limit on the total number of splats, and the [`GaussianSplatResource.BufferResource`](gaussiansplatresource/bufferresource-swift.struct.md) initializer throws if you exceed it. To reduce cost, you can:

- Reduce splat count through pruning during the training pipeline.
- Minimize overdraw by culling low-opacity splats before you provide data to the component.

## Topics

### Initializers
- [init(GaussianSplatResource)](gaussiansplatcomponent/init(_:).md)
  Creates a component that displays a Gaussian splat resource.
### Instance Properties
- [var splatResource: GaussianSplatResource](gaussiansplatcomponent/splatresource.md)
  The splat data and rendering options the component displays.

## Relationships

### Conforms To
- [Component](component.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/gaussiansplatcomponent)*