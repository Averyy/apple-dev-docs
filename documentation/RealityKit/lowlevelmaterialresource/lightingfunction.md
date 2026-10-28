# LowLevelMaterialResource.LightingFunction

**Framework**: RealityKit  
**Kind**: class  
**Role**: Class

A compiled Metal function that evaluates lighting.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final class LightingFunction
```

## Overview

Create a `LightingFunction` through a context’s [`lighting`](../lowlevelrendercontext/lighting.md) provider, using [`makeImageBasedLightingFunction()`](../lowlevelrendercontextlighting/makeimagebasedlightingfunction%28%29.md) for image-based lighting or [`makeUnlitLightingFunction()`](../lowlevelrendercontextlighting/makeunlitlightingfunction%28%29.md) for unlit shading.

## Topics

### Configuring shader arguments
- [var parameterMapping: LowLevelMaterialParameterMapping?](./lightingfunction/parametermapping.md)
  The parameter name-to-slot mapping for this lighting function, or `nil` if it takes no custom parameters.
- [var argumentTableDescriptor: LowLevelArgumentTable.Descriptor?](./lightingfunction/argumenttabledescriptor.md)
  The argument table descriptor for this lighting function, or `nil` if it takes no per-draw arguments.

## Relationships

### Conforms To
- [LowLevelMaterialResource.Function](./function.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [LowLevelMaterialResource.Function](./function.md)
  A compiled shader function that can receive per-draw parameters via an argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialresource/lightingfunction)*