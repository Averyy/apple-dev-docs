# BNNSOptimizerRMSPropFields

**Framework**: Accelerate  
**Kind**: struct

A structure that contains the fields of a root mean square propagation (RMSProp) optimizer.

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
struct BNNSOptimizerRMSPropFields
```

## Topics

### Initializers
- [init(learning_rate: Float, alpha: Float, epsilon: Float, centered: Bool, momentum: Float, gradient_scale: Float, regularization_scale: Float, clip_gradients: Bool, clip_gradients_min: Float, clip_gradients_max: Float, regularization_func: BNNSOptimizerRegularizationFunction)](bnnsoptimizerrmspropfields/init(learning_rate:alpha:epsilon:centered:momentum:gradient_scale:regularization_scale:clip_gradients:clip_gradients_min:clip_gradients_max:regularization_func:).md)
  Returns a new RMSProp optimizer fields structure from the specified parameters.
- [init()](bnnsoptimizerrmspropfields/init.md)
  Returns a new RMSProp optimizer fields structure.
### Instance Properties
- [var learning_rate: Float](bnnsoptimizerrmspropfields/learning_rate.md)
  A value that specifies the learning rate.
- [var alpha: Float](bnnsoptimizerrmspropfields/alpha.md)
  A constant that specifies smoothing.
- [var epsilon: Float](bnnsoptimizerrmspropfields/epsilon.md)
  A term that the optimizer adds to the denominator.
- [var centered: Bool](bnnsoptimizerrmspropfields/centered.md)
  A Boolean value that specifies whether to use the centered variant.
- [var momentum: Float](bnnsoptimizerrmspropfields/momentum.md)
  The rate of momentum decay.
- [var gradient_scale: Float](bnnsoptimizerrmspropfields/gradient_scale.md)
  A value that specifies the gradient scaling factor.
- [var regularization_scale: Float](bnnsoptimizerrmspropfields/regularization_scale.md)
  A value that specifies the regularization scaling factor.
- [var clip_gradients: Bool](bnnsoptimizerrmspropfields/clip_gradients.md)
  A Boolean value that specifies whether to clip the gradient between minimum and maximum values.
- [var clip_gradients_min: Float](bnnsoptimizerrmspropfields/clip_gradients_min.md)
  The values for the minimum gradient.
- [var clip_gradients_max: Float](bnnsoptimizerrmspropfields/clip_gradients_max.md)
  The values for the maximum gradient.
- [var regularization_func: BNNSOptimizerRegularizationFunction](bnnsoptimizerrmspropfields/regularization_func.md)
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
- [struct BNNSOptimizerAdamFields](bnnsoptimizeradamfields.md)
  A structure that contains the fields of an Adam optimizer.
- [struct BNNSOptimizerAdamWithClippingFields](bnnsoptimizeradamwithclippingfields.md)
  A structure that contains the fields of an Adam or AdamW optimizer that optionally clips the gradient by value or by norm.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsoptimizerrmspropfields)*