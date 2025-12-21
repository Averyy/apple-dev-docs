# BNNS.SGDMomentumOptimizer

**Framework**: Accelerate  
**Kind**: struct

An optimizer that uses the stochastic gradient descent (SGD) with the momentum optimization method.

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
struct SGDMomentumOptimizer
```

## Topics

### Creating an SGD with Momentum Optimizer
- [init(learningRate: Float, momentum: Float, gradientScale: Float, regularizationScale: Float, clipsGradientsTo: ClosedRange<Float>?, usesNestrovMomentum: Bool, regularizationFunction: BNNSOptimizerRegularizationFunction, sgdMomentumVariant: BNNSOptimizerSGDMomentumVariant)](bnns/sgdmomentumoptimizer/init(learningrate:momentum:gradientscale:regularizationscale:clipsgradientsto:usesnestrovmomentum:regularizationfunction:sgdmomentumvariant:).md)
  Returns a new stochastic gradient descent (SGD) with momentum optimizer object.
### Inspecting the Properties of an SGD with Momentum Optimizer
- [var learningRate: Float](bnns/sgdmomentumoptimizer/learningrate.md)
  A value that specifies the learning rate.
- [var momentum: Float](bnns/sgdmomentumoptimizer/momentum.md)
  The rate of momentum decay.
- [var gradientScale: Float](bnns/sgdmomentumoptimizer/gradientscale.md)
  A value that specifies the gradient scaling factor.
- [var regularizationScale: Float](bnns/sgdmomentumoptimizer/regularizationscale.md)
  A value that specifies the regularization scaling factor.
- [var gradientBounds: ClosedRange<Float>?](bnns/sgdmomentumoptimizer/gradientbounds.md)
  The values for the minimum and maximum gradients.
- [var gradientClipping: BNNS.GradientClipping](bnns/sgdmomentumoptimizer/gradientclipping.md)
  The gradient clipping.
- [BNNS.GradientClipping](bnns/gradientclipping.md)
  Constants that describe clipping functions.
- [var usesNestrovMomentum: Bool](bnns/sgdmomentumoptimizer/usesnestrovmomentum.md)
  A Boolean value that specifies whether to use Nesterov momentum update.
- [var regularizationFunction: BNNSOptimizerRegularizationFunction](bnns/sgdmomentumoptimizer/regularizationfunction.md)
  The variable that specifies the regularization function.
- [var sgdMomentumVariant: BNNSOptimizerSGDMomentumVariant](bnns/sgdmomentumoptimizer/sgdmomentumvariant.md)
  The variable that specifies the momentum variant.
- [var accumulatorCountMultiplier: Int](bnns/sgdmomentumoptimizer/accumulatorcountmultiplier.md)
  The number of accumulators required for each parameter.
### Initializers
- [init(learningRate: Float, momentum: Float, gradientScale: Float, regularizationScale: Float, clipsGradientsTo: ClosedRange<Float>?, usesNesterovMomentum: Bool, regularizationFunction: BNNSOptimizerRegularizationFunction, sgdMomentumVariant: BNNSOptimizerSGDMomentumVariant)](bnns/sgdmomentumoptimizer/init(learningrate:momentum:gradientscale:regularizationscale:clipsgradientsto:usesnesterovmomentum:regularizationfunction:sgdmomentumvariant:).md)
- [init(learningRate: Float, momentum: Float, gradientScale: Float, regularizationScale: Float, gradientClipping: BNNS.GradientClipping, usesNesterovMomentum: Bool, regularizationFunction: BNNSOptimizerRegularizationFunction, sgdMomentumVariant: BNNSOptimizerSGDMomentumVariant)](bnns/sgdmomentumoptimizer/init(learningrate:momentum:gradientscale:regularizationscale:gradientclipping:usesnesterovmomentum:regularizationfunction:sgdmomentumvariant:).md)
### Instance Properties
- [var usesNesterovMomentum: Bool](bnns/sgdmomentumoptimizer/usesnesterovmomentum.md)

## Relationships

### Conforms To
- [BNNSOptimizer](bnnsoptimizer.md)

## See Also

- [struct AdamOptimizer](bnns/adamoptimizer.md)
  An optimizer that uses the Adam optimization algorithm.
- [struct AdamWOptimizer](bnns/adamwoptimizer.md)
  An optimizer that uses the AdamW optimization algorithm.
- [struct RMSPropOptimizer](bnns/rmspropoptimizer.md)
  An optimizer that uses the root mean square propagation (RMSProp) optimization method.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/sgdmomentumoptimizer)*