# sphericalHarmonicsLevel

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) NSUInteger sphericalHarmonicsLevel;
```

#### Discussion

Each level of spherical harmonics contains more coefficients, and thus affects the layout of the data containing those coefficients. For details, see the [`sphericalHarmonicsCoefficients`](./sphericalharmonicscoefficients.md) property.

## See Also

### Working with Spherical Harmonics
- [func generateSphericalHarmonics(fromIrradiance: Int)](./generatesphericalharmonics%28fromirradiance%29.md)
  Generates spherical harmonics information based on the light probe’s irradiance texture.
- [var sphericalHarmonicsCoefficients: Data?](./sphericalharmonicscoefficients.md)
  Data containing the spherical harmonics coefficients for the light.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdllightprobe/sphericalharmonicslevel)*