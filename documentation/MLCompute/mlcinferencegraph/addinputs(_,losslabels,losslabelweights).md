# addInputs(_:lossLabels:lossLabelWeights:)

**Framework**: ML Compute  
**Kind**: method  
**Role**: Instance Method

Adds the inputs, loss labels, and loss label weights that you specify to the inference graph.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
func addInputs(_ inputs: [String : MLCTensor], lossLabels: [String : MLCTensor]?, lossLabelWeights: [String : MLCTensor]?) -> Bool
```

```objc
- (BOOL) addInputs:(NSDictionary<NSString *,MLCTensor *> *) inputs lossLabels:(NSDictionary<NSString *,MLCTensor *> *) lossLabels lossLabelWeights:(NSDictionary<NSString *,MLCTensor *> *) lossLabelWeights;
```

#### Return Value

`true` if the operation was successful.

## Parameters

- `inputs`: A dictionary that contains inputs.
- `lossLabels`: A dictionary that contains loss label inputs.
- `lossLabelWeights`: A dictionary that contains loss label weights.

## See Also

### Preparing Inference Graphs
- [func addInputs([String : MLCTensor]) -> Bool](./addinputs%28_%29.md)
  Adds the inputs you specify to the inference graph.
- [func addOutputs([String : MLCTensor]) -> Bool](./addoutputs%28_%29.md)
  Adds the outputs you specify to the inference graph.
- [func compile(options: MLCGraphCompilationOptions, device: MLCDevice) -> Bool](./compile%28options,device%29.md)
  Compiles the inference graph for the options and device you specify.
- [func compile(options: MLCGraphCompilationOptions, device: MLCDevice, inputTensors: [String : MLCTensor]?, inputTensorsData: [String : MLCTensorData]?) -> Bool](./compile%28options,device,inputtensors,inputtensorsdata%29.md)
  Compiles the inference graph for the options, device, and input tensors you specify.
- [func link(with: [MLCInferenceGraph]) -> Bool](./link%28with%29.md)
  Links the inference graphs you specify.
- [struct MLCGraphCompilationOptions](../mlcgraphcompilationoptions.md)
  A bitmask that specifies the options you use when compiling a graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcinferencegraph/addinputs(_:losslabels:losslabelweights:))*