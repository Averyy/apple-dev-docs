# BNNSReduceFunctionNone

**Framework**: Accelerate  
**Kind**: var

A reduction function that copies the input to the output.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var BNNSReduceFunctionNone: BNNSReduceFunction { get }
```

#### Discussion

BNNS provides this reduction function for use with some functions — such as [`BNNSScatter(_:_:_:_:_:_:)`](bnnsscatter(_:_:_:_:_:_:).md) — to indicate that the operation copies the input to the output. [`BNNSReduceFunctionNone`](bnnsreducefunctionnone.md) isn’t supported by the BNNS reduction layer, use [`BNNSCopy(_:_:_:)`](bnnscopy(_:_:_:).md) to perform a copy or conversion operation.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsreducefunctionnone)*