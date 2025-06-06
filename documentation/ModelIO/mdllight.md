# MDLLight

**Framework**: Model I/O  
**Kind**: class

The abstract superclass for objects that describe light sources in a scene.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLLight
```

#### Overview

When you load lights from an asset file using the [`MDLAsset`](mdlasset.md) class or create lights when building an asset for export, you use one or more of the concrete subclasses [`MDLPhysicallyPlausibleLight`](mdlphysicallyplausiblelight.md), [`MDLAreaLight`](mdlarealight.md), [`MDLPhotometricLight`](mdlphotometriclight.md), or [`MDLLightProbe`](mdllightprobe.md).

## Topics

### Working with Lights
- [func irradiance(atPoint: vector_float3) -> Unmanaged<CGColor>](mdllight/irradiance(atpoint:).md)
  Returns the radiance of the light as received at a specific point in the same scene.
- [func irradiance(atPoint: vector_float3, colorSpace: CGColorSpace) -> Unmanaged<CGColor>](mdllight/irradiance(atpoint:colorspace:).md)
  Returns the radiance of the light as received at a specific point in the same scene, expressed using the specified color space.
- [var lightType: MDLLightType](mdllight/lighttype.md)
  The type of the light.
- [var colorSpace: String](mdllight/colorspace.md)
  The name of the Core Graphics color space to be used for interpreting the light’s color information.
### Constants
- [enum MDLLightType](mdllighttype.md)
  Options for the shape and style of illumination provided by a light, used by the [`lightType`](mdllight/lighttype.md) property.

## Relationships

### Inherits From
- [MDLObject](mdlobject.md)
### Inherited By
- [MDLLightProbe](mdllightprobe.md)
- [MDLPhysicallyPlausibleLight](mdlphysicallyplausiblelight.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MDLNamed](mdlnamed.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MDLAreaLight](mdlarealight.md)
  A light source that illuminates a 3D scene from an area with a specific shape.
- [class MDLLightProbe](mdllightprobe.md)
  A light source described in terms of the variations in color and intensity of its illumination in all directions.
- [protocol MDLLightProbeIrradianceDataSource](mdllightprobeirradiancedatasource.md)
  Adopt this protocol to provide information for use in automatic placement of light probes around a scene.
- [class MDLPhotometricLight](mdlphotometriclight.md)
  A light source whose shape, direction, and intensity of illumination are determined by a photometric profile.
- [class MDLPhysicallyPlausibleLight](mdlphysicallyplausiblelight.md)
  A light source for use in shading models based on real-world physics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdllight)*