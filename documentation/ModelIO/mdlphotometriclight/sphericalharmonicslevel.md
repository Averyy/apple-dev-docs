# sphericalHarmonicsLevel

**Framework**: Model I/O  
**Kind**: property

The number of levels of generated spherical harmonics information.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var sphericalHarmonicsLevel: Int { get }
```

#### Discussion

Each level of spherical harmonics contains more coefficients, and thus affects the layout of the data containing those coefficients. For details, see the [`sphericalHarmonicsCoefficients`](mdlphotometriclight/sphericalharmonicscoefficients.md) property.

## See Also

- [func generateSphericalHarmonics(fromLight: Int)](mdlphotometriclight/generatesphericalharmonics(fromlight:).md)
  Generates spherical harmonics information based on the light’s photometry data.
- [var sphericalHarmonicsCoefficients: Data?](mdlphotometriclight/sphericalharmonicscoefficients.md)
  Data containing spherical harmonics coefficients that describe the light’s intensity in all directions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlphotometriclight/sphericalharmonicslevel)*