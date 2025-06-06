# boundingBox

**Framework**: Model I/O  
**Kind**: property  
**Required**: Yes

The bounding region of the scene to which light probes are being added.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var boundingBox: MDLAxisAlignedBoundingBox { get set }
```

#### Discussion

When you call the [`MDLAsset`](mdlasset.md) [`placeLightProbes(withDensity:heuristic:using:)`](mdlasset/placelightprobes(withdensity:heuristic:using:).md) method to automatically distribute light probes in a scene, Model I/O reads this property to ask your code which regions should be evaluated for light probe placement.

## See Also

- [var sphericalHarmonicsLevel: Int](mdllightprobeirradiancedatasource/sphericalharmonicslevel.md)
  The number of levels of spherical harmonics information provided by the data source.
- [func sphericalHarmonicsCoefficients(atPosition: vector_float3) -> Data](mdllightprobeirradiancedatasource/sphericalharmonicscoefficients(atposition:).md)
  Asks the data source to provide spherical harmonics coefficients that describe lighting conditions in all directions from the specified point in a scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdllightprobeirradiancedatasource/boundingbox)*