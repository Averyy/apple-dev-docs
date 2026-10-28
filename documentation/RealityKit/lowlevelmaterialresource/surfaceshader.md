# LowLevelMaterialResource.SurfaceShader

**Framework**: RealityKit  
**Kind**: class  
**Role**: Class

A compiled Metal function that implements the surface shader function.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final class SurfaceShader
```

## Overview

Create a `SurfaceShader` by compiling a [`LowLevelMaterialResource.SurfaceShader.Descriptor`](./surfaceshader/descriptor.md) with [`makeSurfaceShader(descriptor:)`](../lowlevelrendercontext/makesurfaceshader%28descriptor%29-66tq8.md), or use [`makeSimpleSurfaceShader(descriptor:)`](../lowlevelrendercontext/makesimplesurfaceshader%28descriptor%29-74vhb.md) for the built-in simple surface shader function.

## Topics

### Describing the shader
- [LowLevelMaterialResource.SurfaceShader.Descriptor](./surfaceshader/descriptor.md)
  The name and library for a user-authored Metal surface shader function.
### Configuring shader parameters
- [var parameterMapping: LowLevelMaterialParameterMapping?](./surfaceshader/parametermapping.md)
  The parameter name-to-slot mapping for this surface shader function, or `nil` if it takes no custom parameters.
- [var argumentTableDescriptor: LowLevelArgumentTable.Descriptor?](./surfaceshader/argumenttabledescriptor.md)
  The argument table descriptor for this surface shader, or `nil` if it takes no per-draw arguments.

## Relationships

### Conforms To
- [LowLevelMaterialResource.Function](./function.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the shaders
- [var surface: LowLevelMaterialResource.SurfaceShader](./surface.md)
  The compiled fragment-stage surface shader.
- [var geometry: LowLevelMaterialResource.GeometryModifier](./geometry.md)
  The compiled vertex-stage geometry modifier.
- [LowLevelMaterialResource.GeometryModifier](./geometrymodifier.md)
  A compiled Metal function that implements the geometry modifier function.
- [LowLevelMaterialResource.LightingFunction](./lightingfunction.md)
  A compiled Metal function that evaluates lighting.
- [LowLevelMaterialResource.Function](./function.md)
  A compiled shader function that can receive per-draw parameters via an argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialresource/surfaceshader)*