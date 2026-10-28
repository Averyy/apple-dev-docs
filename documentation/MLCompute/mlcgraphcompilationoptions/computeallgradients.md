# computeAllGradients

**Framework**: ML Compute  
**Kind**: property  
**Role**: Type Property

The option to compute all gradients during graph compilation.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
static var computeAllGradients: MLCGraphCompilationOptions { get }
```

```c
MLCGraphCompilationOptionsComputeAllGradients
```

## Discussion

Include this option to compute gradients for layers with or without parameters that only take input tensors.

For example, if the first layer of a graph is a convolution layer, the framework only computes the gradients for weights and biases associated with the convolution layer, but not the gradients for the input. Include this option if you want to compute all gradients for the input.

## See Also

### Creating Graph Compilation Options
- [init(rawValue: UInt64)](./init%28rawvalue%29.md)
  Creates a graph compilation option with the specified raw value.
- [static var debugLayers: MLCGraphCompilationOptions](./debuglayers.md)
  The option to debug layers during graph compilation.
- [static var disableLayerFusion: MLCGraphCompilationOptions](./disablelayerfusion.md)
  The option to disable layer fusion during graph compilation.
- [static var linkGraphs: MLCGraphCompilationOptions](./linkgraphs.md)
  The option to link graphs during graph compilation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgraphcompilationoptions/computeallgradients)*