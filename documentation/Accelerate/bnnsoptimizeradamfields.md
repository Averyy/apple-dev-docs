# BNNSOptimizerAdamFields

**Framework**: Accelerate  
**Kind**: struct

A structure that contains the fields of an Adam optimizer.

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
struct BNNSOptimizerAdamFields
```

## Topics

### Initializers
- [init(learning_rate: Float, beta1: Float, beta2: Float, time_step: Float, epsilon: Float, gradient_scale: Float, regularization_scale: Float, clip_gradients: Bool, clip_gradients_min: Float, clip_gradients_max: Float, regularization_func: BNNSOptimizerRegularizationFunction)](bnnsoptimizeradamfields/init(learning_rate:beta1:beta2:time_step:epsilon:gradient_scale:regularization_scale:clip_gradients:clip_gradients_min:clip_gradients_max:regularization_func:).md)
  Returns a new Adam optimizer fields structure from the specified parameters.
- [init()](bnnsoptimizeradamfields/init.md)
  Returns a new Adam optimizer fields structure.
### Instance Properties
- [var learning_rate: Float](bnnsoptimizeradamfields/learning_rate.md)
  A value that specifies the learning rate.
- [var beta1: Float](bnnsoptimizeradamfields/beta1.md)
  A value that specifies the first moment constant in the range 0 to 1.
- [var beta2: Float](bnnsoptimizeradamfields/beta2.md)
  A value that specifies the second moment constant in the range 0 to 1.
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

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct AdamOptimizer](bnns/adamoptimizer.md)
  An optimizer that uses the Adam optimization algorithm.
- [struct AdamWOptimizer](bnns/adamwoptimizer.md)
  An optimizer that uses the AdamW optimization algorithm.
- [struct RMSPropOptimizer](bnns/rmspropoptimizer.md)
  An optimizer that uses the root mean square propagation (RMSProp) optimization method.
- [struct SGDMomentumOptimizer](bnns/sgdmomentumoptimizer.md)
  An optimizer that uses the stochastic gradient descent (SGD) with the momentum optimization method.
- [protocol BNNSOptimizer](bnnsoptimizer.md)
- [struct BNNSOptimizerRegularizationFunction](bnnsoptimizerregularizationfunction.md)
  A structure that contains optimizer regularization functions.
- [struct BNNSOptimizerAdamWithClippingFields](bnnsoptimizeradamwithclippingfields.md)
  A structure that contains the fields of an Adam or AdamW optimizer that optionally clips the gradient by value or by norm.
- [struct BNNSOptimizerRMSPropFields](bnnsoptimizerrmspropfields.md)
  A structure that contains the fields of a root mean square propagation (RMSProp) optimizer.
- [struct BNNSOptimizerRMSPropWithClippingFields](bnnsoptimizerrmspropwithclippingfields.md)
  A structure that contains the fields of a root mean square propagation (RMSProp) optimizer that optionally clips the gradient by value or by norm.
- [struct BNNSOptimizerSGDMomentumFields](bnnsoptimizersgdmomentumfields.md)
  A structure that contains the fields of a stochastic gradient descent (SGD) with momentum optimizer.
- [struct BNNSOptimizerSGDMomentumWithClippingFields](bnnsoptimizersgdmomentumwithclippingfields.md)
  A structure that contains the fields of a stochastic gradient descent (SGD) with momentum optimizer that optionally clips the gradient by value or by norm.
- [struct BNNSOptimizerSGDMomentumVariant](bnnsoptimizersgdmomentumvariant.md)
  Constants that define SGD momentum variants.
- [func BNNSOptimizerStep(BNNSOptimizerFunction, UnsafeRawPointer, Int, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>>, UnsafeMutablePointer<UnsafePointer<BNNSNDArrayDescriptor>>, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>?>?, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsoptimizerstep(_:_:_:_:_:_:_:).md)
  Applies a single optimization step to one or more parameters.
- [struct BNNSOptimizerFunction](bnnsoptimizerfunction.md)
  A structure that contains optimizer functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsoptimizeradamfields)*