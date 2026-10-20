# BNNSOptimizerStep(_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Applies a single optimization step to one or more parameters.

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
func BNNSOptimizerStep(_ function: BNNSOptimizerFunction, _ OptimizerAlgFields: UnsafeRawPointer, _ number_of_parameters: Int, _ parameters: UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>>, _ gradients: UnsafeMutablePointer<UnsafePointer<BNNSNDArrayDescriptor>>, _ accumulators: UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>?>?, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> Int32
```

```c
int BNNSOptimizerStep(BNNSOptimizerFunction function, const void *OptimizerAlgFields, size_t number_of_parameters, BNNSNDArrayDescriptor **parameters, const BNNSNDArrayDescriptor **gradients, BNNSNDArrayDescriptor **accumulators, const BNNSFilterParameters *filter_params);
```

#### Discussion

Use [`BNNSOptimizerStep(_:_:_:_:_:_:_:)`](./bnnsoptimizerstep%28_,_,_,_,_,_,_%29.md) to update a set of parameters using a supplied optimization algorithm.

> ❗ **Important**:  Parameter, gradient, and accumulator descriptors must have the same sizes and strides and be of type `float`.

For example, the following shows the code required to update the weights data described by `weightsDescriptor` using an Adam optimizer.

```swift
var weightsDescriptor: BNNSNDArrayDescriptor = ...
var deltaDescriptor: BNNSNDArrayDescriptor = ...
var accumulatorOneDescriptor: BNNSNDArrayDescriptor = ...
var accumulatorTwoDescriptor: BNNSNDArrayDescriptor = ...
var adamFields: BNNSOptimizerAdamFields = ...

withUnsafeMutablePointer(to: &weightsDescriptor) { weightsDescriptorPtr in
    withUnsafePointer(to: &deltaDescriptor) { deltaDescriptorPtr in
        withUnsafeMutablePointer(to: &accumulatorOneDescriptor) { accumulatorOneDescriptorPtr in
            withUnsafeMutablePointer(to: &accumulatorTwoDescriptor) { accumulatorTwoDescriptorPtr in
                
                var paramaters = [ weightsDescriptorPtr ]
                var gradients = [ deltaDescriptorPtr ]
                var accumulators = [ Optional(accumulatorOneDescriptorPtr),
                                     Optional(accumulatorTwoDescriptorPtr) ]
                
                let error = withUnsafePointer(to: &adamFields) { adamFieldsPointer in
                    BNNSOptimizerStep(BNNSOptimizerFunctionAdam,
                                      adamFieldsPointer, 1,
                                      &paramaters,
                                      &gradients,
                                      &accumulators,
                                      nil)
                }
                
                if error != 0 {
                    fatalError("BNNSOptimizerStep failed.")
                }
            }
        }
    }
}

```

## Parameters

- `function`: The optimization algorithm.
- `OptimizerAlgFields`: A pointer to parameters for optimization function.
- `number_of_parameters`: The number of parameters the step updates.
- `parameters`: An array of pointers to parameter descriptors.
- `gradients`: An array of pointers to gradient descriptors.
- `accumulators`: An array of pointers to accumulator descriptors.
- `filter_params`: The filter runtime parameters.

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
- [struct BNNSOptimizerSGDMomentumVariant](./bnnsoptimizersgdmomentumvariant.md)
  Constants that define SGD momentum variants.
- [struct BNNSOptimizerFunction](./bnnsoptimizerfunction.md)
  A structure that contains optimizer functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsoptimizerstep(_:_:_:_:_:_:_:))*