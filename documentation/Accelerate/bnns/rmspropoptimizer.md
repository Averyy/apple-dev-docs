# BNNS.RMSPropOptimizer

**Framework**: Accelerate  
**Kind**: struct

An optimizer that uses the root mean square propagation (RMSProp) optimization method.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
struct RMSPropOptimizer
```

## Topics

### Creating an RMSProp Optimizer
- [init(learningRate: Float, alpha: Float, epsilon: Float, centered: Bool, momentum: Float, gradientScale: Float, regularizationScale: Float, clipsGradientsTo: ClosedRange<Float>?, regularizationFunction: BNNSOptimizerRegularizationFunction)](bnns/rmspropoptimizer/init(learningrate:alpha:epsilon:centered:momentum:gradientscale:regularizationscale:clipsgradientsto:regularizationfunction:).md)
  Returns a new RMSProp optimizer object.
- [init(learningRate: Float, alpha: Float, epsilon: Float, centered: Bool, momentum: Float, gradientScale: Float, regularizationScale: Float, gradientClipping: BNNS.GradientClipping, regularizationFunction: BNNSOptimizerRegularizationFunction)](bnns/rmspropoptimizer/init(learningrate:alpha:epsilon:centered:momentum:gradientscale:regularizationscale:gradientclipping:regularizationfunction:).md)
  Returns a new RMSProp optimizer object with gradient clipped by value or clipped by norm.
### Inspecting the Properties of an RMSProp Optimizer
- [var learningRate: Float](bnns/rmspropoptimizer/learningrate.md)
  A value that specifies the learning rate.
- [var alpha: Float](bnns/rmspropoptimizer/alpha.md)
  A constant that specifies smoothing.
- [var epsilon: Float](bnns/rmspropoptimizer/epsilon.md)
  A term that the optimizer adds to the denominator.
- [var centered: Bool](bnns/rmspropoptimizer/centered.md)
  A Boolean value that specifies whether to use the centered variant.
- [var momentum: Float](bnns/rmspropoptimizer/momentum.md)
  The rate of momentum decay.
- [var gradientScale: Float](bnns/rmspropoptimizer/gradientscale.md)
  A value that specifies the gradient scaling factor.
- [var regularizationScale: Float](bnns/rmspropoptimizer/regularizationscale.md)
  A value that specifies the regularization scaling factor.
- [var gradientBounds: ClosedRange<Float>?](bnns/rmspropoptimizer/gradientbounds.md)
  The values for the minimum and maximum gradients.
- [var gradientClipping: BNNS.GradientClipping](bnns/rmspropoptimizer/gradientclipping.md)
  The gradient clipping.
- [BNNS.GradientClipping](bnns/gradientclipping.md)
  Constants that describe clipping functions.
- [var regularizationFunction: BNNSOptimizerRegularizationFunction](bnns/rmspropoptimizer/regularizationfunction.md)
  The variable that specifies the regularization function.
- [var accumulatorCountMultiplier: Int](bnns/rmspropoptimizer/accumulatorcountmultiplier.md)
  The number of accumulators required for each parameter.

## Relationships

### Conforms To
- [BNNSOptimizer](bnnsoptimizer.md)

## See Also

- [struct AdamOptimizer](bnns/adamoptimizer.md)
  An optimizer that uses the Adam optimization algorithm.
- [struct AdamWOptimizer](bnns/adamwoptimizer.md)
  An optimizer that uses the AdamW optimization algorithm.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/rmspropoptimizer)*