# BNNS.AdamOptimizer

**Framework**: Accelerate  
**Kind**: struct

An optimizer that uses the Adam optimization algorithm.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- visionOS ?+
- watchOS 7.0+
- Unknown ?+ - Deprecated
- tvOS 14.0+

## Declaration

```swift
struct AdamOptimizer
```

## Topics

### Creating an Adam Optimizer
- [init(learningRate: Float, beta1: Float, beta2: Float, timeStep: Float, epsilon: Float, gradientScale: Float, regularizationScale: Float, clipsGradientsTo: ClosedRange<Float>?, regularizationFunction: BNNSOptimizerRegularizationFunction)](bnns/adamoptimizer/init(learningrate:beta1:beta2:timestep:epsilon:gradientscale:regularizationscale:clipsgradientsto:regularizationfunction:).md)
  Returns a new Adam optimizer object.
- [init(learningRate: Float, beta1: Float, beta2: Float, timeStep: Float, epsilon: Float, gradientScale: Float, regularizationScale: Float, gradientClipping: BNNS.GradientClipping, regularizationFunction: BNNSOptimizerRegularizationFunction, usesAMSGrad: Bool)](bnns/adamoptimizer/init(learningrate:beta1:beta2:timestep:epsilon:gradientscale:regularizationscale:gradientclipping:regularizationfunction:usesamsgrad:).md)
  Returns a new Adam optimizer object with gradient clipped by value or clipped by norm.
### Inspecting the Properties of an Adam Optimizer
- [var learningRate: Float](bnns/adamoptimizer/learningrate.md)
  A value that specifies the learning rate.
- [var beta1: Float](bnns/adamoptimizer/beta1.md)
  A value that specifies the first-moment constant, in the range `0` to `1`.
- [var beta2: Float](bnns/adamoptimizer/beta2.md)
  A value that specifies the second-moment constant, in the range `0` to `1`.
- [var timeStep: Float](bnns/adamoptimizer/timestep.md)
  A value that’s at least `1` and represents the optimizer’s current time.
- [var epsilon: Float](bnns/adamoptimizer/epsilon.md)
  The epsilon value you use to improve numerical stability.
- [var gradientScale: Float](bnns/adamoptimizer/gradientscale.md)
  A value that specifies the gradient scaling factor.
- [var regularizationScale: Float](bnns/adamoptimizer/regularizationscale.md)
  A value that specifies the regularization scaling factor.
- [var gradientBounds: ClosedRange<Float>?](bnns/adamoptimizer/gradientbounds.md)
  The values for the minimum and maximum gradients.
- [var gradientClipping: BNNS.GradientClipping](bnns/adamoptimizer/gradientclipping.md)
  The gradient clipping.
- [var regularizationFunction: BNNSOptimizerRegularizationFunction](bnns/adamoptimizer/regularizationfunction.md)
  The variable that specifies the regularization function.
- [var usesAMSGrad: Bool](bnns/adamoptimizer/usesamsgrad.md)
  A Boolean value that specifies whether to use the AMSGrad variant.
- [var accumulatorCountMultiplier: Int](bnns/adamoptimizer/accumulatorcountmultiplier.md)
  The number of accumulators required for each parameter.
- [BNNS.GradientClipping](bnns/gradientclipping.md)
  Constants that describe clipping functions.

## Relationships

### Conforms To
- [BNNSOptimizer](bnnsoptimizer.md)

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/adamoptimizer)*