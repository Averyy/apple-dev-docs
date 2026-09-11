# init(count:position:scale:rotation:opacity:sphericalHarmonics:)

**Framework**: RealityKit  
**Kind**: init

Creates a buffer resource from descriptors for each per-splat property.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@MainActor
init(count: Int, position: GaussianSplatResource.BufferDescriptor, scale: GaussianSplatResource.BufferDescriptor, rotation: GaussianSplatResource.BufferDescriptor, opacity: GaussianSplatResource.BufferDescriptor, sphericalHarmonics: (GaussianSplatResource.BufferDescriptor, GaussianSplatResource.SphericalHarmonicDegree)) throws
```

#### Discussion

> **Note**: An error if a descriptor is invalid or its buffer is too small for the splat count, or if the count exceeds the maximum the platform supports.

## Parameters

- `count`: The number of splats to render.
- `position`: The descriptor for each splat’s position.
- `scale`: The descriptor for each splat’s scale.
- `rotation`: The descriptor for each splat’s rotation.
- `opacity`: The descriptor for each splat’s opacity.
- `sphericalHarmonics`: The descriptor for each splat’s spherical harmonic coefficients, paired with the degree those coefficients represent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/gaussiansplatresource/bufferresource-swift.struct/init(count:position:scale:rotation:opacity:sphericalharmonics:))*