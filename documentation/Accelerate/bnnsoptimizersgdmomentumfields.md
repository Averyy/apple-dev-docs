# BNNSOptimizerSGDMomentumFields

**Framework**: Accelerate  
**Kind**: struct

A structure that contains the fields of a stochastic gradient descent (SGD) with momentum optimizer.

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
struct BNNSOptimizerSGDMomentumFields
```

## Topics

### Initializers
- [init(learning_rate: Float, momentum: Float, gradient_scale: Float, regularization_scale: Float, clip_gradients: Bool, clip_gradients_min: Float, clip_gradients_max: Float, nesterov: Bool, regularization_func: BNNSOptimizerRegularizationFunction, sgd_momentum_variant: BNNSOptimizerSGDMomentumVariant)](bnnsoptimizersgdmomentumfields/init(learning_rate:momentum:gradient_scale:regularization_scale:clip_gradients:clip_gradients_min:clip_gradients_max:nesterov:regularization_func:sgd_momentum_variant:).md)
  Returns a new SGD with momentum optimizer fields structure from the specified parameters.
- [init()](bnnsoptimizersgdmomentumfields/init.md)
  Returns a new SGD with momentum optimizer fields structure.
### Instance Properties
- [var learning_rate: Float](bnnsoptimizersgdmomentumfields/learning_rate.md)
  A value that specifies the learning rate.
- [var momentum: Float](bnnsoptimizersgdmomentumfields/momentum.md)
  The rate of momentum decay.
- [var gradient_scale: Float](bnnsoptimizersgdmomentumfields/gradient_scale.md)
  A value that specifies the gradient scaling factor.
- [var regularization_scale: Float](bnnsoptimizersgdmomentumfields/regularization_scale.md)
  A value that specifies the regularization scaling factor.
- [var clip_gradients: Bool](bnnsoptimizersgdmomentumfields/clip_gradients.md)
  A Boolean value that specifies whether to clip the gradient between minimum and maximum values.
- [var clip_gradients_min: Float](bnnsoptimizersgdmomentumfields/clip_gradients_min.md)
  The values for the minimum gradient.
- [var clip_gradients_max: Float](bnnsoptimizersgdmomentumfields/clip_gradients_max.md)
  The values for the maximum gradient.
- [var nesterov: Bool](bnnsoptimizersgdmomentumfields/nesterov.md)
  A Boolean value that specifies whether to use Nesterov momentum update.
- [var regularization_func: BNNSOptimizerRegularizationFunction](bnnsoptimizersgdmomentumfields/regularization_func.md)
  The variable that specifies the regularization function.
- [var sgd_momentum_variant: BNNSOptimizerSGDMomentumVariant](bnnsoptimizersgdmomentumfields/sgd_momentum_variant.md)
  The variable that specifies the momentum variant.

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
- [struct BNNSOptimizerAdamFields](bnnsoptimizeradamfields.md)
  A structure that contains the fields of an Adam optimizer.
- [struct BNNSOptimizerAdamWithClippingFields](bnnsoptimizeradamwithclippingfields.md)
  A structure that contains the fields of an Adam or AdamW optimizer that optionally clips the gradient by value or by norm.
- [struct BNNSOptimizerRMSPropFields](bnnsoptimizerrmspropfields.md)
  A structure that contains the fields of a root mean square propagation (RMSProp) optimizer.
- [struct BNNSOptimizerRMSPropWithClippingFields](bnnsoptimizerrmspropwithclippingfields.md)
  A structure that contains the fields of a root mean square propagation (RMSProp) optimizer that optionally clips the gradient by value or by norm.
- [struct BNNSOptimizerSGDMomentumWithClippingFields](bnnsoptimizersgdmomentumwithclippingfields.md)
  A structure that contains the fields of a stochastic gradient descent (SGD) with momentum optimizer that optionally clips the gradient by value or by norm.
- [struct BNNSOptimizerSGDMomentumVariant](bnnsoptimizersgdmomentumvariant.md)
  Constants that define SGD momentum variants.
- [func BNNSOptimizerStep(BNNSOptimizerFunction, UnsafeRawPointer, Int, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>>, UnsafeMutablePointer<UnsafePointer<BNNSNDArrayDescriptor>>, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>?>?, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsoptimizerstep(_:_:_:_:_:_:_:).md)
  Applies a single optimization step to one or more parameters.
- [struct BNNSOptimizerFunction](bnnsoptimizerfunction.md)
  A structure that contains optimizer functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsoptimizersgdmomentumfields)*