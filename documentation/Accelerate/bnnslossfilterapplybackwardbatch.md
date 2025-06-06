# BNNSLossFilterApplyBackwardBatch(_:_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a loss filter backward to generate gradients.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func BNNSLossFilterApplyBackwardBatch(_ filter: BNNSFilter?, _ batch_size: Int, _ in: UnsafeRawPointer, _ in_stride: Int, _ in_delta: UnsafeMutablePointer<BNNSNDArrayDescriptor>, _ in_delta_stride: Int, _ labels: UnsafeRawPointer, _ labels_stride: Int, _ weights: UnsafeRawPointer?, _ weights_size: Int, _ out_delta: UnsafePointer<BNNSNDArrayDescriptor>, _ out_delta_stride: Int) -> Int32
```

## Parameters

- `filter`: The filter to apply.
- `batch_size`: The number of input-output pairs.
- `in`: Pointer to input object.
- `in_stride`: Increment, in values, between input objects.
- `in_delta`: The descriptor of the input delta.
- `in_delta_stride`: Increment, in values, between input delta objects.
- `labels`: Pointer to the labels data.
- `labels_stride`: Increment, in values, between labels.
- `weights`: Pointer to weights delta object.
- `weights_size`: Set to   for no weight loss scaling, or   for same weight scaling for all samples in the batch.
- `out_delta`: The descriptor of the output delta.
- `out_delta_stride`: Increment, in values, between output delta objects.

## See Also

- [class LossLayer](bnns/losslayer.md)
  A layer object that wraps a loss filter and manages its deinitialization.
- [struct BNNSLossFunction](bnnslossfunction.md)
  Constants that describe loss functions.
- [struct BNNSLossReductionFunction](bnnslossreductionfunction.md)
  Constants that describe reduction functions used by a loss layer.
- [struct BNNSLayerParametersLossBase](bnnslayerparameterslossbase.md)
  A structure that contains the parameters of a loss layer.
- [struct BNNSLayerParametersLossHuber](bnnslayerparameterslosshuber.md)
  A structure that contains the parameters of a Huber loss layer.
- [struct BNNSLayerParametersLossSigmoidCrossEntropy](bnnslayerparameterslosssigmoidcrossentropy.md)
  A structure that contains the parameters of a sigmoid cross entropy loss layer.
- [struct BNNSLayerParametersLossSoftmaxCrossEntropy](bnnslayerparameterslosssoftmaxcrossentropy.md)
  A structure that contains the parameters of a softmax cross entropy loss layer.
- [struct BNNSLayerParametersLossYolo](bnnslayerparameterslossyolo.md)
  A structure that contains the parameters of a You Only Look Once (YOLO) loss layer.
- [func BNNSFilterCreateLayerLoss(UnsafeRawPointer, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerloss(_:_:).md)
  Returns a new loss layer.
- [func BNNSLossFilterApplyBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeRawPointer, Int, UnsafeRawPointer?, Int, UnsafeMutableRawPointer, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, Int) -> Int32](bnnslossfilterapplybatch(_:_:_:_:_:_:_:_:_:_:_:).md)
  Applies a loss filter to a set of input objects, writing the result to a set of output objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslossfilterapplybackwardbatch(_:_:_:_:_:_:_:_:_:_:_:_:))*