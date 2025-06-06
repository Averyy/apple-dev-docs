# link(with:)

**Framework**: ML Compute  
**Kind**: method

Links the inference graphs you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
func link(with graphs: [MLCInferenceGraph]) -> Bool
```

#### Return Value

`true` if the operation was successful.

## Parameters

- `graphs`: An array that contains the inference graphs.

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
- [struct MLCGraphCompilationOptions](mlcgraphcompilationoptions.md)
  A bitmask that specifies the options you use when compiling a graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcinferencegraph/link(with:))*