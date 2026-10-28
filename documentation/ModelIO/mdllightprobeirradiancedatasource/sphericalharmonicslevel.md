# sphericalHarmonicsLevel

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

The number of levels of spherical harmonics information provided by the data source.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional var sphericalHarmonicsLevel: Int { get set }
```

```objc
@property NSUInteger sphericalHarmonicsLevel;
```

## Discussion

Each level of spherical harmonics contains more coefficients, and thus affects the layout of the data containing those coefficients. For details, see the [`sphericalHarmonicsCoefficients(atPosition:)`](./sphericalharmonicscoefficients%28atposition%29.md) method.

## See Also

### Providing Light Probe Information
- [var boundingBox: MDLAxisAlignedBoundingBox](./boundingbox.md)
  The bounding region of the scene to which light probes are being added.
- [func sphericalHarmonicsCoefficients(atPosition: vector_float3) -> Data](./sphericalharmonicscoefficients%28atposition%29.md)
  Asks the data source to provide spherical harmonics coefficients that describe lighting conditions in all directions from the specified point in a scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdllightprobeirradiancedatasource/sphericalharmonicslevel)*