# softmaxCrossEntropy(reductionType:labelSmoothing:classCount:weights:)

**Framework**: ML Compute  
**Kind**: method  
**Role**: Type Method

Creates a softmax cross entropy loss layer with the reduction type, label smoothing, number of classes, and weights you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class func softmaxCrossEntropy(reductionType: MLCReductionType, labelSmoothing: Float, classCount: Int, weights: MLCTensor?) -> Self
```

```objc
+ (instancetype) softmaxCrossEntropyLossWithReductionType:(MLCReductionType) reductionType labelSmoothing:(float) labelSmoothing classCount:(NSUInteger) classCount weights:(MLCTensor *) weights;
```

## Return Value

A softmax cross entropy loss layer.

## Parameters

- `reductionType`: The reduction operation type.
- `labelSmoothing`: Label smoothing value.
- `classCount`: The number of classes.
- `weights`: The loss label weights tensor.

## See Also

### Creating Loss Layers with Tensor Weights
- [class func categoricalCrossEntropy(reductionType: MLCReductionType, labelSmoothing: Float, classCount: Int, weights: MLCTensor?) -> Self](./categoricalcrossentropy%28reductiontype,labelsmoothing,classcount,weights%29.md)
  Creates a categorical cross entropy loss layer with the reduction type, label smoothing, number of classes, and weights you specify.
- [class func sigmoidCrossEntropy(reductionType: MLCReductionType, labelSmoothing: Float, weights: MLCTensor?) -> Self](./sigmoidcrossentropy%28reductiontype,labelsmoothing,weights%29.md)
  Creates a sigmoid cross entropy loss layer with the reduction type, label smoothing, and weights you specify.
- [class func log(reductionType: MLCReductionType, epsilon: Float, weights: MLCTensor?) -> Self](./log%28reductiontype,epsilon,weights%29.md)
  Creates a log loss layer with the reduction type, epsilon, and weights you specify.
- [class func huberLoss(reductionType: MLCReductionType, delta: Float, weights: MLCTensor?) -> Self](./huberloss%28reductiontype,delta,weights%29.md)
  Creates a huber loss layer with the reduction type, delta, and weights you specify.
- [class func meanAbsoluteError(reductionType: MLCReductionType, weights: MLCTensor?) -> Self](./meanabsoluteerror%28reductiontype,weights%29.md)
  Creates a mean absolute loss layer with the reduction type and weights you specify.
- [class func meanSquaredError(reductionType: MLCReductionType, weights: MLCTensor?) -> Self](./meansquarederror%28reductiontype,weights%29.md)
  Creates a mean squared loss layer with the reduction type and weights you specify.
- [class func hingeLoss(reductionType: MLCReductionType, weights: MLCTensor?) -> Self](./hingeloss%28reductiontype,weights%29.md)
  Creates a hinge loss layer with the reduction type and weights you specify.
- [class func cosineDistance(reductionType: MLCReductionType, weights: MLCTensor?) -> Self](./cosinedistance%28reductiontype,weights%29.md)
  Creates a cosine distance loss layer with the reduction type and weights you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclosslayer/softmaxcrossentropy(reductiontype:labelsmoothing:classcount:weights:))*