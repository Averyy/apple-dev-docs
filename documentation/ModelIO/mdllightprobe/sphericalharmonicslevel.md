# sphericalHarmonicsLevel

**Framework**: Model I/O  
**Kind**: property

The number of levels of spherical harmonics information in the light probe.

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

Each level of spherical harmonics contains more coefficients, and thus affects the layout of the data containing those coefficients. For details, see the [`sphericalHarmonicsCoefficients`](mdllightprobe/sphericalharmonicscoefficients.md) property.

## See Also

- [func generateSphericalHarmonics(fromIrradiance: Int)](mdllightprobe/generatesphericalharmonics(fromirradiance:).md)
  Generates spherical harmonics information based on the light probe’s irradiance texture.
- [var sphericalHarmonicsCoefficients: Data?](mdllightprobe/sphericalharmonicscoefficients.md)
  Data containing the spherical harmonics coefficients for the light.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdllightprobe/sphericalharmonicslevel)*