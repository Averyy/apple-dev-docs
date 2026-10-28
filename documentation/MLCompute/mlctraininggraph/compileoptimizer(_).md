# compileOptimizer(_:)

**Framework**: ML Compute  
**Kind**: method  
**Role**: Instance Method

Compiles the optimizer to use with a training graph you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
func compileOptimizer(_ optimizer: MLCOptimizer) -> Bool
```

```objc
- (BOOL) compileOptimizer:(MLCOptimizer *) optimizer;
```

## Return Value

`true` if the operation was successful.

## Discussion

Typically you specify the optimizer to use with a training graph when creating the training graph, using [`init(graphObjects:lossLayer:optimizer:)`](./init%28graphobjects,losslayer,optimizer%29.md). The optimizer is then compiled in when you call [`compile(options:device:)`](./compile%28options,device%29.md).

Alternatively, if the optimizer isn’t known when the framework creates or compiles the training graph, you can use this method to associate and compile in an optimizer.

## Parameters

- `optimizer`: The optimizer.

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
- [func compile(options: MLCGraphCompilationOptions, device: MLCDevice) -> Bool](./compile%28options,device%29.md)
  Compiles the training graph for the options and device you specify.
- [func compile(options: MLCGraphCompilationOptions, device: MLCDevice, inputTensors: [String : MLCTensor]?, inputTensorsData: [String : MLCTensorData]?) -> Bool](./compile%28options,device,inputtensors,inputtensorsdata%29.md)
  Compiles the training graph for the options, device, and input tensors you specify.
- [func link(with: [MLCTrainingGraph]) -> Bool](./link%28with%29.md)
  Links the training graphs you specify.
- [func allocateUserGradient(for: MLCTensor) -> MLCTensor?](./allocateusergradient%28for%29.md)
  Allocates an entry for a gradient for the result tensor you specify.
- [struct MLCGraphCompilationOptions](../mlcgraphcompilationoptions.md)
  A bitmask that specifies the options you use when compiling a graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctraininggraph/compileoptimizer(_:))*