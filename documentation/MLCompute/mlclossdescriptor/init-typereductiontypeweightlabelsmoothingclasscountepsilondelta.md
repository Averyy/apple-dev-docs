# init(type:reductionType:weight:labelSmoothing:classCount:epsilon:delta:)

**Framework**: ML Compute  
**Kind**: init

Creates a loss descriptor with the loss function, reduction type, weight, label smoothing, and number of classes, epsilon, and delta that you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init(type lossType: MLCLossType, reductionType: MLCReductionType, weight: Float, labelSmoothing: Float, classCount: Int, epsilon: Float, delta: Float)
```

## Parameters

- `lossType`: The loss function type.
- `reductionType`: The reduction operation type.
- `weight`: A scalar floating-point weight value.
- `labelSmoothing`: The value for label smoothing.
- `classCount`: The number of classes.
- `epsilon`: The epsilon used by LogLoss.
- `delta`: The delta used by Huber loss.

## See Also

- [convenience init(type: MLCLossType, reductionType: MLCReductionType)](mlclossdescriptor/init(type:reductiontype:).md)
  Creates a loss descriptor with the loss function and reduction type you specify.
- [convenience init(type: MLCLossType, reductionType: MLCReductionType, weight: Float)](mlclossdescriptor/init(type:reductiontype:weight:).md)
  Creates a loss descriptor with the loss function, reduction type, and weight you specify.
- [convenience init(type: MLCLossType, reductionType: MLCReductionType, weight: Float, labelSmoothing: Float, classCount: Int)](mlclossdescriptor/init(type:reductiontype:weight:labelsmoothing:classcount:).md)
  Creates a loss descriptor with the loss function, reduction type, weight, label smoothing, and number of classes you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclossdescriptor/init(type:reductiontype:weight:labelsmoothing:classcount:epsilon:delta:))*