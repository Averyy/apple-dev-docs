# weight

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The scale factor you apply to each element of a result.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var weight: Float { get }
```

```objc
@property (nonatomic, readonly) float weight;
```

## Discussion

The default value is `1.0`.

## See Also

### Inspecting Loss Descriptors
- [var lossType: MLCLossType](./losstype.md)
  The loss function type.
- [var reductionType: MLCReductionType](./reductiontype.md)
  The reduction operation performed by the loss function.
- [var labelSmoothing: Float](./labelsmoothing.md)
  The value for label smoothing.
- [var classCount: Int](./classcount.md)
  The number of classes.
- [var epsilon: Float](./epsilon.md)
  The epsilon value.
- [var delta: Float](./delta.md)
  The delta value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclossdescriptor/weight)*