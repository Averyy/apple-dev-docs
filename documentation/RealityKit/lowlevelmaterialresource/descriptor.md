# LowLevelMaterialResource.Descriptor

**Framework**: RealityKit  
**Kind**: struct

The geometry modifier, surface shader, and lighting function for a material.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Descriptor
```

## Topics

### Creating a descriptor
- [init(geometry: LowLevelMaterialResource.GeometryModifier, surface: LowLevelMaterialResource.SurfaceShader, lighting: LowLevelMaterialResource.LightingFunction)](lowlevelmaterialresource/descriptor/init(geometry:surface:lighting:).md)
  Creates a descriptor from the three shader stages.
### Configuring the shaders
- [var surface: LowLevelMaterialResource.SurfaceShader](lowlevelmaterialresource/descriptor/surface.md)
  The fragment-stage surface shader.
- [var geometry: LowLevelMaterialResource.GeometryModifier](lowlevelmaterialresource/descriptor/geometry.md)
  The vertex-stage geometry modifier.
### Instance Properties
- [var lighting: LowLevelMaterialResource.LightingFunction](lowlevelmaterialresource/descriptor/lighting.md)
  The lighting evaluation function.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [LowLevelMaterialResource.SimpleSurfaceDescriptor](lowlevelmaterialresource/simplesurfacedescriptor.md)
  The configuration for a built-in surface shader that applies a tint color, a texture, or both.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialresource/descriptor)*