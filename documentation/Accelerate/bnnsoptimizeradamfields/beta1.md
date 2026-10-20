# beta1

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

A value that specifies the first moment constant in the range 0 to 1.

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
var beta1: Float
```

```c
float beta1;
```

## See Also

### Instance Properties
- [var learning_rate: Float](./learning_rate.md)
  A value that specifies the learning rate.
- [var beta2: Float](./beta2.md)
  A value that specifies the second moment constant in the range 0 to 1.
- [var time_step: Float](./time_step.md)
  A value that represents the optimizer’s current time and you’re responsible for updating after optimizing all the layer parameters in your network.
- [var epsilon: Float](./epsilon.md)
  An addition for the division in the parameter update stage.
- [var gradient_scale: Float](./gradient_scale.md)
  A value that specifies the gradient scaling factor.
- [var regularization_scale: Float](./regularization_scale.md)
  A value that specifies the regularization scaling factor.
- [var clip_gradients: Bool](./clip_gradients.md)
  A Boolean value that specifies whether to clip the gradient between minimum and maximum values.
- [var clip_gradients_min: Float](./clip_gradients_min.md)
  The values for the minimum gradient.
- [var clip_gradients_max: Float](./clip_gradients_max.md)
  The values for the maximum gradient.
- [var regularization_func: BNNSOptimizerRegularizationFunction](./regularization_func.md)
  The variable that specifies the regularization function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsoptimizeradamfields/beta1)*