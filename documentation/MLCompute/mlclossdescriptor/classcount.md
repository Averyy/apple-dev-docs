# classCount

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The number of classes.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var classCount: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger classCount;
```

## Discussion

The default value is 1.

> **Note**:  This is only valid for the loss function type [`MLCLossType.softmaxCrossEntropy`](../mlclosstype/softmaxcrossentropy.md).

## See Also

### Inspecting Loss Descriptors
- [var lossType: MLCLossType](./losstype.md)
  The loss function type.
- [var reductionType: MLCReductionType](./reductiontype.md)
  The reduction operation performed by the loss function.
- [var weight: Float](./weight.md)
  The scale factor you apply to each element of a result.
- [var labelSmoothing: Float](./labelsmoothing.md)
  The value for label smoothing.
- [var epsilon: Float](./epsilon.md)
  The epsilon value.
- [var delta: Float](./delta.md)
  The delta value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclossdescriptor/classcount)*