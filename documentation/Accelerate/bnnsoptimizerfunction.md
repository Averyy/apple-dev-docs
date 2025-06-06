# BNNSOptimizerFunction

**Framework**: Accelerate  
**Kind**: struct

A structure that contains optimizer functions.

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
struct BNNSOptimizerFunction
```

## Topics

### Adam Optimizer Functions
- [var BNNSOptimizerFunctionAdam: BNNSOptimizerFunction](bnnsoptimizerfunctionadam.md)
  An optimizer function that updates parameters according to the Adam algorithm.
- [var BNNSOptimizerFunctionAdamWithClipping: BNNSOptimizerFunction](bnnsoptimizerfunctionadamwithclipping.md)
  An optimizer function that updates parameters according to the Adam algorithm and optionally clips the gradient by value or by norm.
- [var BNNSOptimizerFunctionAdamAMSGrad: BNNSOptimizerFunction](bnnsoptimizerfunctionadamamsgrad.md)
  An optimizer function that updates parameters according to the AMSGrad variant of the Adam algorithm.
- [var BNNSOptimizerFunctionAdamAMSGradWithClipping: BNNSOptimizerFunction](bnnsoptimizerfunctionadamamsgradwithclipping.md)
  An optimizer function that updates parameters according to the AMSGrad variant of the Adam algorithm and optionally clips the gradient by value or by norm.
### AdamW Optimizer Functions
- [var BNNSOptimizerFunctionAdamW: BNNSOptimizerFunction](bnnsoptimizerfunctionadamw.md)
  An optimizer function that updates parameters according to the AdamW algorithm.
- [var BNNSOptimizerFunctionAdamWWithClipping: BNNSOptimizerFunction](bnnsoptimizerfunctionadamwwithclipping.md)
  An optimizer function that updates parameters according to the AdamW algorithm and optionally clips the gradient by value or by norm.
- [var BNNSOptimizerFunctionAdamWAMSGrad: BNNSOptimizerFunction](bnnsoptimizerfunctionadamwamsgrad.md)
  An optimizer function that updates parameters according to the AMSGrad variant of the AdamW algorithm.
- [var BNNSOptimizerFunctionAdamWAMSGradWithClipping: BNNSOptimizerFunction](bnnsoptimizerfunctionadamwamsgradwithclipping.md)
  An optimizer function that updates parameters according to the AMSGrad variant of the AdamW algorithm and optionally clips the gradient by value or by norm.
### RMSProp Optimizer Functions
- [var BNNSOptimizerFunctionRMSProp: BNNSOptimizerFunction](bnnsoptimizerfunctionrmsprop.md)
  An optimizer function that updates parameters according to the root mean square propagation (RMSProp) algorithm.
- [var BNNSOptimizerFunctionRMSPropWithClipping: BNNSOptimizerFunction](bnnsoptimizerfunctionrmspropwithclipping.md)
  An optimizer function that updates parameters according to the root mean square propagation (RMSProp) algorithm and optionally clips the gradient by value or by norm.
### SGD  Optimizer Functions
- [var BNNSOptimizerFunctionSGDMomentum: BNNSOptimizerFunction](bnnsoptimizerfunctionsgdmomentum.md)
  An optimizer function that updates parameters according to the stochastic gradient descent (SGD) with momentum algorithm.
- [var BNNSOptimizerFunctionSGDMomentumWithClipping: BNNSOptimizerFunction](bnnsoptimizerfunctionsgdmomentumwithclipping.md)
  An optimizer function that updates parameters according to the stochastic gradient descent (SGD) with momentum algorithm and optionally clips the gradient by value or by norm.
### Raw Values
- [var rawValue: UInt32](bnnsoptimizerfunction/rawvalue.md)
- [init(UInt32)](bnnsoptimizerfunction/init(_:).md)
- [init(rawValue: UInt32)](bnnsoptimizerfunction/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
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
- [struct BNNSOptimizerSGDMomentumFields](bnnsoptimizersgdmomentumfields.md)
  A structure that contains the fields of a stochastic gradient descent (SGD) with momentum optimizer.
- [struct BNNSOptimizerSGDMomentumWithClippingFields](bnnsoptimizersgdmomentumwithclippingfields.md)
  A structure that contains the fields of a stochastic gradient descent (SGD) with momentum optimizer that optionally clips the gradient by value or by norm.
- [struct BNNSOptimizerSGDMomentumVariant](bnnsoptimizersgdmomentumvariant.md)
  Constants that define SGD momentum variants.
- [func BNNSOptimizerStep(BNNSOptimizerFunction, UnsafeRawPointer, Int, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>>, UnsafeMutablePointer<UnsafePointer<BNNSNDArrayDescriptor>>, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>?>?, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsoptimizerstep(_:_:_:_:_:_:_:).md)
  Applies a single optimization step to one or more parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsoptimizerfunction)*