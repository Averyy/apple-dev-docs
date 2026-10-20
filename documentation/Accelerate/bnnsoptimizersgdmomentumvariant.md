# BNNSOptimizerSGDMomentumVariant

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

Constants that define SGD momentum variants.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct BNNSOptimizerSGDMomentumVariant
```

```c
typedef enum { ... } BNNSOptimizerSGDMomentumVariant;
```

## Topics

### Momentum Variants
- [init(UInt32)](./bnnsoptimizersgdmomentumvariant/init%28_%29.md)
- [init(rawValue: UInt32)](./bnnsoptimizersgdmomentumvariant/init%28rawvalue%29.md)
- [var rawValue: UInt32](./bnnsoptimizersgdmomentumvariant/rawvalue.md)
- [var BNNSSGDMomentumVariant0: BNNSOptimizerSGDMomentumVariant](./bnnssgdmomentumvariant0.md)
  A constant that indicates SGD momentum variant 0.
- [var BNNSSGDMomentumVariant1: BNNSOptimizerSGDMomentumVariant](./bnnssgdmomentumvariant1.md)
  A constant that indicates SGD momentum variant 1.
- [var BNNSSGDMomentumVariant2: BNNSOptimizerSGDMomentumVariant](./bnnssgdmomentumvariant2.md)
  A constant that indicates SGD momentum variant 2.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
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
- [struct BNNSOptimizerAdamWithClippingFields](./bnnsoptimizeradamwithclippingfields.md)
  A structure that contains the fields of an Adam or AdamW optimizer that optionally clips the gradient by value or by norm.
- [struct BNNSOptimizerRMSPropFields](./bnnsoptimizerrmspropfields.md)
  A structure that contains the fields of a root mean square propagation (RMSProp) optimizer.
- [struct BNNSOptimizerRMSPropWithClippingFields](./bnnsoptimizerrmspropwithclippingfields.md)
  A structure that contains the fields of a root mean square propagation (RMSProp) optimizer that optionally clips the gradient by value or by norm.
- [struct BNNSOptimizerSGDMomentumFields](./bnnsoptimizersgdmomentumfields.md)
  A structure that contains the fields of a stochastic gradient descent (SGD) with momentum optimizer.
- [struct BNNSOptimizerSGDMomentumWithClippingFields](./bnnsoptimizersgdmomentumwithclippingfields.md)
  A structure that contains the fields of a stochastic gradient descent (SGD) with momentum optimizer that optionally clips the gradient by value or by norm.
- [func BNNSOptimizerStep(BNNSOptimizerFunction, UnsafeRawPointer, Int, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>>, UnsafeMutablePointer<UnsafePointer<BNNSNDArrayDescriptor>>, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>?>?, UnsafePointer<BNNSFilterParameters>?) -> Int32](./bnnsoptimizerstep%28_,_,_,_,_,_,_%29.md)
  Applies a single optimization step to one or more parameters.
- [struct BNNSOptimizerFunction](./bnnsoptimizerfunction.md)
  A structure that contains optimizer functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsoptimizersgdmomentumvariant)*