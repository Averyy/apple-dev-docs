# init(type:reductionType:weight:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a loss descriptor with the loss function, reduction type, and weight you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init(type lossType: MLCLossType, reductionType: MLCReductionType, weight: Float)
```

```objc
+ (instancetype) descriptorWithType:(MLCLossType) lossType reductionType:(MLCReductionType) reductionType weight:(float) weight;
```

## Parameters

- `lossType`: The loss function type.
- `reductionType`: The reduction operation type.
- `weight`: A scalar floating-point weight value.

## See Also

### Creating Loss Descriptors
- [convenience init(type: MLCLossType, reductionType: MLCReductionType)](./init%28type,reductiontype%29.md)
  Creates a loss descriptor with the loss function and reduction type you specify.
- [convenience init(type: MLCLossType, reductionType: MLCReductionType, weight: Float, labelSmoothing: Float, classCount: Int)](./init%28type,reductiontype,weight,labelsmoothing,classcount%29.md)
  Creates a loss descriptor with the loss function, reduction type, weight, label smoothing, and number of classes you specify.
- [convenience init(type: MLCLossType, reductionType: MLCReductionType, weight: Float, labelSmoothing: Float, classCount: Int, epsilon: Float, delta: Float)](./init%28type,reductiontype,weight,labelsmoothing,classcount,epsilon,delta%29.md)
  Creates a loss descriptor with the loss function, reduction type, weight, label smoothing, and number of classes, epsilon, and delta that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclossdescriptor/init(type:reductiontype:weight:))*