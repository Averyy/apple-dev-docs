# BNNS.LossFunction.huber(huberDelta:)

**Framework**: Accelerate  
**Kind**: case  
**Role**: Case

Huber loss computation between input logits and one-hot encoded labels.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
case huber(huberDelta: Float)
```

## See Also

### Loss Functions
- [BNNS.LossFunction.categoricalCrossEntropy](./categoricalcrossentropy.md)
  Categorical cross-entropy computation between input prediction and labels.
- [BNNS.LossFunction.cosineDistance](./cosinedistance.md)
  Cosine distance loss computation between input predictions and labels.
- [BNNS.LossFunction.hinge](./hinge.md)
  Hinge loss computation between labels and unbounded, zero-centered binary predictions.
- [BNNS.LossFunction.log](./log.md)
  Log loss computation between labels and predictions.
- [BNNS.LossFunction.meanAbsoluteError](./meanabsoluteerror.md)
  Mean absolute error (MAE) computation between input prediction and labels.
- [BNNS.LossFunction.meanSquareError](./meansquareerror.md)
  Mean square error (MSE) computation between input logits and one-hot encoded labels.
- [BNNS.LossFunction.sigmoidCrossEntropy(labelSmoothing:)](./sigmoidcrossentropy%28labelsmoothing%29.md)
  Sigmoid activation on input logits, and independent computation of cross-entropy loss for each class.
- [BNNS.LossFunction.softmaxCrossEntropy(labelSmoothing:)](./softmaxcrossentropy%28labelsmoothing%29.md)
  Softmax activation on input logits, and computation of cross-entropy loss with one-hot encoded labels.
- [case yolo(parameters: BNNS.LossFunction.YoloParameters)](./yolo%28parameters%29.md)
  You Only Look Once (YOLO) loss computation between prediction and ground truth labels.
- [BNNS.LossFunction.YoloParameters](./yoloparameters.md)
  A structure that contains the parameters for You Only Look Once (YOLO) loss computation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/lossfunction/huber(huberdelta:))*