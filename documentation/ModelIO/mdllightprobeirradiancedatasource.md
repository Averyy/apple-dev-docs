# MDLLightProbeIrradianceDataSource

**Framework**: Model I/O  
**Kind**: protocol

Adopt this protocol to provide information for use in automatic placement of light probes around a scene.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
protocol MDLLightProbeIrradianceDataSource : NSObjectProtocol
```

#### Overview

The [`MDLAsset`](mdlasset.md) [`placeLightProbes(withDensity:heuristic:using:)`](mdlasset/placelightprobes(withdensity:heuristic:using:).md) method automatically creates [`MDLLightProbe`](mdllightprobe.md) objects, setting their positions and lighting parameters to provide optimal light probe coverage within a scene you define. When you use that method, you must provide an object implementing this protocol, which Model I/O queries in order to evaluate your scene.

## Topics

### Providing Light Probe Information
- [var boundingBox: MDLAxisAlignedBoundingBox](mdllightprobeirradiancedatasource/boundingbox.md)
  The bounding region of the scene to which light probes are being added.
- [var sphericalHarmonicsLevel: Int](mdllightprobeirradiancedatasource/sphericalharmonicslevel.md)
  The number of levels of spherical harmonics information provided by the data source.
- [func sphericalHarmonicsCoefficients(atPosition: vector_float3) -> Data](mdllightprobeirradiancedatasource/sphericalharmonicscoefficients(atposition:).md)
  Asks the data source to provide spherical harmonics coefficients that describe lighting conditions in all directions from the specified point in a scene.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MDLLight](mdllight.md)
  The abstract superclass for objects that describe light sources in a scene.
- [class MDLAreaLight](mdlarealight.md)
  A light source that illuminates a 3D scene from an area with a specific shape.
- [class MDLLightProbe](mdllightprobe.md)
  A light source described in terms of the variations in color and intensity of its illumination in all directions.
- [class MDLPhotometricLight](mdlphotometriclight.md)
  A light source whose shape, direction, and intensity of illumination are determined by a photometric profile.
- [class MDLPhysicallyPlausibleLight](mdlphysicallyplausiblelight.md)
  A light source for use in shading models based on real-world physics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdllightprobeirradiancedatasource)*