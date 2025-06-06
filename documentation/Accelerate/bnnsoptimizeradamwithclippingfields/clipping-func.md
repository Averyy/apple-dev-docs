# clipping_func

**Framework**: Accelerate  
**Kind**: property

The clipping function.

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
var clipping_func: BNNSOptimizerClippingFunction
```

## See Also

- [var learning_rate: Float](bnnsoptimizeradamwithclippingfields/learning_rate.md)
  A value that specifies the learning rate.
- [var beta1: Float](bnnsoptimizeradamwithclippingfields/beta1.md)
  A value that specifies the first moment constant in the range 0 to 1.
- [var beta2: Float](bnnsoptimizeradamwithclippingfields/beta2.md)
  A value that specifies the second moment constant in the range 0 to 1.
- [var time_step: Float](bnnsoptimizeradamwithclippingfields/time_step.md)
  A value that’s at least 1 and represents the optimizer’s current time.
- [var epsilon: Float](bnnsoptimizeradamwithclippingfields/epsilon.md)
  An addition for the division in the parameter update stage.
- [var gradient_scale: Float](bnnsoptimizeradamwithclippingfields/gradient_scale.md)
  A value that specifies the gradient scaling factor.
- [var regularization_scale: Float](bnnsoptimizeradamwithclippingfields/regularization_scale.md)
  A value that specifies the regularization scaling factor.
- [var regularization_func: BNNSOptimizerRegularizationFunction](bnnsoptimizeradamwithclippingfields/regularization_func.md)
  The variable that specifies the regularization function.
- [struct BNNSOptimizerClippingFunction](bnnsoptimizerclippingfunction.md)
  Constants that describe clipping functions.
- [var clip_gradients_min: Float](bnnsoptimizeradamwithclippingfields/clip_gradients_min.md)
  The minimum clipping value for clipping by value.
- [var clip_gradients_max: Float](bnnsoptimizeradamwithclippingfields/clip_gradients_max.md)
  The maximum clipping value for clipping by value.
- [var clip_gradients_max_norm: Float](bnnsoptimizeradamwithclippingfields/clip_gradients_max_norm.md)
  The maximum Euclidean norm for clipping by norm and clipping by global norm.
- [var clip_gradients_use_norm: Float](bnnsoptimizeradamwithclippingfields/clip_gradients_use_norm.md)
  An optional value for a known Euclidean norm for clipping by global norm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsoptimizeradamwithclippingfields/clipping_func)*