# compile(options:device:)

**Framework**: ML Compute  
**Kind**: method  
**Role**: Instance Method

Compiles the inference graph for the options and device you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
func compile(options: MLCGraphCompilationOptions = [], device: MLCDevice) -> Bool
```

```objc
- (BOOL) compileWithOptions:(MLCGraphCompilationOptions) options device:(MLCDevice *) device;
```

## Return Value

`true` if the operation was successful.

## Parameters

- `options`: The compiler options.
- `device`: The device.

## See Also

### Preparing Inference Graphs
- [func addInputs([String : MLCTensor]) -> Bool](./addinputs%28_%29.md)
  Adds the inputs you specify to the inference graph.
- [func addInputs([String : MLCTensor], lossLabels: [String : MLCTensor]?, lossLabelWeights: [String : MLCTensor]?) -> Bool](./addinputs%28_,losslabels,losslabelweights%29.md)
  Adds the inputs, loss labels, and loss label weights that you specify to the inference graph.
- [func addOutputs([String : MLCTensor]) -> Bool](./addoutputs%28_%29.md)
  Adds the outputs you specify to the inference graph.
- [func compile(options: MLCGraphCompilationOptions, device: MLCDevice, inputTensors: [String : MLCTensor]?, inputTensorsData: [String : MLCTensorData]?) -> Bool](./compile%28options,device,inputtensors,inputtensorsdata%29.md)
  Compiles the inference graph for the options, device, and input tensors you specify.
- [func link(with: [MLCInferenceGraph]) -> Bool](./link%28with%29.md)
  Links the inference graphs you specify.
- [struct MLCGraphCompilationOptions](../mlcgraphcompilationoptions.md)
  A bitmask that specifies the options you use when compiling a graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcinferencegraph/compile(options:device:))*