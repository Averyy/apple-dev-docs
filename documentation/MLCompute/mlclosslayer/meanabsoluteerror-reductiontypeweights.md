# meanAbsoluteError(reductionType:weights:)

**Framework**: ML Compute  
**Kind**: method

Creates a mean absolute loss layer with the reduction type and weights you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class func meanAbsoluteError(reductionType: MLCReductionType, weights: MLCTensor?) -> Self
```

#### Return Value

A mean absolute loss layer.

## Parameters

- `reductionType`: The reduction operation type.
- `weights`: The loss label weights tensor.

## See Also

- [class func softmaxCrossEntropy(reductionType: MLCReductionType, labelSmoothing: Float, classCount: Int, weights: MLCTensor?) -> Self](mlclosslayer/softmaxcrossentropy(reductiontype:labelsmoothing:classcount:weights:).md)
  Creates a softmax cross entropy loss layer with the reduction type, label smoothing, number of classes, and weights you specify.
- [class func categoricalCrossEntropy(reductionType: MLCReductionType, labelSmoothing: Float, classCount: Int, weights: MLCTensor?) -> Self](mlclosslayer/categoricalcrossentropy(reductiontype:labelsmoothing:classcount:weights:).md)
  Creates a categorical cross entropy loss layer with the reduction type, label smoothing, number of classes, and weights you specify.
- [class func sigmoidCrossEntropy(reductionType: MLCReductionType, labelSmoothing: Float, weights: MLCTensor?) -> Self](mlclosslayer/sigmoidcrossentropy(reductiontype:labelsmoothing:weights:).md)
  Creates a sigmoid cross entropy loss layer with the reduction type, label smoothing, and weights you specify.
- [class func log(reductionType: MLCReductionType, epsilon: Float, weights: MLCTensor?) -> Self](mlclosslayer/log(reductiontype:epsilon:weights:).md)
  Creates a log loss layer with the reduction type, epsilon, and weights you specify.
- [class func huberLoss(reductionType: MLCReductionType, delta: Float, weights: MLCTensor?) -> Self](mlclosslayer/huberloss(reductiontype:delta:weights:).md)
  Creates a huber loss layer with the reduction type, delta, and weights you specify.
- [class func meanSquaredError(reductionType: MLCReductionType, weights: MLCTensor?) -> Self](mlclosslayer/meansquarederror(reductiontype:weights:).md)
  Creates a mean squared loss layer with the reduction type and weights you specify.
- [class func hingeLoss(reductionType: MLCReductionType, weights: MLCTensor?) -> Self](mlclosslayer/hingeloss(reductiontype:weights:).md)
  Creates a hinge loss layer with the reduction type and weights you specify.
- [class func cosineDistance(reductionType: MLCReductionType, weights: MLCTensor?) -> Self](mlclosslayer/cosinedistance(reductiontype:weights:).md)
  Creates a cosine distance loss layer with the reduction type and weights you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclosslayer/meanabsoluteerror(reductiontype:weights:))*