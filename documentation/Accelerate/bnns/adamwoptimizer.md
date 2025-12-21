# BNNS.AdamWOptimizer

**Framework**: Accelerate  
**Kind**: struct

An optimizer that uses the AdamW optimization algorithm.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
struct AdamWOptimizer
```

## Topics

### Creating an AdamW Optimizer
- [init(learningRate: Float, beta1: Float, beta2: Float, timeStep: Float, epsilon: Float, gradientScale: Float, weightDecay: Float, gradientClipping: BNNS.GradientClipping, usesAMSGrad: Bool)](bnns/adamwoptimizer/init(learningrate:beta1:beta2:timestep:epsilon:gradientscale:weightdecay:gradientclipping:usesamsgrad:).md)
  Returns a new AdamW optimizer object with gradient clipped by value or clipped by norm.
### Inspecting the Properties of an AdamW Optimizer
- [var learningRate: Float](bnns/adamwoptimizer/learningrate.md)
  A value that specifies the learning rate.
- [var beta1: Float](bnns/adamwoptimizer/beta1.md)
  A value that specifies the first-moment constant, in the range `0` to `1`.
- [var beta2: Float](bnns/adamwoptimizer/beta2.md)
  A value that specifies the second-moment constant, in the range `0` to `1`.
- [var timeStep: Float](bnns/adamwoptimizer/timestep.md)
  A value that’s at least `1` and represents the optimizer’s current time.
- [var epsilon: Float](bnns/adamwoptimizer/epsilon.md)
  The epsilon value you use to improve numerical stability.
- [var gradientScale: Float](bnns/adamwoptimizer/gradientscale.md)
  A value that specifies the gradient scaling factor.
- [var weightDecay: Float](bnns/adamwoptimizer/weightdecay.md)
  The weight decay coefficient.
- [var gradientClipping: BNNS.GradientClipping](bnns/adamwoptimizer/gradientclipping.md)
  The gradient clipping function and bounds.
- [BNNS.GradientClipping](bnns/gradientclipping.md)
  Constants that describe clipping functions.
- [var accumulatorCountMultiplier: Int](bnns/adamwoptimizer/accumulatorcountmultiplier.md)
  The number of accumulators required for each parameter.

## Relationships

### Conforms To
- [BNNSOptimizer](bnnsoptimizer.md)

## See Also

- [struct AdamOptimizer](bnns/adamoptimizer.md)
  An optimizer that uses the Adam optimization algorithm.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/adamwoptimizer)*