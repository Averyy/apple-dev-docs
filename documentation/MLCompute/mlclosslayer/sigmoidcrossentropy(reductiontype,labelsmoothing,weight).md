# sigmoidCrossEntropy(reductionType:labelSmoothing:weight:)

**Framework**: ML Compute  
**Kind**: method  
**Role**: Type Method

Creates a sigmoid cross entropy loss layer with the reduction type, label smoothing, and weight you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class func sigmoidCrossEntropy(reductionType: MLCReductionType, labelSmoothing: Float, weight: Float) -> Self
```

```objc
+ (instancetype) sigmoidCrossEntropyLossWithReductionType:(MLCReductionType) reductionType labelSmoothing:(float) labelSmoothing weight:(float) weight;
```

## Return Value

A sigmoid cross entropy loss layer.

## Parameters

- `reductionType`: The reduction operation type.
- `labelSmoothing`: The value for label smoothing.
- `weight`: A scalar floating-point weight value.

## See Also

### Creating Loss Layers with Scalar Weights
- [class func softmaxCrossEntropy(reductionType: MLCReductionType, labelSmoothing: Float, classCount: Int, weight: Float) -> Self](./softmaxcrossentropy%28reductiontype,labelsmoothing,classcount,weight%29.md)
  Creates a softmax cross entropy loss layer with the reduction type, label smoothing, number of classes, and weight you specify.
- [class func categoricalCrossEntropy(reductionType: MLCReductionType, labelSmoothing: Float, classCount: Int, weight: Float) -> Self](./categoricalcrossentropy%28reductiontype,labelsmoothing,classcount,weight%29.md)
  Creates a categorical cross entropy loss layer with the reduction type, label smoothing, number of classes, and weight you specify.
- [class func log(reductionType: MLCReductionType, epsilon: Float, weight: Float) -> Self](./log%28reductiontype,epsilon,weight%29.md)
  Creates a log loss layer with the reduction type, epsilon, and weight you specify.
- [class func huberLoss(reductionType: MLCReductionType, delta: Float, weight: Float) -> Self](./huberloss%28reductiontype,delta,weight%29.md)
  Creates a huber loss layer with the reduction type, delta, and weight you specify.
- [class func meanAbsoluteError(reductionType: MLCReductionType, weight: Float) -> Self](./meanabsoluteerror%28reductiontype,weight%29.md)
  Creates a mean absolute loss layer with the reduction type and weight.
- [class func meanSquaredError(reductionType: MLCReductionType, weight: Float) -> Self](./meansquarederror%28reductiontype,weight%29.md)
  Creates a mean squared loss layer with the reduction type and weight you specify.
- [class func hingeLoss(reductionType: MLCReductionType, weight: Float) -> Self](./hingeloss%28reductiontype,weight%29.md)
  Creates a hinge loss layer with the reduction type and weight you specify.
- [class func cosineDistance(reductionType: MLCReductionType, weight: Float) -> Self](./cosinedistance%28reductiontype,weight%29.md)
  Creates a cosine distance loss layer with the reduction type and weight you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclosslayer/sigmoidcrossentropy(reductiontype:labelsmoothing:weight:))*