# GaussianSplatResource.BufferResource

**Framework**: RealityKit  
**Kind**: struct

A set of buffer descriptors that supplies the per-splat data for rendering.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct BufferResource
```

#### Overview

The descriptors can share one buffer at different offsets, or use a separate buffer for each property.

## Topics

### Initializers
- [init(count: Int, position: GaussianSplatResource.BufferDescriptor, scale: GaussianSplatResource.BufferDescriptor, rotation: GaussianSplatResource.BufferDescriptor, opacity: GaussianSplatResource.BufferDescriptor, sphericalHarmonics: (GaussianSplatResource.BufferDescriptor, GaussianSplatResource.SphericalHarmonicDegree)) throws](gaussiansplatresource/bufferresource-swift.struct/init(count:position:scale:rotation:opacity:sphericalharmonics:).md)
  Creates a buffer resource from descriptors for each per-splat property.
### Instance Properties
- [let count: Int](gaussiansplatresource/bufferresource-swift.struct/count.md)
  The number of splats the resource renders.
- [let degree: GaussianSplatResource.SphericalHarmonicDegree](gaussiansplatresource/bufferresource-swift.struct/degree.md)
  The amount of view-dependent color detail stored per splat.
- [let opacity: GaussianSplatResource.BufferDescriptor](gaussiansplatresource/bufferresource-swift.struct/opacity.md)
  The descriptor for each splat’s opacity, stored as a single float.
- [let position: GaussianSplatResource.BufferDescriptor](gaussiansplatresource/bufferresource-swift.struct/position.md)
  The descriptor for each splat’s position, stored as three floats.
- [let rotation: GaussianSplatResource.BufferDescriptor](gaussiansplatresource/bufferresource-swift.struct/rotation.md)
  The descriptor for each splat’s rotation, stored as a four-component quaternion.
- [let scale: GaussianSplatResource.BufferDescriptor](gaussiansplatresource/bufferresource-swift.struct/scale.md)
  The descriptor for each splat’s scale, stored as three floats.
- [let sphericalHarmonics: GaussianSplatResource.BufferDescriptor](gaussiansplatresource/bufferresource-swift.struct/sphericalharmonics.md)
  The descriptor for each splat’s spherical harmonic color coefficients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/gaussiansplatresource/bufferresource-swift.struct)*