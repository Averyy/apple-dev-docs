# classCount

**Framework**: ML Compute  
**Kind**: property

The number of classes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
var classCount: Int { get }
```

#### Discussion

The default value is 1.

> **Note**:  This is only valid for the loss function type [`MLCLossType.softmaxCrossEntropy`](mlclosstype/softmaxcrossentropy.md).

 This is only valid for the loss function type [`MLCLossType.softmaxCrossEntropy`](mlclosstype/softmaxcrossentropy.md).

## See Also

- [var lossType: MLCLossType](mlclossdescriptor/losstype.md)
  The loss function type.
- [var reductionType: MLCReductionType](mlclossdescriptor/reductiontype.md)
  The reduction operation performed by the loss function.
- [var weight: Float](mlclossdescriptor/weight.md)
  The scale factor you apply to each element of a result.
- [var labelSmoothing: Float](mlclossdescriptor/labelsmoothing.md)
  The value for label smoothing.
- [var epsilon: Float](mlclossdescriptor/epsilon.md)
  The epsilon value.
- [var delta: Float](mlclossdescriptor/delta.md)
  The delta value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclossdescriptor/classcount)*