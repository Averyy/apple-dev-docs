# resultGradientTensors(for:)

**Framework**: ML Compute  
**Kind**: method

Gets the result gradient tensors for the layer in the training graph you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
func resultGradientTensors(for layer: MLCLayer) -> [MLCTensor]
```

#### Return Value

An array of tensors.

## Parameters

- `layer`: A layer in the training graph.

## See Also

- [func bindOptimizerData([MLCTensorData], deviceData: [MLCTensorOptimizerDeviceData]?, with: MLCTensor) -> Bool](mlctraininggraph/bindoptimizerdata(_:devicedata:with:).md)
  Associates the optimizer and device data you specify along with the tensor.
- [var optimizer: MLCOptimizer?](mlctraininggraph/optimizer.md)
  The optimizer to use with the training graph.
- [var deviceMemorySize: Int](mlctraininggraph/devicememorysize.md)
  The device memory size in bytes for all intermediate tensors for forward, gradient passes, and optimizer updates for all layers in the training graph.
- [func gradientTensor(forInput: MLCTensor) -> MLCTensor?](mlctraininggraph/gradienttensor(forinput:).md)
  Gets the gradient tensor for the input tensor you specify.
- [func sourceGradientTensors(for: MLCLayer) -> [MLCTensor]](mlctraininggraph/sourcegradienttensors(for:).md)
  Gets the source gradient tensors for the layer in the training graph you specify.
- [func gradientData(forParameter: MLCTensor, layer: MLCLayer) -> Data?](mlctraininggraph/gradientdata(forparameter:layer:).md)
  Gets the gradient data for the trainable parameter and associated layer you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctraininggraph/resultgradienttensors(for:))*