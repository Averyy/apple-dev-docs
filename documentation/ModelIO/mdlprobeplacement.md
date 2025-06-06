# MDLProbePlacement

**Framework**: Model I/O  
**Kind**: enum

Options affecting automatic placement of light probes in a scene, used with the [`placeLightProbes(withDensity:heuristic:using:)`](mdlasset/placelightprobes(withdensity:heuristic:using:).md) method.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum MDLProbePlacement
```

## Topics

### Constants
- [MDLProbePlacement.irradianceDistribution](mdlprobeplacement/irradiancedistribution.md)
  An option to examine the lighting conditions at various positions in the scene being evaluated, then place light probes only at the locations where each contributes optimally to scene lighting.
- [MDLProbePlacement.uniformGrid](mdlprobeplacement/uniformgrid.md)
  An option to place light probes at each unit coordinate in a three-dimensional grid that evenly divides the region being evaluated.
### Initializers
- [init?(rawValue: Int)](mdlprobeplacement/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class func placeLightProbes(withDensity: Float, heuristic: MDLProbePlacement, using: any MDLLightProbeIrradianceDataSource) -> [MDLLightProbe]](mdlasset/placelightprobes(withdensity:heuristic:using:).md)
  Automatically creates and places light probes for use in illuminating a scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlprobeplacement)*