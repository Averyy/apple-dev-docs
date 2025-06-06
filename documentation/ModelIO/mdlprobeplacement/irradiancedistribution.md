# MDLProbePlacement.irradianceDistribution

**Framework**: Model I/O  
**Kind**: case

An option to examine the lighting conditions at various positions in the scene being evaluated, then place light probes only at the locations where each contributes optimally to scene lighting.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
case irradianceDistribution
```

#### Discussion

If you use this heuristic, your data source must implement the [`sphericalHarmonicsCoefficients(atPosition:)`](mdllightprobeirradiancedatasource/sphericalharmonicscoefficients(atposition:).md) method.

## See Also

- [MDLProbePlacement.uniformGrid](mdlprobeplacement/uniformgrid.md)
  An option to place light probes at each unit coordinate in a three-dimensional grid that evenly divides the region being evaluated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlprobeplacement/irradiancedistribution)*