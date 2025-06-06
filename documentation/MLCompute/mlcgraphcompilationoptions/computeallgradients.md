# computeAllGradients

**Framework**: ML Compute  
**Kind**: property

The option to compute all gradients during graph compilation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
static var computeAllGradients: MLCGraphCompilationOptions { get }
```

#### Discussion

Include this option to compute gradients for layers with or without parameters that only take input tensors.

For example, if the first layer of a graph is a convolution layer, the framework only computes the gradients for weights and biases associated with the convolution layer, but not the gradients for the input. Include this option if you want to compute all gradients for the input.

## See Also

- [init(rawValue: UInt64)](mlcgraphcompilationoptions/init(rawvalue:).md)
  Creates a graph compilation option with the specified raw value.
- [static var debugLayers: MLCGraphCompilationOptions](mlcgraphcompilationoptions/debuglayers.md)
  The option to debug layers during graph compilation.
- [static var disableLayerFusion: MLCGraphCompilationOptions](mlcgraphcompilationoptions/disablelayerfusion.md)
  The option to disable layer fusion during graph compilation.
- [static var linkGraphs: MLCGraphCompilationOptions](mlcgraphcompilationoptions/linkgraphs.md)
  The option to link graphs during graph compilation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgraphcompilationoptions/computeallgradients)*