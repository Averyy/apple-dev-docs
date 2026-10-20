# linkGraphs

**Framework**: ML Compute  
**Kind**: property  
**Role**: Type Property

The option to link graphs during graph compilation.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
static var linkGraphs: MLCGraphCompilationOptions { get }
```

```c
MLCGraphCompilationOptionsLinkGraphs
```

#### Discussion

Include this option when you link together one or more sub-graphs when executing the forward, gradient, and optimizer update. For example, if the full computation graph includes a layer that the framework doesn’t support, you’ll need to create multiple sub-graphs and link them together using `linkWithGraphs`. When doing so, include this option when you call `compileWithOptions` for graphs you want to link together.

## See Also

### Creating Graph Compilation Options
- [init(rawValue: UInt64)](./init%28rawvalue%29.md)
  Creates a graph compilation option with the specified raw value.
- [static var debugLayers: MLCGraphCompilationOptions](./debuglayers.md)
  The option to debug layers during graph compilation.
- [static var disableLayerFusion: MLCGraphCompilationOptions](./disablelayerfusion.md)
  The option to disable layer fusion during graph compilation.
- [static var computeAllGradients: MLCGraphCompilationOptions](./computeallgradients.md)
  The option to compute all gradients during graph compilation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgraphcompilationoptions/linkgraphs)*