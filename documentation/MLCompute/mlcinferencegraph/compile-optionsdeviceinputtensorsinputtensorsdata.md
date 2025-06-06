# compile(options:device:inputTensors:inputTensorsData:)

**Framework**: ML Compute  
**Kind**: method

Compiles the inference graph for the options, device, and input tensors you specify.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+

## Declaration

```swift
func compile(options: MLCGraphCompilationOptions = [], device: MLCDevice, inputTensors: [String : MLCTensor]?, inputTensorsData: [String : MLCTensorData]?) -> Bool
```

#### Return Value

A Boolean that indicates success or failure.

#### Discussion

If you specify the list of constant tensors before the framework compiles the graph, then the framework can perform additional optimizations during the compilation.

## Parameters

- `options`: The compiler options.
- `device`: The device.
- `inputTensors`: The list of input tensors that are constants.
- `inputTensorsData`: The tensor data to use with the input tensors.

## See Also

- [func addInputs([String : MLCTensor]) -> Bool](mlcinferencegraph/addinputs(_:).md)
  Adds the inputs you specify to the inference graph.
- [func addInputs([String : MLCTensor], lossLabels: [String : MLCTensor]?, lossLabelWeights: [String : MLCTensor]?) -> Bool](mlcinferencegraph/addinputs(_:losslabels:losslabelweights:).md)
  Adds the inputs, loss labels, and loss label weights that you specify to the inference graph.
- [func addOutputs([String : MLCTensor]) -> Bool](mlcinferencegraph/addoutputs(_:).md)
  Adds the outputs you specify to the inference graph.
- [func compile(options: MLCGraphCompilationOptions, device: MLCDevice) -> Bool](mlcinferencegraph/compile(options:device:).md)
  Compiles the inference graph for the options and device you specify.
- [func link(with: [MLCInferenceGraph]) -> Bool](mlcinferencegraph/link(with:).md)
  Links the inference graphs you specify.
- [struct MLCGraphCompilationOptions](mlcgraphcompilationoptions.md)
  A bitmask that specifies the options you use when compiling a graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcinferencegraph/compile(options:device:inputtensors:inputtensorsdata:))*