# MDLProbePlacement

**Framework**: Model I/O  
**Kind**: enum  
**Role**: Enumeration

Options affecting automatic placement of light probes in a scene, used with the [`placeLightProbes(withDensity:heuristic:using:)`](./mdlasset/placelightprobes%28withdensity,heuristic,using%29.md) method.

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

```c
enum MDLProbePlacement : NSInteger;
```

## Topics

### Constants
- [MDLProbePlacement.irradianceDistribution](./mdlprobeplacement/irradiancedistribution.md)
  An option to examine the lighting conditions at various positions in the scene being evaluated, then place light probes only at the locations where each contributes optimally to scene lighting.
- [MDLProbePlacement.uniformGrid](./mdlprobeplacement/uniformgrid.md)
  An option to place light probes at each unit coordinate in a three-dimensional grid that evenly divides the region being evaluated.
### Initializers
- [init?(rawValue: Int)](./mdlprobeplacement/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Working with Lights
- [class func placeLightProbes(withDensity: Float, heuristic: MDLProbePlacement, using: any MDLLightProbeIrradianceDataSource) -> [MDLLightProbe]](./mdlasset/placelightprobes%28withdensity,heuristic,using%29.md)
  Automatically creates and places light probes for use in illuminating a scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlprobeplacement)*