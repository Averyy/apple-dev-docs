# BNNSLossFunction

**Framework**: Accelerate  
**Kind**: struct

Constants that describe loss functions.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct BNNSLossFunction
```

## Topics

### Loss Functions
- [init(UInt32)](bnnslossfunction/init(_:).md)
- [init(rawValue: UInt32)](bnnslossfunction/init(rawvalue:).md)
- [var rawValue: UInt32](bnnslossfunction/rawvalue.md)
- [var BNNSLossFunctionCategoricalCrossEntropy: BNNSLossFunction](bnnslossfunctioncategoricalcrossentropy.md)
  Performs categorical cross entropy computation between input prediction and labels.
- [var BNNSLossFunctionCosineDistance: BNNSLossFunction](bnnslossfunctioncosinedistance.md)
  Performs cosine distance loss computation between input predictions and labels.
- [var BNNSLossFunctionHinge: BNNSLossFunction](bnnslossfunctionhinge.md)
  Performs Hinge loss computation between labels and unbounded zero-centered binary predictions.
- [var BNNSLossFunctionHuber: BNNSLossFunction](bnnslossfunctionhuber.md)
  Huber loss computation between input logits and one-hot encoded labels.
- [var BNNSLossFunctionLog: BNNSLossFunction](bnnslossfunctionlog.md)
  Log loss computation between labels and predictions.
- [var BNNSLossFunctionMeanAbsoluteError: BNNSLossFunction](bnnslossfunctionmeanabsoluteerror.md)
  Mean absolute error (MAE) computation between input prediction and labels.
- [var BNNSLossFunctionMeanSquareError: BNNSLossFunction](bnnslossfunctionmeansquareerror.md)
  Mean square error (MSE) computation between input logits and one-hot encoded labels.
- [var BNNSLossFunctionSigmoidCrossEntropy: BNNSLossFunction](bnnslossfunctionsigmoidcrossentropy.md)
  Sigmoid activation on input logits, and independent computation of cross-entropy loss for each class.
- [var BNNSLossFunctionSoftmaxCrossEntropy: BNNSLossFunction](bnnslossfunctionsoftmaxcrossentropy.md)
  Softmax activation on input logits, and computation of cross-entropy loss with one-hot encoded labels.
- [var BNNSLossFunctionYolo: BNNSLossFunction](bnnslossfunctionyolo.md)
  You Only Look Once (YOLO) loss computation between prediction and ground truth labels.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class LossLayer](bnns/losslayer.md)
  A layer object that wraps a loss filter and manages its deinitialization.
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
- [func BNNSLossFilterApplyBackwardBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafeRawPointer, Int, UnsafeRawPointer?, Int, UnsafePointer<BNNSNDArrayDescriptor>, Int) -> Int32](bnnslossfilterapplybackwardbatch(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Applies a loss filter backward to generate gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslossfunction)*