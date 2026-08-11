# LowLevelMaterialResource.SurfaceShader

**Framework**: RealityKit  
**Kind**: class

A compiled Metal function that implements the surface shader function.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class SurfaceShader
```

#### Overview

Create a `SurfaceShader` by compiling a [`LowLevelMaterialResource.SurfaceShader.Descriptor`](lowlevelmaterialresource/surfaceshader/descriptor.md) with [`makeSurfaceShader(descriptor:)`](lowlevelrendercontext/makesurfaceshader(descriptor:)-66tq8.md), or use [`makeSimpleSurfaceShader(descriptor:)`](lowlevelrendercontext/makesimplesurfaceshader(descriptor:)-74vhb.md) for the built-in simple surface shader function.

## Topics

### Describing the shader
- [LowLevelMaterialResource.SurfaceShader.Descriptor](lowlevelmaterialresource/surfaceshader/descriptor.md)
  The name and library for a user-authored Metal surface shader function.
### Configuring shader parameters
- [var parameterMapping: LowLevelMaterialParameterMapping?](lowlevelmaterialresource/surfaceshader/parametermapping.md)
  The parameter name-to-slot mapping for this surface shader function, or `nil` if it takes no custom parameters.
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
  A compiled Metal function that implements the geometry modifier function.
- [LowLevelMaterialResource.LightingFunction](lowlevelmaterialresource/lightingfunction.md)
  A compiled Metal function that evaluates lighting.
- [LowLevelMaterialResource.Function](lowlevelmaterialresource/function.md)
  A compiled shader function that can receive per-draw parameters via an argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialresource/surfaceshader)*