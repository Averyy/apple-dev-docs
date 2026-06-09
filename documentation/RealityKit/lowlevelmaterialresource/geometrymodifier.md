# LowLevelMaterialResource.GeometryModifier

**Framework**: RealityKit  
**Kind**: class

A compiled Metal function that implements the vertex geometry modifier stage.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class GeometryModifier
```

## Topics

### Creating a geometry modifier
- [LowLevelMaterialResource.GeometryModifier.Descriptor](lowlevelmaterialresource/geometrymodifier/descriptor.md)
  The name and library for a user-authored Metal geometry modifier function.
### Configuring arguments and parameters
- [var argumentTableDescriptor: LowLevelArgumentTable.Descriptor?](lowlevelmaterialresource/geometrymodifier/argumenttabledescriptor.md)
  The argument table descriptor for this geometry modifier, or `nil` if it takes no per-draw arguments.
- [var parameterMapping: LowLevelMaterialParameterMapping?](lowlevelmaterialresource/geometrymodifier/parametermapping.md)
  The parameter name-to-slot mapping for this geometry modifier.

## Relationships

### Conforms To
- [LowLevelMaterialResource.Function](lowlevelmaterialresource/function.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var surface: LowLevelMaterialResource.SurfaceShader](lowlevelmaterialresource/surface.md)
  The compiled fragment-stage surface shader.
- [LowLevelMaterialResource.SurfaceShader](lowlevelmaterialresource/surfaceshader.md)
  A compiled Metal function that implements the fragment surface shader stage.
- [var geometry: LowLevelMaterialResource.GeometryModifier](lowlevelmaterialresource/geometry.md)
  The compiled vertex-stage geometry modifier.
- [LowLevelMaterialResource.LightingFunction](lowlevelmaterialresource/lightingfunction.md)
  A compiled function that evaluates lighting for a surface shader stage.
- [LowLevelMaterialResource.Function](lowlevelmaterialresource/function.md)
  A compiled shader stage function that can receive per-draw parameters via an argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialresource/geometrymodifier)*