# BNNSReduceFunction

**Framework**: Accelerate  
**Kind**: struct

Constants that describe reduction functions.

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
struct BNNSReduceFunction
```

## Topics

### Reduction Functions
- [init(UInt32)](bnnsreducefunction/init(_:).md)
- [init(rawValue: UInt32)](bnnsreducefunction/init(rawvalue:).md)
- [var rawValue: UInt32](bnnsreducefunction/rawvalue.md)
- [var BNNSReduceFunctionArgMax: BNNSReduceFunction](bnnsreducefunctionargmax.md)
  A reduction function that computes the index of the maximum value.
- [var BNNSReduceFunctionArgMin: BNNSReduceFunction](bnnsreducefunctionargmin.md)
  A reduction function that computes the index of the minimum value.
- [var BNNSReduceFunctionL1Norm: BNNSReduceFunction](bnnsreducefunctionl1norm.md)
  A reduction function that computes the sum of the absolute value of each element.
- [var BNNSReduceFunctionLogicalAnd: BNNSReduceFunction](bnnsreducefunctionlogicaland.md)
  A reduction function that reduces a tensor to true if all elements are true.
- [var BNNSReduceFunctionAll: BNNSReduceFunction](bnnsreducefunctionall.md)
  An alias of the logical AND reduction function.
- [var BNNSReduceFunctionLogicalOr: BNNSReduceFunction](bnnsreducefunctionlogicalor.md)
  A reduction function that reduces a tensor to true if any element is true.
- [var BNNSReduceFunctionLogSum: BNNSReduceFunction](bnnsreducefunctionlogsum.md)
- [var BNNSReduceFunctionAny: BNNSReduceFunction](bnnsreducefunctionany.md)
  An alias of the logical OR reduction function.
- [var BNNSReduceFunctionMax: BNNSReduceFunction](bnnsreducefunctionmax.md)
  A reduction function that computes the maximum value.
- [var BNNSReduceFunctionMean: BNNSReduceFunction](bnnsreducefunctionmean.md)
  A reduction function that computes the mean value.
- [var BNNSReduceFunctionMeanNonZero: BNNSReduceFunction](bnnsreducefunctionmeannonzero.md)
  A reduction function that computes the mean value of nonzero elements.
- [var BNNSReduceFunctionMin: BNNSReduceFunction](bnnsreducefunctionmin.md)
  A reduction function that computes the minimum value.
- [var BNNSReduceFunctionSum: BNNSReduceFunction](bnnsreducefunctionsum.md)
  A reduction function that computes the sum of all values.
- [var BNNSReduceFunctionSumLog: BNNSReduceFunction](bnnsreducefunctionsumlog.md)
  A reduction function that computes the sum of the natural logarithm of all values.
- [var BNNSReduceFunctionSumSquare: BNNSReduceFunction](bnnsreducefunctionsumsquare.md)
  A reduction function that computes the sum of the square of all values.
- [var BNNSReduceFunctionL2Norm: BNNSReduceFunction](bnnsreducefunctionl2norm.md)
  A reduction function that computes the Euclidean norm.
- [var BNNSReduceFunctionLogSumExp: BNNSReduceFunction](bnnsreducefunctionlogsumexp.md)
  A reduction function that computes the logarithm of the sum of the exponentials of each element.
- [var BNNSReduceFunctionNone: BNNSReduceFunction](bnnsreducefunctionnone.md)
  A reduction function that copies the input to the output.
- [var BNNSReduceFunctionProduct: BNNSReduceFunction](bnnsreducefunctionproduct.md)
  A reduction function that computes the product of all values.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class ReductionLayer](bnns/reductionlayer.md)
  A layer object that wraps a reduction filter and manages its deinitialization.
- [static func applyReduction(BNNS.ReductionFunction, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, weights: BNNSNDArrayDescriptor?, filterParameters: BNNSFilterParameters?) throws](bnns/applyreduction(_:input:output:weights:filterparameters:).md)
  Applies the specified reduction function.
- [struct BNNSLayerParametersReduction](bnnslayerparametersreduction.md)
  A set of parameters that define a reduction layer.
- [func BNNSFilterCreateLayerReduction(UnsafePointer<BNNSLayerParametersReduction>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerreduction(_:_:).md)
  Returns a new reduction layer.
- [func BNNSDirectApplyReduction(UnsafePointer<BNNSLayerParametersReduction>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsdirectapplyreduction(_:_:).md)
  Applies a reduction operation directly to an input tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsreducefunction)*