# MLCGraphCompilationOptions

**Framework**: ML Compute  
**Kind**: struct  
**Role**: Structure

A bitmask that specifies the options you use when compiling a graph.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
struct MLCGraphCompilationOptions
```

```c
enum MLCGraphCompilationOptions : uint64_t;
```

## Topics

### Creating Graph Compilation Options
- [init(rawValue: UInt64)](./mlcgraphcompilationoptions/init%28rawvalue%29.md)
  Creates a graph compilation option with the specified raw value.
- [static var debugLayers: MLCGraphCompilationOptions](./mlcgraphcompilationoptions/debuglayers.md)
  The option to debug layers during graph compilation.
- [static var disableLayerFusion: MLCGraphCompilationOptions](./mlcgraphcompilationoptions/disablelayerfusion.md)
  The option to disable layer fusion during graph compilation.
- [static var linkGraphs: MLCGraphCompilationOptions](./mlcgraphcompilationoptions/linkgraphs.md)
  The option to link graphs during graph compilation.
- [static var computeAllGradients: MLCGraphCompilationOptions](./mlcgraphcompilationoptions/computeallgradients.md)
  The option to compute all gradients during graph compilation.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Preparing Inference Graphs
- [func addInputs([String : MLCTensor]) -> Bool](./mlcinferencegraph/addinputs%28_%29.md)
  Adds the inputs you specify to the inference graph.
- [func addInputs([String : MLCTensor], lossLabels: [String : MLCTensor]?, lossLabelWeights: [String : MLCTensor]?) -> Bool](./mlcinferencegraph/addinputs%28_,losslabels,losslabelweights%29.md)
  Adds the inputs, loss labels, and loss label weights that you specify to the inference graph.
- [func addOutputs([String : MLCTensor]) -> Bool](./mlcinferencegraph/addoutputs%28_%29.md)
  Adds the outputs you specify to the inference graph.
- [func compile(options: MLCGraphCompilationOptions, device: MLCDevice) -> Bool](./mlcinferencegraph/compile%28options,device%29.md)
  Compiles the inference graph for the options and device you specify.
- [func compile(options: MLCGraphCompilationOptions, device: MLCDevice, inputTensors: [String : MLCTensor]?, inputTensorsData: [String : MLCTensorData]?) -> Bool](./mlcinferencegraph/compile%28options,device,inputtensors,inputtensorsdata%29.md)
  Compiles the inference graph for the options, device, and input tensors you specify.
- [func link(with: [MLCInferenceGraph]) -> Bool](./mlcinferencegraph/link%28with%29.md)
  Links the inference graphs you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcgraphcompilationoptions)*