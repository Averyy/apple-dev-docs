# BNNSOptimizerClippingFunction

**Framework**: Accelerate  
**Kind**: struct

Constants that describe clipping functions.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct BNNSOptimizerClippingFunction
```

## Topics

### Clipping Functions
- [init(UInt32)](bnnsoptimizerclippingfunction/init(_:).md)
  Creates a new instance with the specified raw value.
- [init(rawValue: UInt32)](bnnsoptimizerclippingfunction/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
- [var rawValue: UInt32](bnnsoptimizerclippingfunction/rawvalue.md)
  The corresponding value of the raw type.
- [var BNNSOptimizerClippingNone: BNNSOptimizerClippingFunction](bnnsoptimizerclippingnone.md)
  A constant that specifes no clipping.
- [var BNNSOptimizerClippingByValue: BNNSOptimizerClippingFunction](bnnsoptimizerclippingbyvalue.md)
  A constant that specifes clipping to minimum and maximum values.
- [var BNNSOptimizerClippingByNorm: BNNSOptimizerClippingFunction](bnnsoptimizerclippingbynorm.md)
  A constant that specifes clipping to a maximum Euclidean norm.
- [var BNNSOptimizerClippingByGlobalNorm: BNNSOptimizerClippingFunction](bnnsoptimizerclippingbyglobalnorm.md)
  A constant that specifes clipping to a maximum global Euclidean norm.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

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
- [var clipping_func: BNNSOptimizerClippingFunction](bnnsoptimizeradamwithclippingfields/clipping_func.md)
  The clipping function.
- [var clip_gradients_min: Float](bnnsoptimizeradamwithclippingfields/clip_gradients_min.md)
  The minimum clipping value for clipping by value.
- [var clip_gradients_max: Float](bnnsoptimizeradamwithclippingfields/clip_gradients_max.md)
  The maximum clipping value for clipping by value.
- [var clip_gradients_max_norm: Float](bnnsoptimizeradamwithclippingfields/clip_gradients_max_norm.md)
  The maximum Euclidean norm for clipping by norm and clipping by global norm.
- [var clip_gradients_use_norm: Float](bnnsoptimizeradamwithclippingfields/clip_gradients_use_norm.md)
  An optional value for a known Euclidean norm for clipping by global norm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsoptimizerclippingfunction)*