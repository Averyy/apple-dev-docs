# sphericalHarmonicsCoefficients

**Framework**: Model I/O  
**Kind**: property

Data containing spherical harmonics coefficients that describe the light’s intensity in all directions.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var sphericalHarmonicsCoefficients: Data? { get }
```

#### Discussion

Spherical harmonic coefficients describe the distribution of light around a light source with less high-frequency detail than a cube map texture, but they can be used more efficiently in real-time rendering. Use the [`generateSphericalHarmonics(fromLight:)`](mdlphotometriclight/generatesphericalharmonics(fromlight:).md) method to create spherical harmonics data based on the light’s photometry data.

The data is an array of 32-bit floating-point values, containing three noninterleaved data sets corresponding to the red, green, and blue sets of coefficients. The array’s length is determined by the [`sphericalHarmonicsLevel`](mdlphotometriclight/sphericalharmonicslevel.md) property:

- At level 0, the array has 1 coefficient (3 values).
- At level 1, the array has 4 coefficients (3 sets of 4 values, 12 values total).
- At level 2, the array has 9 coefficients (3 sets of 9 values, 27 values total).
- At level 3, the array has 16 coefficients (3 sets of 16 values, 48 values total).
- Spherical harmonics levels beyond 3 are not supported.

For example, the code below shows how to access the second coefficient at level 2. (Note, however, that typically a renderer passes the entire data buffer to a GPU-based shader and uses equivalent shader code to extract individual coefficients.)

## See Also

- [func generateSphericalHarmonics(fromLight: Int)](mdlphotometriclight/generatesphericalharmonics(fromlight:).md)
  Generates spherical harmonics information based on the light’s photometry data.
- [var sphericalHarmonicsLevel: Int](mdlphotometriclight/sphericalharmonicslevel.md)
  The number of levels of generated spherical harmonics information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlphotometriclight/sphericalharmonicscoefficients)*