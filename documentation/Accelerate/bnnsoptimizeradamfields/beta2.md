# beta2

**Framework**: Accelerate  
**Kind**: property

A value that specifies the second moment constant in the range 0 to 1.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var beta2: Float
```

## See Also

- [var learning_rate: Float](bnnsoptimizeradamfields/learning_rate.md)
  A value that specifies the learning rate.
- [var beta1: Float](bnnsoptimizeradamfields/beta1.md)
  A value that specifies the first moment constant in the range 0 to 1.
- [var time_step: Float](bnnsoptimizeradamfields/time_step.md)
  A value that represents the optimizer’s current time and you’re responsible for updating after optimizing all the layer parameters in your network.
- [var epsilon: Float](bnnsoptimizeradamfields/epsilon.md)
  An addition for the division in the parameter update stage.
- [var gradient_scale: Float](bnnsoptimizeradamfields/gradient_scale.md)
  A value that specifies the gradient scaling factor.
- [var regularization_scale: Float](bnnsoptimizeradamfields/regularization_scale.md)
  A value that specifies the regularization scaling factor.
- [var clip_gradients: Bool](bnnsoptimizeradamfields/clip_gradients.md)
  A Boolean value that specifies whether to clip the gradient between minimum and maximum values.
- [var clip_gradients_min: Float](bnnsoptimizeradamfields/clip_gradients_min.md)
  The values for the minimum gradient.
- [var clip_gradients_max: Float](bnnsoptimizeradamfields/clip_gradients_max.md)
  The values for the maximum gradient.
- [var regularization_func: BNNSOptimizerRegularizationFunction](bnnsoptimizeradamfields/regularization_func.md)
  The variable that specifies the regularization function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsoptimizeradamfields/beta2)*