# compile(options:device:inputTensors:inputTensorsData:)

**Framework**: ML Compute  
**Kind**: method  
**Role**: Instance Method

Compiles the training graph for the options, device, and input tensors you specify.

**Availability**:
- iOS 14.5+ - Deprecated in 17.4
- iPadOS 14.5+ - Deprecated in 17.4
- Mac Catalyst 14.5+ - Deprecated in 17.4
- macOS 11.3+ - Deprecated in 14.3
- tvOS 14.5+ - Deprecated in 17.4

## Declaration

```swift
func compile(options: MLCGraphCompilationOptions = [], device: MLCDevice, inputTensors: [String : MLCTensor]?, inputTensorsData: [String : MLCTensorData]?) -> Bool
```

```objc
- (BOOL) compileWithOptions:(MLCGraphCompilationOptions) options device:(MLCDevice *) device inputTensors:(NSDictionary<NSString *,MLCTensor *> *) inputTensors inputTensorsData:(NSDictionary<NSString *,MLCTensorData *> *) inputTensorsData;
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

### Preparing Training Graphs
- [func addInputs([String : MLCTensor], lossLabels: [String : MLCTensor]?) -> Bool](./addinputs%28_,losslabels%29.md)
  Adds the inputs and loss label inputs that you specify to the training graph.
- [func addInputs([String : MLCTensor], lossLabels: [String : MLCTensor]?, lossLabelWeights: [String : MLCTensor]?) -> Bool](./addinputs%28_,losslabels,losslabelweights%29.md)
  Adds the inputs, loss labels, and loss label weights that you specify to the training graph.
- [func addOutputs([String : MLCTensor]) -> Bool](./addoutputs%28_%29.md)
  Adds the outputs to the training graph you specify.
- [func stopGradient(for: [MLCTensor]) -> Bool](./stopgradient%28for%29.md)
  Adds the tensors that you specify, to indicate which contributions the graph excludes when computing gradients during gradient pass.
- [func compileOptimizer(MLCOptimizer) -> Bool](./compileoptimizer%28_%29.md)
  Compiles the optimizer to use with a training graph you specify.
- [func compile(options: MLCGraphCompilationOptions, device: MLCDevice) -> Bool](./compile%28options,device%29.md)
  Compiles the training graph for the options and device you specify.
- [func link(with: [MLCTrainingGraph]) -> Bool](./link%28with%29.md)
  Links the training graphs you specify.
- [func allocateUserGradient(for: MLCTensor) -> MLCTensor?](./allocateusergradient%28for%29.md)
  Allocates an entry for a gradient for the result tensor you specify.
- [struct MLCGraphCompilationOptions](../mlcgraphcompilationoptions.md)
  A bitmask that specifies the options you use when compiling a graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctraininggraph/compile(options:device:inputtensors:inputtensorsdata:))*