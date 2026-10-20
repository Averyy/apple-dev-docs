# learning_rate

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

A value that specifies the learning rate.

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
var learning_rate: Float
```

```c
float learning_rate;
```

## See Also

### Instance Properties
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
- [var regularization_func: BNNSOptimizerRegularizationFunction](./regularization_func.md)
  The variable that specifies the regularization function.
- [var clipping_func: BNNSOptimizerClippingFunction](./clipping_func.md)
  The clipping function.
- [struct BNNSOptimizerClippingFunction](../bnnsoptimizerclippingfunction.md)
  Constants that describe clipping functions.
- [var clip_gradients_min: Float](./clip_gradients_min.md)
  The minimum clipping value for clipping by value.
- [var clip_gradients_max: Float](./clip_gradients_max.md)
  The maximum clipping value for clipping by value.
- [var clip_gradients_max_norm: Float](./clip_gradients_max_norm.md)
  The maximum Euclidean norm for clipping by norm and clipping by global norm.
- [var clip_gradients_use_norm: Float](./clip_gradients_use_norm.md)
  An optional value for a known Euclidean norm for clipping by global norm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsoptimizerrmspropwithclippingfields/learning_rate)*