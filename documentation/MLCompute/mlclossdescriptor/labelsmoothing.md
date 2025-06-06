# labelSmoothing

**Framework**: ML Compute  
**Kind**: property

The value for label smoothing.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
var labelSmoothing: Float { get }
```

#### Discussion

The default value is `1.0`.

> **Note**:  This is only valid for the following loss function types: [`MLCLossType.softmaxCrossEntropy`](mlclosstype/softmaxcrossentropy.md) [`MLCLossType.sigmoidCrossEntropy`](mlclosstype/sigmoidcrossentropy.md)

 This is only valid for the following loss function types:

[`MLCLossType.softmaxCrossEntropy`](mlclosstype/softmaxcrossentropy.md)

[`MLCLossType.sigmoidCrossEntropy`](mlclosstype/sigmoidcrossentropy.md)

## See Also

- [var lossType: MLCLossType](mlclossdescriptor/losstype.md)
  The loss function type.
- [var reductionType: MLCReductionType](mlclossdescriptor/reductiontype.md)
  The reduction operation performed by the loss function.
- [var weight: Float](mlclossdescriptor/weight.md)
  The scale factor you apply to each element of a result.
- [var classCount: Int](mlclossdescriptor/classcount.md)
  The number of classes.
- [var epsilon: Float](mlclossdescriptor/epsilon.md)
  The epsilon value.
- [var delta: Float](mlclossdescriptor/delta.md)
  The delta value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclossdescriptor/labelsmoothing)*