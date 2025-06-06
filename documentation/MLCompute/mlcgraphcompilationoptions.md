# MLCGraphCompilationOptions

**Framework**: ML Compute  
**Kind**: struct

A bitmask that specifies the options you use when compiling a graph.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
struct MLCGraphCompilationOptions
```

## Topics

### Creating Graph Compilation Options
- [init(rawValue: UInt64)](mlcgraphcompilationoptions/init(rawvalue:).md)
  Creates a graph compilation option with the specified raw value.
- [static var debugLayers: MLCGraphCompilationOptions](mlcgraphcompilationoptions/debuglayers.md)
  The option to debug layers during graph compilation.
- [static var disableLayerFusion: MLCGraphCompilationOptions](mlcgraphcompilationoptions/disablelayerfusion.md)
  The option to disable layer fusion during graph compilation.
- [static var linkGraphs: MLCGraphCompilationOptions](mlcgraphcompilationoptions/linkgraphs.md)
  The option to link graphs during graph compilation.
- [static var computeAllGradients: MLCGraphCompilationOptions](mlcgraphcompilationoptions/computeallgradients.md)
  The option to compute all gradients during graph compilation.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func addInputs([String : MLCTensor]) -> Bool](mlcinferencegraph/addinputs(_:).md)
  Adds the inputs you specify to the inference graph.
- [func addInputs([String : MLCTensor], lossLabels: [String : MLCTensor]?, lossLabelWeights: [String : MLCTensor]?) -> Bool](mlcinferencegraph/addinputs(_:losslabels:losslabelweights:).md)
  Adds the inputs, loss labels, and loss label weights that you specify to the inference graph.
- [func addOutputs([String : MLCTensor]) -> Bool](mlcinferencegraph/addoutputs(_:).md)
  Adds the outputs you specify to the inference graph.
- [func compile(options: MLCGraphCompilationOptions, device: MLCDevice) -> Bool](mlcinferencegraph/compile(options:device:).md)
  Compiles the inference graph for the options and device you specify.
- [func compile(options: MLCGraphCompilationOptions, device: MLCDevice, inputTensors: [String : MLCTensor]?, inputTensorsData: [String : MLCTensorData]?) -> Bool](mlcinferencegraph/compile(options:device:inputtensors:inputtensorsdata:).md)
  Compiles the inference graph for the options, device, and input tensors you specify.
- [func link(with: [MLCInferenceGraph]) -> Bool](mlcinferencegraph/link(with:).md)
  Links the inference graphs you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgraphcompilationoptions)*