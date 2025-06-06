# compile(options:device:)

**Framework**: ML Compute  
**Kind**: method

Compiles the training graph for the options and device you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
func compile(options: MLCGraphCompilationOptions = [], device: MLCDevice) -> Bool
```

#### Return Value

`true` if the operation was successful.

## Parameters

- `options`: The compiler options.
- `device`: The device.

## See Also

- [func addInputs([String : MLCTensor], lossLabels: [String : MLCTensor]?) -> Bool](mlctraininggraph/addinputs(_:losslabels:).md)
  Adds the inputs and loss label inputs that you specify to the training graph.
- [func addInputs([String : MLCTensor], lossLabels: [String : MLCTensor]?, lossLabelWeights: [String : MLCTensor]?) -> Bool](mlctraininggraph/addinputs(_:losslabels:losslabelweights:).md)
  Adds the inputs, loss labels, and loss label weights that you specify to the training graph.
- [func addOutputs([String : MLCTensor]) -> Bool](mlctraininggraph/addoutputs(_:).md)
  Adds the outputs to the training graph you specify.
- [func stopGradient(for: [MLCTensor]) -> Bool](mlctraininggraph/stopgradient(for:).md)
  Adds the tensors that you specify, to indicate which contributions the graph excludes when computing gradients during gradient pass.
- [func compileOptimizer(MLCOptimizer) -> Bool](mlctraininggraph/compileoptimizer(_:).md)
  Compiles the optimizer to use with a training graph you specify.
- [func compile(options: MLCGraphCompilationOptions, device: MLCDevice, inputTensors: [String : MLCTensor]?, inputTensorsData: [String : MLCTensorData]?) -> Bool](mlctraininggraph/compile(options:device:inputtensors:inputtensorsdata:).md)
  Compiles the training graph for the options, device, and input tensors you specify.
- [func link(with: [MLCTrainingGraph]) -> Bool](mlctraininggraph/link(with:).md)
  Links the training graphs you specify.
- [func allocateUserGradient(for: MLCTensor) -> MLCTensor?](mlctraininggraph/allocateusergradient(for:).md)
  Allocates an entry for a gradient for the result tensor you specify.
- [struct MLCGraphCompilationOptions](mlcgraphcompilationoptions.md)
  A bitmask that specifies the options you use when compiling a graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctraininggraph/compile(options:device:))*