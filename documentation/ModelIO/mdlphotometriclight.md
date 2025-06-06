# MDLPhotometricLight

**Framework**: Model I/O  
**Kind**: class

A light source whose shape, direction, and intensity of illumination are determined by a photometric profile.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MDLPhotometricLight
```

#### Overview

You create a photometric light from a file in the IES format, containing physical measurements of a light source. Many manufacturers of real-world light fixtures publish such files describing the lighting characteristics of their products. This photometry data measures the light web surrounding a light source—measurements of the light’s intensity in all directions around the source.The [`MDLPhotometricLight`](mdlphotometriclight.md) provides two ways to interpret a light web:

- As a cube map texture. Use the [`generateCubemap(fromLight:)`](mdlphotometriclight/generatecubemap(fromlight:).md) method to generate a texture, then use the [`lightCubeMap`](mdlphotometriclight/lightcubemap.md) property to access the texture. In this texture, each texel represents the light’s intensity in the direction from the cube’s center to the texel’s position on the cube.
-  Use the [`generateSphericalHarmonics(fromLight:)`](mdlphotometriclight/generatesphericalharmonics(fromlight:).md) method to generate a set of spherical harmonic coefficients, and then use the [`sphericalHarmonicsLevel`](mdlphotometriclight/sphericalharmonicslevel.md) and [`sphericalHarmonicsCoefficients`](mdlphotometriclight/sphericalharmonicscoefficients.md) properties to access these coefficients. Spherical harmonic coefficients provide a more compact representation of the same information as the cube map texture, so you can use them during shading without the performance cost of a texture lookup.

Both the [`MDLPhotometricLight`](mdlphotometriclight.md) and [`MDLAreaLight`](mdlarealight.md) classes can describe lights with interesting shapes—an area light offers a simpler design that can be implemented with better rendering performance, and a photometric light offers design that better models real-world light fixtures at the cost of higher computational complexity.

## Topics

### Creating a Photometric Light
- [init?(iesProfile: URL)](mdlphotometriclight/init(iesprofile:).md)
  Initializes a light from photometry data in the file at the specified URL.
### Interpreting the Light Web as a Cube Texture
- [func generateCubemap(fromLight: Int)](mdlphotometriclight/generatecubemap(fromlight:).md)
  Generates a cube map texture from the light’s photometry data.
- [var lightCubeMap: MDLTexture?](mdlphotometriclight/lightcubemap.md)
  A cube map texture describing the light’s intensity in all directions.
### Interpreting the Light Web as Spherical Harmonics
- [func generateSphericalHarmonics(fromLight: Int)](mdlphotometriclight/generatesphericalharmonics(fromlight:).md)
  Generates spherical harmonics information based on the light’s photometry data.
- [var sphericalHarmonicsCoefficients: Data?](mdlphotometriclight/sphericalharmonicscoefficients.md)
  Data containing spherical harmonics coefficients that describe the light’s intensity in all directions.
- [var sphericalHarmonicsLevel: Int](mdlphotometriclight/sphericalharmonicslevel.md)
  The number of levels of generated spherical harmonics information.
### Instance Methods
- [func generateTexture(Int) -> MDLTexture](mdlphotometriclight/generatetexture(_:).md)

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
- [class MDLAreaLight](mdlarealight.md)
  A light source that illuminates a 3D scene from an area with a specific shape.
- [class MDLLightProbe](mdllightprobe.md)
  A light source described in terms of the variations in color and intensity of its illumination in all directions.
- [protocol MDLLightProbeIrradianceDataSource](mdllightprobeirradiancedatasource.md)
  Adopt this protocol to provide information for use in automatic placement of light probes around a scene.
- [class MDLPhysicallyPlausibleLight](mdlphysicallyplausiblelight.md)
  A light source for use in shading models based on real-world physics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlphotometriclight)*