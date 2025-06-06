# generateSphericalHarmonics(fromIrradiance:)

**Framework**: Model I/O  
**Kind**: method

Generates spherical harmonics information based on the light probe’s irradiance texture.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func generateSphericalHarmonics(fromIrradiance sphericalHarmonicsLevel: Int)
```

#### Discussion

Spherical harmonic coefficients describe the distribution of light around a light source with less high-frequency detail than a cube map texture, but they can be used more efficiently in real-time rendering. After calling this method, use the [`sphericalHarmonicsCoefficients`](mdllightprobe/sphericalharmonicscoefficients.md) property to access the generated coefficients.

## Parameters

- `sphericalHarmonicsLevel`: The number of levels for which to generate spherical harmonics. Each level of spherical harmonics contains more coefficients, affecting both the layout of the resulting data and the detail of any lighting effects based on it.

## See Also

- [var sphericalHarmonicsCoefficients: Data?](mdllightprobe/sphericalharmonicscoefficients.md)
  Data containing the spherical harmonics coefficients for the light.
- [var sphericalHarmonicsLevel: Int](mdllightprobe/sphericalharmonicslevel.md)
  The number of levels of spherical harmonics information in the light probe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdllightprobe/generatesphericalharmonics(fromirradiance:))*