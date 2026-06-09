# LowLevelMaterialResource.SurfaceShader

**Framework**: RealityKit  
**Kind**: class

A compiled Metal function that implements the fragment surface shader stage.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class SurfaceShader
```

## Topics

### Describing the shader
- [LowLevelMaterialResource.SurfaceShader.Descriptor](lowlevelmaterialresource/surfaceshader/descriptor.md)
  The name and library for a user-authored Metal surface shader function.
### Configuring shader parameters
- [var parameterMapping: LowLevelMaterialParameterMapping?](lowlevelmaterialresource/surfaceshader/parametermapping.md)
  The parameter name-to-slot mapping for this surface shader.
- [var argumentTableDescriptor: LowLevelArgumentTable.Descriptor?](lowlevelmaterialresource/surfaceshader/argumenttabledescriptor.md)
  The argument table descriptor for this surface shader, or `nil` if it takes no per-draw arguments.

## Relationships

### Conforms To
- [LowLevelMaterialResource.Function](lowlevelmaterialresource/function.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var surface: LowLevelMaterialResource.SurfaceShader](lowlevelmaterialresource/surface.md)
  The compiled fragment-stage surface shader.
- [var geometry: LowLevelMaterialResource.GeometryModifier](lowlevelmaterialresource/geometry.md)
  The compiled vertex-stage geometry modifier.
- [LowLevelMaterialResource.GeometryModifier](lowlevelmaterialresource/geometrymodifier.md)
  A compiled Metal function that implements the vertex geometry modifier stage.
- [LowLevelMaterialResource.LightingFunction](lowlevelmaterialresource/lightingfunction.md)
  A compiled function that evaluates lighting for a surface shader stage.
- [LowLevelMaterialResource.Function](lowlevelmaterialresource/function.md)
  A compiled shader stage function that can receive per-draw parameters via an argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialresource/surfaceshader)*