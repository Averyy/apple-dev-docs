# init(type:reductionType:)

**Framework**: ML Compute  
**Kind**: init

Creates a loss descriptor with the loss function and reduction type you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init(type lossType: MLCLossType, reductionType: MLCReductionType)
```

## Parameters

- `lossType`: The loss function type.
- `reductionType`: The reduction operation type.

## See Also

- [convenience init(type: MLCLossType, reductionType: MLCReductionType, weight: Float)](mlclossdescriptor/init(type:reductiontype:weight:).md)
  Creates a loss descriptor with the loss function, reduction type, and weight you specify.
- [convenience init(type: MLCLossType, reductionType: MLCReductionType, weight: Float, labelSmoothing: Float, classCount: Int)](mlclossdescriptor/init(type:reductiontype:weight:labelsmoothing:classcount:).md)
  Creates a loss descriptor with the loss function, reduction type, weight, label smoothing, and number of classes you specify.
- [convenience init(type: MLCLossType, reductionType: MLCReductionType, weight: Float, labelSmoothing: Float, classCount: Int, epsilon: Float, delta: Float)](mlclossdescriptor/init(type:reductiontype:weight:labelsmoothing:classcount:epsilon:delta:).md)
  Creates a loss descriptor with the loss function, reduction type, weight, label smoothing, and number of classes, epsilon, and delta that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclossdescriptor/init(type:reductiontype:))*