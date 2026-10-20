# LowLevelMaterialResource.Descriptor

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The geometry modifier, surface shader, and lighting function for a material.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Descriptor
```

## Topics

### Creating a descriptor
- [init(geometry: LowLevelMaterialResource.GeometryModifier, surface: LowLevelMaterialResource.SurfaceShader, lighting: LowLevelMaterialResource.LightingFunction)](./descriptor/init%28geometry,surface,lighting%29.md)
  Creates a descriptor from the three shader stages.
### Configuring the shaders
- [var surface: LowLevelMaterialResource.SurfaceShader](./descriptor/surface.md)
  The fragment-stage surface shader.
- [var geometry: LowLevelMaterialResource.GeometryModifier](./descriptor/geometry.md)
  The vertex-stage geometry modifier.
### Instance Properties
- [var lighting: LowLevelMaterialResource.LightingFunction](./descriptor/lighting.md)
  The lighting evaluation function.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Describing the material
- [LowLevelMaterialResource.SimpleSurfaceDescriptor](./simplesurfacedescriptor.md)
  The configuration for a built-in surface shader that applies a tint color, a texture, or both.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialresource/descriptor)*