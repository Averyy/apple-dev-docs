# placeLightProbes(withDensity:heuristic:using:)

**Framework**: Model I/O  
**Kind**: method

Automatically creates and places light probes for use in illuminating a scene.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func placeLightProbes(withDensity value: Float, heuristic type: MDLProbePlacement, using dataSource: any MDLLightProbeIrradianceDataSource) -> [MDLLightProbe]
```

#### Return Value

An array of light probe objects for use in the scene.

#### Discussion

When you call this method, you must pass a custom object implementing the [`MDLLightProbeIrradianceDataSource`](mdllightprobeirradiancedatasource.md) protocol. Model I/O queries this object to determine how to place light probes.

When you use the [`MDLProbePlacement.uniformGrid`](mdlprobeplacement/uniformgrid.md) heuristic,  Model I/O simply divides the [`boundingBox`](mdllightprobeirradiancedatasource/boundingbox.md) region your data source provides into `value` units in each dimension, and creates an array of light probe objects to fill each position in the resulting grid.

When you use the [`MDLProbePlacement.irradianceDistribution`](mdlprobeplacement/irradiancedistribution.md) heuristic, Model I/O uses the same grid to sample information about the lighting conditions in your scene (by calling the [`sphericalHarmonicsLevel`](mdllightprobeirradiancedatasource/sphericalharmonicslevel.md) and [`sphericalHarmonicsCoefficients(atPosition:)`](mdllightprobeirradiancedatasource/sphericalharmonicscoefficients(atposition:).md) methods of your data source), then creates and positions light probes to optimally account for differences in lighting conditions across the scene.

## Parameters

- `value`: A value that determines the coarseness or fineness with which to evaluate the scene. Lower values evaluate fewer positions, resulting in fewer light probes and lower fidelity. Higher values evaluate more positions, resulting in higher fidelity at increased computational cost.
- `type`: An option that determine how Model I/O uses the data source to position light probes.
- `dataSource`: A custom object that provides information about the scene to be evaluated.

## See Also

- [enum MDLProbePlacement](mdlprobeplacement.md)
  Options affecting automatic placement of light probes in a scene, used with the [`placeLightProbes(withDensity:heuristic:using:)`](mdlasset/placelightprobes(withdensity:heuristic:using:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlasset/placelightprobes(withdensity:heuristic:using:))*