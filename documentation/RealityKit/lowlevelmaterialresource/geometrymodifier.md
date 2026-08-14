# LowLevelMaterialResource.GeometryModifier

**Framework**: RealityKit  
**Kind**: class

A compiled Metal function that implements the geometry modifier function.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class GeometryModifier
```

#### Overview

Create a `GeometryModifier` by calling [`makeGeometryModifier(descriptor:)`](lowlevelrendercontext/makegeometrymodifier(descriptor:)-307ec.md), or use [`makeDefaultGeometryModifier()`](lowlevelrendercontext/makedefaultgeometrymodifier().md) for a pass-through modifier that performs no vertex transformation.

## Topics

### Creating a geometry modifier
- [LowLevelMaterialResource.GeometryModifier.Descriptor](lowlevelmaterialresource/geometrymodifier/descriptor.md)
  The name and library for a user-authored Metal geometry modifier function.
### Configuring arguments and parameters
- [var argumentTableDescriptor: LowLevelArgumentTable.Descriptor?](lowlevelmaterialresource/geometrymodifier/argumenttabledescriptor.md)
  The argument table descriptor for this geometry modifier, or `nil` if it takes no per-draw arguments.
- [var parameterMapping: LowLevelMaterialParameterMapping?](lowlevelmaterialresource/geometrymodifier/parametermapping.md)
  The parameter name-to-slot mapping for this geometry modifier, or `nil` if it takes no custom parameters.

## Relationships

### Conforms To
- [LowLevelMaterialResource.Function](lowlevelmaterialresource/function.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var surface: LowLevelMaterialResource.SurfaceShader](lowlevelmaterialresource/surface.md)
  The compiled fragment-stage surface shader.
- [LowLevelMaterialResource.SurfaceShader](lowlevelmaterialresource/surfaceshader.md)
  A compiled Metal function that implements the surface shader function.
- [var geometry: LowLevelMaterialResource.GeometryModifier](lowlevelmaterialresource/geometry.md)
  The compiled vertex-stage geometry modifier.
- [LowLevelMaterialResource.LightingFunction](lowlevelmaterialresource/lightingfunction.md)
  A compiled Metal function that evaluates lighting.
- [LowLevelMaterialResource.Function](lowlevelmaterialresource/function.md)
  A compiled shader function that can receive per-draw parameters via an argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmaterialresource/geometrymodifier)*