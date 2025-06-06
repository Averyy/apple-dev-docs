# huberLoss(reductionType:delta:weight:)

**Framework**: ML Compute  
**Kind**: method

Creates a huber loss layer with the reduction type, delta, and weight you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class func huberLoss(reductionType: MLCReductionType, delta: Float, weight: Float) -> Self
```

#### Return Value

A huber loss layer.

## Parameters

- `reductionType`: The reduction operation type.
- `delta`: The delta value.
- `weight`: A scalar floating-point weight value.

## See Also

- [class func softmaxCrossEntropy(reductionType: MLCReductionType, labelSmoothing: Float, classCount: Int, weight: Float) -> Self](mlclosslayer/softmaxcrossentropy(reductiontype:labelsmoothing:classcount:weight:).md)
  Creates a softmax cross entropy loss layer with the reduction type, label smoothing, number of classes, and weight you specify.
- [class func categoricalCrossEntropy(reductionType: MLCReductionType, labelSmoothing: Float, classCount: Int, weight: Float) -> Self](mlclosslayer/categoricalcrossentropy(reductiontype:labelsmoothing:classcount:weight:).md)
  Creates a categorical cross entropy loss layer with the reduction type, label smoothing, number of classes, and weight you specify.
- [class func sigmoidCrossEntropy(reductionType: MLCReductionType, labelSmoothing: Float, weight: Float) -> Self](mlclosslayer/sigmoidcrossentropy(reductiontype:labelsmoothing:weight:).md)
  Creates a sigmoid cross entropy loss layer with the reduction type, label smoothing, and weight you specify.
- [class func log(reductionType: MLCReductionType, epsilon: Float, weight: Float) -> Self](mlclosslayer/log(reductiontype:epsilon:weight:).md)
  Creates a log loss layer with the reduction type, epsilon, and weight you specify.
- [class func meanAbsoluteError(reductionType: MLCReductionType, weight: Float) -> Self](mlclosslayer/meanabsoluteerror(reductiontype:weight:).md)
  Creates a mean absolute loss layer with the reduction type and weight.
- [class func meanSquaredError(reductionType: MLCReductionType, weight: Float) -> Self](mlclosslayer/meansquarederror(reductiontype:weight:).md)
  Creates a mean squared loss layer with the reduction type and weight you specify.
- [class func hingeLoss(reductionType: MLCReductionType, weight: Float) -> Self](mlclosslayer/hingeloss(reductiontype:weight:).md)
  Creates a hinge loss layer with the reduction type and weight you specify.
- [class func cosineDistance(reductionType: MLCReductionType, weight: Float) -> Self](mlclosslayer/cosinedistance(reductiontype:weight:).md)
  Creates a cosine distance loss layer with the reduction type and weight you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclosslayer/huberloss(reductiontype:delta:weight:))*