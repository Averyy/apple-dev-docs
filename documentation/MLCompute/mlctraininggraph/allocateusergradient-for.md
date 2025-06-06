# allocateUserGradient(for:)

**Framework**: ML Compute  
**Kind**: method

Allocates an entry for a gradient for the result tensor you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
func allocateUserGradient(for tensor: MLCTensor) -> MLCTensor?
```

#### Return Value

A gradient tensor.

#### Discussion

Third-party numeric libraries can perform additional computations on the result tensor produced by a layer in the training graph. This external computation may produce gradients that you can backpropagate during gradient execution by using this method to allocate an entry for the gradient.

## Parameters

- `tensor`: A result tensor.

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
- [func compile(options: MLCGraphCompilationOptions, device: MLCDevice) -> Bool](mlctraininggraph/compile(options:device:).md)
  Compiles the training graph for the options and device you specify.
- [func compile(options: MLCGraphCompilationOptions, device: MLCDevice, inputTensors: [String : MLCTensor]?, inputTensorsData: [String : MLCTensorData]?) -> Bool](mlctraininggraph/compile(options:device:inputtensors:inputtensorsdata:).md)
  Compiles the training graph for the options, device, and input tensors you specify.
- [func link(with: [MLCTrainingGraph]) -> Bool](mlctraininggraph/link(with:).md)
  Links the training graphs you specify.
- [struct MLCGraphCompilationOptions](mlcgraphcompilationoptions.md)
  A bitmask that specifies the options you use when compiling a graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctraininggraph/allocateusergradient(for:))*