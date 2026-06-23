# GaussianSplatResource.BufferResource

**Framework**: RealityKit  
**Kind**: struct

Use a BufferResource to provide your 3DGS data for rendering. Each aspect of the data is expressed using a BufferDescriptor. The data may all come from the same LowLevelBuffer with different offsets, or separate LowLevelBuffers for each descriptor.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct BufferResource
```

## Topics

### Initializers
- [init(count: Int, position: GaussianSplatResource.BufferDescriptor, scale: GaussianSplatResource.BufferDescriptor, rotation: GaussianSplatResource.BufferDescriptor, opacity: GaussianSplatResource.BufferDescriptor, sphericalHarmonics: (GaussianSplatResource.BufferDescriptor, GaussianSplatResource.SphericalHarmonicDegree)) throws](gaussiansplatresource/bufferresource-swift.struct/init(count:position:scale:rotation:opacity:sphericalharmonics:).md)
### Instance Properties
- [let count: Int](gaussiansplatresource/bufferresource-swift.struct/count.md)
- [let degree: GaussianSplatResource.SphericalHarmonicDegree](gaussiansplatresource/bufferresource-swift.struct/degree.md)
- [let opacity: GaussianSplatResource.BufferDescriptor](gaussiansplatresource/bufferresource-swift.struct/opacity.md)
- [let position: GaussianSplatResource.BufferDescriptor](gaussiansplatresource/bufferresource-swift.struct/position.md)
- [let rotation: GaussianSplatResource.BufferDescriptor](gaussiansplatresource/bufferresource-swift.struct/rotation.md)
- [let scale: GaussianSplatResource.BufferDescriptor](gaussiansplatresource/bufferresource-swift.struct/scale.md)
- [let sphericalHarmonics: GaussianSplatResource.BufferDescriptor](gaussiansplatresource/bufferresource-swift.struct/sphericalharmonics.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/gaussiansplatresource/bufferresource-swift.struct)*