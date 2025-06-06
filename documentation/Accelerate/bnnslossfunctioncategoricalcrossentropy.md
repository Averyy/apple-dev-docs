# BNNSLossFunctionCategoricalCrossEntropy

**Framework**: Accelerate  
**Kind**: var

Performs categorical cross entropy computation between input prediction and labels.

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
var BNNSLossFunctionCategoricalCrossEntropy: BNNSLossFunction { get }
```

#### Discussion

[`BNNSLossFunctionCategoricalCrossEntropy`](bnnslossfunctioncategoricalcrossentropy.md) performs categorical cross entropy (that is, softmax activation plus a cross entropy loss) computation between input prediction and labels.

You can scale the loss with either a scalar value or weight matrix, and reduce the loss according to a reduction function.

## See Also

- [init(UInt32)](bnnslossfunction/init(_:).md)
- [init(rawValue: UInt32)](bnnslossfunction/init(rawvalue:).md)
- [var rawValue: UInt32](bnnslossfunction/rawvalue.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslossfunctioncategoricalcrossentropy)*