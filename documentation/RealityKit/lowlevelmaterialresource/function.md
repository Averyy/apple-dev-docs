# LowLevelMaterialResource.Function

**Framework**: RealityKit  
**Kind**: protocol

A compiled shader function that can receive per-draw parameters via an argument table.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol Function : Sendable
```

## Topics

### Configuring the function
- [var parameterMapping: LowLevelMaterialParameterMapping?](lowlevelmaterialresource/function/parametermapping.md)
  The parameter name-to-slot mapping for this function, used to look up binding indices by name at runtime, or `nil` if the function takes no custom parameters.
- [var argumentTableDescriptor: LowLevelArgumentTable.Descriptor?](lowlevelmaterialresource/function/argumenttabledescriptor.md)
  The argument table descriptor that describes the buffer and texture slots this function requires, or `nil` if the function takes no per-draw arguments.

## Relationships

### Inherits From
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
### Conforming Types
- [LowLevelMaterialResource.GeometryModifier](lowlevelmaterialresource/geometrymodifier.md)
- [LowLevelMaterialResource.LightingFunction](lowlevelmaterialresource/lightingfunction.md)
- [LowLevelMaterialResource.SurfaceShader](lowlevelmaterialresource/surfaceshader.md)

## See Also

- [var surface: LowLevelMaterialResource.SurfaceShader](lowlevelmaterialresource/surface.md)
  The compiled fragment-stage surface shader.
- [LowLevelMaterialResource.SurfaceShader](lowlevelmaterialresource/surfaceshader.md)
  A compiled Metal function that implements the surface shader function.
- [var geometry: LowLevelMaterialResource.GeometryModifier](lowlevelmaterialresource/geometry.md)
  The compiled vertex-stage geometry modifier.
- [LowLevelMaterialResource.GeometryModifier](lowlevelmaterialresource/geometrymodifier.md)
  A compiled Metal function that implements the geometry modifier function.
- [LowLevelMaterialResource.LightingFunction](lowlevelmaterialresource/lightingfunction.md)
  A compiled Metal function that evaluates lighting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialresource/function)*