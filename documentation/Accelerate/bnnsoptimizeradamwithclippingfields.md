# BNNSOptimizerAdamWithClippingFields

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A structure that contains the fields of an Adam or AdamW optimizer that optionally clips the gradient by value or by norm.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 14.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use BNNSGraph* APIs

## Declaration

```swift
struct BNNSOptimizerAdamWithClippingFields
```

```c
typedef struct { ... } BNNSOptimizerAdamWithClippingFields;
```

## Topics

### Initializers
- [init(learning_rate: Float, beta1: Float, beta2: Float, time_step: Float, epsilon: Float, gradient_scale: Float, regularization_scale: Float, regularization_func: BNNSOptimizerRegularizationFunction, clipping_func: BNNSOptimizerClippingFunction, clip_gradients_min: Float, clip_gradients_max: Float, clip_gradients_max_norm: Float, clip_gradients_use_norm: Float)](./bnnsoptimizeradamwithclippingfields/init%28learning_rate,beta1,beta2,time_step,epsilon,gradient_scale,regularization_scale,regularization_func,clipping_func,clip_gradients_min,clip_gradients_max,clip_gradients_max_norm,clip_gradients_use_norm%29.md)
  Returns a new Adam or AdamW optimizer fields structure from the specified parameters.
- [init()](./bnnsoptimizeradamwithclippingfields/init%28%29.md)
  Returns a new Adam or AdamW optimizer fields structure.
### Instance Properties
- [var learning_rate: Float](./bnnsoptimizeradamwithclippingfields/learning_rate.md)
  A value that specifies the learning rate.
- [var beta1: Float](./bnnsoptimizeradamwithclippingfields/beta1.md)
  A value that specifies the first moment constant in the range 0 to 1.
- [var beta2: Float](./bnnsoptimizeradamwithclippingfields/beta2.md)
  A value that specifies the second moment constant in the range 0 to 1.
- [var time_step: Float](./bnnsoptimizeradamwithclippingfields/time_step.md)
  A value that’s at least 1 and represents the optimizer’s current time.
- [var epsilon: Float](./bnnsoptimizeradamwithclippingfields/epsilon.md)
  An addition for the division in the parameter update stage.
- [var gradient_scale: Float](./bnnsoptimizeradamwithclippingfields/gradient_scale.md)
  A value that specifies the gradient scaling factor.
- [var regularization_scale: Float](./bnnsoptimizeradamwithclippingfields/regularization_scale.md)
  A value that specifies the regularization scaling factor.
- [var regularization_func: BNNSOptimizerRegularizationFunction](./bnnsoptimizeradamwithclippingfields/regularization_func.md)
  The variable that specifies the regularization function.
- [var clipping_func: BNNSOptimizerClippingFunction](./bnnsoptimizeradamwithclippingfields/clipping_func.md)
  The clipping function.
- [struct BNNSOptimizerClippingFunction](./bnnsoptimizerclippingfunction.md)
  Constants that describe clipping functions.
- [var clip_gradients_min: Float](./bnnsoptimizeradamwithclippingfields/clip_gradients_min.md)
  The minimum clipping value for clipping by value.
- [var clip_gradients_max: Float](./bnnsoptimizeradamwithclippingfields/clip_gradients_max.md)
  The maximum clipping value for clipping by value.
- [var clip_gradients_max_norm: Float](./bnnsoptimizeradamwithclippingfields/clip_gradients_max_norm.md)
  The maximum Euclidean norm for clipping by norm and clipping by global norm.
- [var clip_gradients_use_norm: Float](./bnnsoptimizeradamwithclippingfields/clip_gradients_use_norm.md)
  An optional value for a known Euclidean norm for clipping by global norm.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Optimizers
- [struct AdamOptimizer](./bnns/adamoptimizer.md)
  An optimizer that uses the Adam optimization algorithm.
- [struct AdamWOptimizer](./bnns/adamwoptimizer.md)
  An optimizer that uses the AdamW optimization algorithm.
- [struct RMSPropOptimizer](./bnns/rmspropoptimizer.md)
  An optimizer that uses the root mean square propagation (RMSProp) optimization method.
- [struct SGDMomentumOptimizer](./bnns/sgdmomentumoptimizer.md)
  An optimizer that uses the stochastic gradient descent (SGD) with the momentum optimization method.
- [protocol BNNSOptimizer](./bnnsoptimizer.md)
- [struct BNNSOptimizerRegularizationFunction](./bnnsoptimizerregularizationfunction.md)
  A structure that contains optimizer regularization functions.
- [struct BNNSOptimizerAdamFields](./bnnsoptimizeradamfields.md)
  A structure that contains the fields of an Adam optimizer.
- [struct BNNSOptimizerRMSPropFields](./bnnsoptimizerrmspropfields.md)
  A structure that contains the fields of a root mean square propagation (RMSProp) optimizer.
- [struct BNNSOptimizerRMSPropWithClippingFields](./bnnsoptimizerrmspropwithclippingfields.md)
  A structure that contains the fields of a root mean square propagation (RMSProp) optimizer that optionally clips the gradient by value or by norm.
- [struct BNNSOptimizerSGDMomentumFields](./bnnsoptimizersgdmomentumfields.md)
  A structure that contains the fields of a stochastic gradient descent (SGD) with momentum optimizer.
- [struct BNNSOptimizerSGDMomentumWithClippingFields](./bnnsoptimizersgdmomentumwithclippingfields.md)
  A structure that contains the fields of a stochastic gradient descent (SGD) with momentum optimizer that optionally clips the gradient by value or by norm.
- [struct BNNSOptimizerSGDMomentumVariant](./bnnsoptimizersgdmomentumvariant.md)
  Constants that define SGD momentum variants.
- [func BNNSOptimizerStep(BNNSOptimizerFunction, UnsafeRawPointer, Int, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>>, UnsafeMutablePointer<UnsafePointer<BNNSNDArrayDescriptor>>, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>?>?, UnsafePointer<BNNSFilterParameters>?) -> Int32](./bnnsoptimizerstep%28_,_,_,_,_,_,_%29.md)
  Applies a single optimization step to one or more parameters.
- [struct BNNSOptimizerFunction](./bnnsoptimizerfunction.md)
  A structure that contains optimizer functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsoptimizeradamwithclippingfields)*