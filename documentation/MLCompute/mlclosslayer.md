# MLCLossLayer

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A layer that estimates the inaccuracies of the model to reduce the loss on the next evaluation.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCLossLayer
```

```objc
@interface MLCLossLayer : MLCLayer
```

## Topics

### Creating Loss Layers with Descriptors
- [convenience init(descriptor: MLCLossDescriptor)](./mlclosslayer/init%28descriptor%29.md)
  Creates a loss layer with the descriptor you specify.
- [convenience init(descriptor: MLCLossDescriptor, weights: MLCTensor)](./mlclosslayer/init%28descriptor,weights%29.md)
  Creates a loss layer with the descriptor and weights you specify.
- [class MLCLossDescriptor](./mlclossdescriptor.md)
  A configuration object you use to create a loss layer.
- [enum MLCLossType](./mlclosstype.md)
  A loss function.
### Creating Loss Layers with Scalar Weights
- [class func softmaxCrossEntropy(reductionType: MLCReductionType, labelSmoothing: Float, classCount: Int, weight: Float) -> Self](./mlclosslayer/softmaxcrossentropy%28reductiontype,labelsmoothing,classcount,weight%29.md)
  Creates a softmax cross entropy loss layer with the reduction type, label smoothing, number of classes, and weight you specify.
- [class func categoricalCrossEntropy(reductionType: MLCReductionType, labelSmoothing: Float, classCount: Int, weight: Float) -> Self](./mlclosslayer/categoricalcrossentropy%28reductiontype,labelsmoothing,classcount,weight%29.md)
  Creates a categorical cross entropy loss layer with the reduction type, label smoothing, number of classes, and weight you specify.
- [class func sigmoidCrossEntropy(reductionType: MLCReductionType, labelSmoothing: Float, weight: Float) -> Self](./mlclosslayer/sigmoidcrossentropy%28reductiontype,labelsmoothing,weight%29.md)
  Creates a sigmoid cross entropy loss layer with the reduction type, label smoothing, and weight you specify.
- [class func log(reductionType: MLCReductionType, epsilon: Float, weight: Float) -> Self](./mlclosslayer/log%28reductiontype,epsilon,weight%29.md)
  Creates a log loss layer with the reduction type, epsilon, and weight you specify.
- [class func huberLoss(reductionType: MLCReductionType, delta: Float, weight: Float) -> Self](./mlclosslayer/huberloss%28reductiontype,delta,weight%29.md)
  Creates a huber loss layer with the reduction type, delta, and weight you specify.
- [class func meanAbsoluteError(reductionType: MLCReductionType, weight: Float) -> Self](./mlclosslayer/meanabsoluteerror%28reductiontype,weight%29.md)
  Creates a mean absolute loss layer with the reduction type and weight.
- [class func meanSquaredError(reductionType: MLCReductionType, weight: Float) -> Self](./mlclosslayer/meansquarederror%28reductiontype,weight%29.md)
  Creates a mean squared loss layer with the reduction type and weight you specify.
- [class func hingeLoss(reductionType: MLCReductionType, weight: Float) -> Self](./mlclosslayer/hingeloss%28reductiontype,weight%29.md)
  Creates a hinge loss layer with the reduction type and weight you specify.
- [class func cosineDistance(reductionType: MLCReductionType, weight: Float) -> Self](./mlclosslayer/cosinedistance%28reductiontype,weight%29.md)
  Creates a cosine distance loss layer with the reduction type and weight you specify.
### Creating Loss Layers with Tensor Weights
- [class func softmaxCrossEntropy(reductionType: MLCReductionType, labelSmoothing: Float, classCount: Int, weights: MLCTensor?) -> Self](./mlclosslayer/softmaxcrossentropy%28reductiontype,labelsmoothing,classcount,weights%29.md)
  Creates a softmax cross entropy loss layer with the reduction type, label smoothing, number of classes, and weights you specify.
- [class func categoricalCrossEntropy(reductionType: MLCReductionType, labelSmoothing: Float, classCount: Int, weights: MLCTensor?) -> Self](./mlclosslayer/categoricalcrossentropy%28reductiontype,labelsmoothing,classcount,weights%29.md)
  Creates a categorical cross entropy loss layer with the reduction type, label smoothing, number of classes, and weights you specify.
- [class func sigmoidCrossEntropy(reductionType: MLCReductionType, labelSmoothing: Float, weights: MLCTensor?) -> Self](./mlclosslayer/sigmoidcrossentropy%28reductiontype,labelsmoothing,weights%29.md)
  Creates a sigmoid cross entropy loss layer with the reduction type, label smoothing, and weights you specify.
- [class func log(reductionType: MLCReductionType, epsilon: Float, weights: MLCTensor?) -> Self](./mlclosslayer/log%28reductiontype,epsilon,weights%29.md)
  Creates a log loss layer with the reduction type, epsilon, and weights you specify.
- [class func huberLoss(reductionType: MLCReductionType, delta: Float, weights: MLCTensor?) -> Self](./mlclosslayer/huberloss%28reductiontype,delta,weights%29.md)
  Creates a huber loss layer with the reduction type, delta, and weights you specify.
- [class func meanAbsoluteError(reductionType: MLCReductionType, weights: MLCTensor?) -> Self](./mlclosslayer/meanabsoluteerror%28reductiontype,weights%29.md)
  Creates a mean absolute loss layer with the reduction type and weights you specify.
- [class func meanSquaredError(reductionType: MLCReductionType, weights: MLCTensor?) -> Self](./mlclosslayer/meansquarederror%28reductiontype,weights%29.md)
  Creates a mean squared loss layer with the reduction type and weights you specify.
- [class func hingeLoss(reductionType: MLCReductionType, weights: MLCTensor?) -> Self](./mlclosslayer/hingeloss%28reductiontype,weights%29.md)
  Creates a hinge loss layer with the reduction type and weights you specify.
- [class func cosineDistance(reductionType: MLCReductionType, weights: MLCTensor?) -> Self](./mlclosslayer/cosinedistance%28reductiontype,weights%29.md)
  Creates a cosine distance loss layer with the reduction type and weights you specify.
### Inspecting Loss Layers
- [var descriptor: MLCLossDescriptor](./mlclosslayer/descriptor.md)
  The configuration object you use to create the loss layer.
- [var weights: MLCTensor?](./mlclosslayer/weights.md)
  The loss label weights tensor.

## Relationships

### Inherits From
- [MLCLayer](./mlclayer.md)
### Inherited By
- [MLCYOLOLossLayer](./mlcyololosslayer.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Loss Layers
- [class MLCYOLOLossLayer](./mlcyololosslayer.md)
  A layer that estimates loss for the YOLO algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclosslayer)*