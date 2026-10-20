# LowLevelMaterialResource.Function

**Framework**: RealityKit  
**Kind**: protocol  
**Role**: Protocol

A compiled shader function that can receive per-draw parameters via an argument table.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
protocol Function : Sendable
```

## Topics

### Configuring the function
- [var parameterMapping: LowLevelMaterialParameterMapping?](./function/parametermapping.md)
  The parameter name-to-slot mapping for this function, used to look up binding indices by name at runtime, or `nil` if the function takes no custom parameters.
- [var argumentTableDescriptor: LowLevelArgumentTable.Descriptor?](./function/argumenttabledescriptor.md)
  The argument table descriptor that describes the buffer and texture slots this function requires, or `nil` if the function takes no per-draw arguments.

## Relationships

### Inherits From
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
### Conforming Types
- [LowLevelMaterialResource.GeometryModifier](./geometrymodifier.md)
- [LowLevelMaterialResource.LightingFunction](./lightingfunction.md)
- [LowLevelMaterialResource.SurfaceShader](./surfaceshader.md)

## See Also

### Configuring the shaders
- [var surface: LowLevelMaterialResource.SurfaceShader](./surface.md)
  The compiled fragment-stage surface shader.
- [LowLevelMaterialResource.SurfaceShader](./surfaceshader.md)
  A compiled Metal function that implements the surface shader function.
- [var geometry: LowLevelMaterialResource.GeometryModifier](./geometry.md)
  The compiled vertex-stage geometry modifier.
- [LowLevelMaterialResource.GeometryModifier](./geometrymodifier.md)
  A compiled Metal function that implements the geometry modifier function.
- [LowLevelMaterialResource.LightingFunction](./lightingfunction.md)
  A compiled Metal function that evaluates lighting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialresource/function)*