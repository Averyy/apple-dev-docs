# BNNS.LossFunction.softmaxCrossEntropy(labelSmoothing:)

**Framework**: Accelerate  
**Kind**: case

Softmax activation on input logits, and computation of cross-entropy loss with one-hot encoded labels.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- watchOS 7.0+
- Unknown ?+ - Deprecated
- visionOS ?+

## Declaration

```swift
case softmaxCrossEntropy(labelSmoothing: Float)
```

## See Also

- [BNNS.LossFunction.categoricalCrossEntropy](bnns/lossfunction/categoricalcrossentropy.md)
  Categorical cross-entropy computation between input prediction and labels.
- [BNNS.LossFunction.cosineDistance](bnns/lossfunction/cosinedistance.md)
  Cosine distance loss computation between input predictions and labels.
- [BNNS.LossFunction.hinge](bnns/lossfunction/hinge.md)
  Hinge loss computation between labels and unbounded, zero-centered binary predictions.
- [BNNS.LossFunction.huber(huberDelta:)](bnns/lossfunction/huber(huberdelta:).md)
  Huber loss computation between input logits and one-hot encoded labels.
- [BNNS.LossFunction.log](bnns/lossfunction/log.md)
  Log loss computation between labels and predictions.
- [BNNS.LossFunction.meanAbsoluteError](bnns/lossfunction/meanabsoluteerror.md)
  Mean absolute error (MAE) computation between input prediction and labels.
- [BNNS.LossFunction.meanSquareError](bnns/lossfunction/meansquareerror.md)
  Mean square error (MSE) computation between input logits and one-hot encoded labels.
- [BNNS.LossFunction.sigmoidCrossEntropy(labelSmoothing:)](bnns/lossfunction/sigmoidcrossentropy(labelsmoothing:).md)
  Sigmoid activation on input logits, and independent computation of cross-entropy loss for each class.
- [case yolo(parameters: BNNS.LossFunction.YoloParameters)](bnns/lossfunction/yolo(parameters:).md)
  You Only Look Once (YOLO) loss computation between prediction and ground truth labels.
- [BNNS.LossFunction.YoloParameters](bnns/lossfunction/yoloparameters.md)
  A structure that contains the parameters for You Only Look Once (YOLO) loss computation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/lossfunction/softmaxcrossentropy(labelsmoothing:))*