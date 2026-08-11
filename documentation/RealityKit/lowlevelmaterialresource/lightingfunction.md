# LowLevelMaterialResource.LightingFunction

**Framework**: RealityKit  
**Kind**: class

A compiled Metal function that evaluates lighting.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class LightingFunction
```

#### Overview

Create a `LightingFunction` through a context’s [`lighting`](lowlevelrendercontext/lighting.md) provider, using [`makeImageBasedLightingFunction()`](lowlevelrendercontextlighting/makeimagebasedlightingfunction().md) for image-based lighting or [`makeUnlitLightingFunction()`](lowlevelrendercontextlighting/makeunlitlightingfunction().md) for unlit shading.

## Topics

### Configuring shader arguments
- [var parameterMapping: LowLevelMaterialParameterMapping?](lowlevelmaterialresource/lightingfunction/parametermapping.md)
  The parameter name-to-slot mapping for this lighting function, or `nil` if it takes no custom parameters.
- [var argumentTableDescriptor: LowLevelArgumentTable.Descriptor?](lowlevelmaterialresource/lightingfunction/argumenttabledescriptor.md)
  The argument table descriptor for this lighting function, or `nil` if it takes no per-draw arguments.

## Relationships

### Conforms To
- [LowLevelMaterialResource.Function](lowlevelmaterialresource/function.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var surface: LowLevelMaterialResource.SurfaceShader](lowlevelmaterialresource/surface.md)
  The compiled fragment-stage surface shader.
- [LowLevelMaterialResource.SurfaceShader](lowlevelmaterialresource/surfaceshader.md)
  A compiled Metal function that implements the surface shader function.
- [var geometry: LowLevelMaterialResource.GeometryModifier](lowlevelmaterialresource/geometry.md)
  The compiled vertex-stage geometry modifier.
- [LowLevelMaterialResource.GeometryModifier](lowlevelmaterialresource/geometrymodifier.md)
  A compiled Metal function that implements the geometry modifier function.
- [LowLevelMaterialResource.Function](lowlevelmaterialresource/function.md)
  A compiled shader function that can receive per-draw parameters via an argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialresource/lightingfunction)*