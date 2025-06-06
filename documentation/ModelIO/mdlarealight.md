# MDLAreaLight

**Framework**: Model I/O  
**Kind**: class

A light source that illuminates a 3D scene from an area with a specific shape.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLAreaLight
```

#### Overview

Unlike other light sources that illuminate a scene from a single point or direction, an area light has a specific shape. The shape of an area light is a two-dimensional figure in the xy-plane of the light’s local coordinate space, and its illumination is directed in the negative z-axis direction (spreading out from that direction according to the inherited [`innerConeAngle`](mdlphysicallyplausiblelight/innerconeangle.md) and [`outerConeAngle`](mdlphysicallyplausiblelight/outerconeangle.md) properties).

Both the [`MDLAreaLight`](mdlarealight.md) and [`MDLPhotometricLight`](mdlphotometriclight.md) classes can describe lights with interesting shapes. An area light offers a simpler design that can be implemented with better rendering performance, and a photometric light offers design that better models real-world light fixtures at the cost of higher computational complexity.

## Topics

### Managing a Light’s Shape
- [var areaRadius: Float](mdlarealight/arearadius.md)
  The radius, in units of local coordinate space, of the area from which light emanates.
- [var aspect: Float](mdlarealight/aspect.md)
  The aspect ratio of the light’s shape.
- [var superEllipticPower: vector_float2](mdlarealight/superellipticpower.md)
  A vector that controls the roundness of a superelliptical light in the x- and y-axis directions.

## Relationships

### Inherits From
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

- [class MDLLight](mdllight.md)
  The abstract superclass for objects that describe light sources in a scene.
- [class MDLLightProbe](mdllightprobe.md)
  A light source described in terms of the variations in color and intensity of its illumination in all directions.
- [protocol MDLLightProbeIrradianceDataSource](mdllightprobeirradiancedatasource.md)
  Adopt this protocol to provide information for use in automatic placement of light probes around a scene.
- [class MDLPhotometricLight](mdlphotometriclight.md)
  A light source whose shape, direction, and intensity of illumination are determined by a photometric profile.
- [class MDLPhysicallyPlausibleLight](mdlphysicallyplausiblelight.md)
  A light source for use in shading models based on real-world physics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlarealight)*