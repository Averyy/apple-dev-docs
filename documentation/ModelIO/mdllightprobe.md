# MDLLightProbe

**Framework**: Model I/O  
**Kind**: class

A light source described in terms of the variations in color and intensity of its illumination in all directions.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLLightProbe
```

#### Overview

A light probe represents this variation either as a cube map texture or as a set of spherical harmonic coefficients. In addition to describing such light sources, the [`MDLLightProbe`](mdllightprobe.md) class provides methods for generating light probe textures based on the contents of a scene and for generating spherical harmonic coefficients from a texture.

A light probe consists of two cube map textures, where each texel represents the color and intensity of light in a particular direction from the cube’s center:

- The [`reflectiveTexture`](mdllightprobe/reflectivetexture.md) cube map, also known as an , contains a rendering of a scene as viewed from the light probe’s position. A renderer can use this texture to create reflections on surfaces with metallic materials.
- The [`irradianceTexture`](mdllightprobe/irradiancetexture.md) cube map contains samples of the total light arriving at the light probe’s position from every direction. A renderer can use this texture to create diffuse lighting effects. You can derive an irradiance map from an environment map with methods on the [`MDLTexture`](mdltexture.md) class, or when creating a light probe with the [`init(textureSize:forLocation:lightsToConsider:objectsToConsider:reflectiveCubemap:irradianceCubemap:)`](mdllightprobe/init(texturesize:forlocation:lightstoconsider:objectstoconsider:reflectivecubemap:irradiancecubemap:).md) method.

Using cube map textures for light-probe-based rendering offers great visual fidelity, but adversely affects performance due to the cost of texture lookups during rendering. In addition, a cube map texture often contains more detail than is necessary for lighting. A set of spherical harmonic coefficients can represent the same information with less detail, and can be used in shader calculations with much less performance cost. To use spherical harmonics, call the [`generateSphericalHarmonics(fromIrradiance:)`](mdllightprobe/generatesphericalharmonics(fromirradiance:).md) method, then access the generated data in the [`sphericalHarmonicsCoefficients`](mdllightprobe/sphericalharmonicscoefficients.md) property.

## Topics

### Creating a Light Probe
- [init(reflectiveTexture: MDLTexture?, irradianceTexture: MDLTexture?)](mdllightprobe/init(reflectivetexture:irradiancetexture:).md)
  Initializes a light probe with the specified cube map textures.
### Working with Textures
- [var reflectiveTexture: MDLTexture?](mdllightprobe/reflectivetexture.md)
  A cube map texture that contains a rendering of a scene as seen from the light probe’s position.
- [var irradianceTexture: MDLTexture?](mdllightprobe/irradiancetexture.md)
  A cube map texture that contains samples of the total light arriving at the light probe’s position from every direction.
### Working with Spherical Harmonics
- [func generateSphericalHarmonics(fromIrradiance: Int)](mdllightprobe/generatesphericalharmonics(fromirradiance:).md)
  Generates spherical harmonics information based on the light probe’s irradiance texture.
- [var sphericalHarmonicsCoefficients: Data?](mdllightprobe/sphericalharmonicscoefficients.md)
  Data containing the spherical harmonics coefficients for the light.
- [var sphericalHarmonicsLevel: Int](mdllightprobe/sphericalharmonicslevel.md)
  The number of levels of spherical harmonics information in the light probe.
### Generating Light Probes from Scene Contents
- [init?(textureSize: Int, forLocation: MDLTransform, lightsToConsider: [MDLLight], objectsToConsider: [MDLObject], reflectiveCubemap: MDLTexture?, irradianceCubemap: MDLTexture?)](mdllightprobe/init(texturesize:forlocation:lightstoconsider:objectstoconsider:reflectivecubemap:irradiancecubemap:).md)
  Creates a light probe representing the shading environment at a specific point in a scene.

## Relationships

### Inherits From
- [MDLLight](mdllight.md)
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
- [protocol MDLLightProbeIrradianceDataSource](mdllightprobeirradiancedatasource.md)
  Adopt this protocol to provide information for use in automatic placement of light probes around a scene.
- [class MDLPhotometricLight](mdlphotometriclight.md)
  A light source whose shape, direction, and intensity of illumination are determined by a photometric profile.
- [class MDLPhysicallyPlausibleLight](mdlphysicallyplausiblelight.md)
  A light source for use in shading models based on real-world physics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdllightprobe)*