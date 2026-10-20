# clip_gradients_min

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The values for the minimum gradient.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 14.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use BNNSGraph* APIs

## Declaration

```swift
var clip_gradients_min: Float
```

```c
float clip_gradients_min;
```

## See Also

### Instance Properties
- [var learning_rate: Float](./learning_rate.md)
  A value that specifies the learning rate.
- [var alpha: Float](./alpha.md)
  A constant that specifies smoothing.
- [var epsilon: Float](./epsilon.md)
  A term that the optimizer adds to the denominator.
- [var centered: Bool](./centered.md)
  A Boolean value that specifies whether to use the centered variant.
- [var momentum: Float](./momentum.md)
  The rate of momentum decay.
- [var gradient_scale: Float](./gradient_scale.md)
  A value that specifies the gradient scaling factor.
- [var regularization_scale: Float](./regularization_scale.md)
  A value that specifies the regularization scaling factor.
- [var clip_gradients: Bool](./clip_gradients.md)
  A Boolean value that specifies whether to clip the gradient between minimum and maximum values.
- [var clip_gradients_max: Float](./clip_gradients_max.md)
  The values for the maximum gradient.
- [var regularization_func: BNNSOptimizerRegularizationFunction](./regularization_func.md)
  The variable that specifies the regularization function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsoptimizerrmspropfields/clip_gradients_min)*