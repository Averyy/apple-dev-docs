# linkGraphs

**Framework**: ML Compute  
**Kind**: property

The option to link graphs during graph compilation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
static var linkGraphs: MLCGraphCompilationOptions { get }
```

#### Discussion

Include this option when you link together one or more sub-graphs when executing the forward, gradient, and optimizer update. For example, if the full computation graph includes a layer that the framework doesn’t support, you’ll need to create multiple sub-graphs and link them together using `linkWithGraphs`. When doing so, include this option when you call `compileWithOptions` for graphs you want to link together.

## See Also

- [init(rawValue: UInt64)](mlcgraphcompilationoptions/init(rawvalue:).md)
  Creates a graph compilation option with the specified raw value.
- [static var debugLayers: MLCGraphCompilationOptions](mlcgraphcompilationoptions/debuglayers.md)
  The option to debug layers during graph compilation.
- [static var disableLayerFusion: MLCGraphCompilationOptions](mlcgraphcompilationoptions/disablelayerfusion.md)
  The option to disable layer fusion during graph compilation.
- [static var computeAllGradients: MLCGraphCompilationOptions](mlcgraphcompilationoptions/computeallgradients.md)
  The option to compute all gradients during graph compilation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgraphcompilationoptions/linkgraphs)*