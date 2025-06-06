# MDLPhysicallyPlausibleLight

**Framework**: Model I/O  
**Kind**: class

A light source for use in shading models based on real-world physics.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLPhysicallyPlausibleLight
```

## Topics

### Managing Light Color and Intensity
- [var color: CGColor?](mdlphysicallyplausiblelight/color.md)
  The color of the light source.
- [var lumens: Float](mdlphysicallyplausiblelight/lumens.md)
  The total visible intensity of the light source, in lumens.
- [func setColorByTemperature(Float)](mdlphysicallyplausiblelight/setcolorbytemperature(_:).md)
  Sets the light’s color based on a black-body temperature.
### Managing Light Geometry
- [var innerConeAngle: Float](mdlphysicallyplausiblelight/innerconeangle.md)
  The radial angle, in degrees, of the area fully illuminated by the light.
- [var outerConeAngle: Float](mdlphysicallyplausiblelight/outerconeangle.md)
  The radial angle, in degrees, at which the illumination from a spotlight becomes zero.
### Managing Attenuation
- [var attenuationStartDistance: Float](mdlphysicallyplausiblelight/attenuationstartdistance.md)
  The distance from the light source, in units of local coordinate space, at which its illumination begins to diminish.
- [var attenuationEndDistance: Float](mdlphysicallyplausiblelight/attenuationenddistance.md)
  The distance from the light source, in units of local coordinate space, at which its illumination becomes zero.

## Relationships

### Inherits From
- [MDLLight](mdllight.md)
### Inherited By
- [MDLAreaLight](mdlarealight.md)
- [MDLPhotometricLight](mdlphotometriclight.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MDLNamed](mdlnamed.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MDLLight](mdllight.md)
  The abstract superclass for objects that describe light sources in a scene.
- [class MDLAreaLight](mdlarealight.md)
  A light source that illuminates a 3D scene from an area with a specific shape.
- [class MDLLightProbe](mdllightprobe.md)
  A light source described in terms of the variations in color and intensity of its illumination in all directions.
- [protocol MDLLightProbeIrradianceDataSource](mdllightprobeirradiancedatasource.md)
  Adopt this protocol to provide information for use in automatic placement of light probes around a scene.
- [class MDLPhotometricLight](mdlphotometriclight.md)
  A light source whose shape, direction, and intensity of illumination are determined by a photometric profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlphysicallyplausiblelight)*