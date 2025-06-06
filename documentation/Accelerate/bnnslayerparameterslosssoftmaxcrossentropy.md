# BNNSLayerParametersLossSoftmaxCrossEntropy

**Framework**: Accelerate  
**Kind**: struct

A structure that contains the parameters of a softmax cross entropy loss layer.

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
struct BNNSLayerParametersLossSoftmaxCrossEntropy
```

## Topics

### Initializers
- [init(function: BNNSLossFunction, i_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, reduction: BNNSLossReductionFunction, label_smooth: Float)](bnnslayerparameterslosssoftmaxcrossentropy/init(function:i_desc:o_desc:reduction:label_smooth:).md)
  Returns a new softmax cross entropy loss layer parameters structure from the specified parameters.
- [init()](bnnslayerparameterslosssoftmaxcrossentropy/init.md)
  Returns a new softmax cross entropy loss layer parameters structure.
### Instance Properties
- [var function: BNNSLossFunction](bnnslayerparameterslosssoftmaxcrossentropy/function.md)
  The function that’s used to compute loss.
- [var i_desc: BNNSNDArrayDescriptor](bnnslayerparameterslosssoftmaxcrossentropy/i_desc.md)
  The descriptor of the input.
- [var o_desc: BNNSNDArrayDescriptor](bnnslayerparameterslosssoftmaxcrossentropy/o_desc.md)
  The descriptor of the output.
- [var reduction: BNNSLossReductionFunction](bnnslayerparameterslosssoftmaxcrossentropy/reduction.md)
  The function that’s used to reduce the computed loss.
- [var label_smooth: Float](bnnslayerparameterslosssoftmaxcrossentropy/label_smooth.md)
  A value that defines the smoothing that the loss function applies to the labels.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

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
- [struct BNNSLayerParametersLossYolo](bnnslayerparameterslossyolo.md)
  A structure that contains the parameters of a You Only Look Once (YOLO) loss layer.
- [func BNNSFilterCreateLayerLoss(UnsafeRawPointer, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerloss(_:_:).md)
  Returns a new loss layer.
- [func BNNSLossFilterApplyBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeRawPointer, Int, UnsafeRawPointer?, Int, UnsafeMutableRawPointer, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, Int) -> Int32](bnnslossfilterapplybatch(_:_:_:_:_:_:_:_:_:_:_:).md)
  Applies a loss filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSLossFilterApplyBackwardBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafeRawPointer, Int, UnsafeRawPointer?, Int, UnsafePointer<BNNSNDArrayDescriptor>, Int) -> Int32](bnnslossfilterapplybackwardbatch(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Applies a loss filter backward to generate gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterslosssoftmaxcrossentropy)*