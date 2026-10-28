# resultGradientTensors(for:)

**Framework**: ML Compute  
**Kind**: method  
**Role**: Instance Method

Gets the result gradient tensors for the layer in the training graph you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
func resultGradientTensors(for layer: MLCLayer) -> [MLCTensor]
```

```objc
- (NSArray<MLCTensor *> *) resultGradientTensorsForLayer:(MLCLayer *) layer;
```

## Return Value

An array of tensors.

## Parameters

- `layer`: A layer in the training graph.

## See Also

### Inspecting Training Graphs
- [func bindOptimizerData([MLCTensorData], deviceData: [MLCTensorOptimizerDeviceData]?, with: MLCTensor) -> Bool](./bindoptimizerdata%28_,devicedata,with%29.md)
  Associates the optimizer and device data you specify along with the tensor.
- [var optimizer: MLCOptimizer?](./optimizer.md)
  The optimizer to use with the training graph.
- [var deviceMemorySize: Int](./devicememorysize.md)
  The device memory size in bytes for all intermediate tensors for forward, gradient passes, and optimizer updates for all layers in the training graph.
- [func gradientTensor(forInput: MLCTensor) -> MLCTensor?](./gradienttensor%28forinput%29.md)
  Gets the gradient tensor for the input tensor you specify.
- [func sourceGradientTensors(for: MLCLayer) -> [MLCTensor]](./sourcegradienttensors%28for%29.md)
  Gets the source gradient tensors for the layer in the training graph you specify.
- [func gradientData(forParameter: MLCTensor, layer: MLCLayer) -> Data?](./gradientdata%28forparameter,layer%29.md)
  Gets the gradient data for the trainable parameter and associated layer you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctraininggraph/resultgradienttensors(for:))*