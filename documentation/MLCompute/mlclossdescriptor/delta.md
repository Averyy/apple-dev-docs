# delta

**Framework**: Mlcompute  
**Kind**: property

The delta value.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
var delta: Float { get }
```

#### Discussion

The default value is `1.0`.

> **Note**:  This is only valid for the loss function type [`MLCLossType.huber`](mlclosstype/huber.md).

## See Also

- [var lossType: MLCLossType](mlclossdescriptor/losstype.md)
  The loss function type.
- [var reductionType: MLCReductionType](mlclossdescriptor/reductiontype.md)
  The reduction operation performed by the loss function.
- [var weight: Float](mlclossdescriptor/weight.md)
  The scale factor you apply to each element of a result.
- [var labelSmoothing: Float](mlclossdescriptor/labelsmoothing.md)
  The value for label smoothing.
- [var classCount: Int](mlclossdescriptor/classcount.md)
  The number of classes.
- [var epsilon: Float](mlclossdescriptor/epsilon.md)
  The epsilon value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/MLCompute/mlclossdescriptor/delta)*