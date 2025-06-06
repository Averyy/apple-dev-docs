# BNNS.ReductionFunction

**Framework**: Accelerate  
**Kind**: enum

Constants that describe reduction functions.

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
enum ReductionFunction
```

## Topics

### Reduction Functions
- [BNNS.ReductionFunction.max](bnns/reductionfunction/max.md)
  A reduction function that computes the maximum value.
- [BNNS.ReductionFunction.argMax](bnns/reductionfunction/argmax.md)
  A reduction function that computes the index of the maximum value.
- [BNNS.ReductionFunction.mean](bnns/reductionfunction/mean.md)
  A function for reduction that computes the mean value.
- [BNNS.ReductionFunction.meanNonZero](bnns/reductionfunction/meannonzero.md)
  A reduction function that computes the mean value of nonzero elements.
- [BNNS.ReductionFunction.min](bnns/reductionfunction/min.md)
  A reduction function that computes the minimum value.
- [BNNS.ReductionFunction.argMin](bnns/reductionfunction/argmin.md)
  A reduction function that computes the index of the minimum value.
- [BNNS.ReductionFunction.sum](bnns/reductionfunction/sum.md)
  A reduction function that computes the sum of all values.
- [BNNS.ReductionFunction.sumOfAbsolutes](bnns/reductionfunction/sumofabsolutes.md)
  A reduction function that computes the sum of all absolute values.
- [BNNS.ReductionFunction.sumOfLogs(epsilon:)](bnns/reductionfunction/sumoflogs(epsilon:).md)
  A reduction function that computes the sum of the natural logarithm of all values.
- [BNNS.ReductionFunction.sumOfSquares](bnns/reductionfunction/sumofsquares.md)
  A reduction function that computes the sum of the square of all values.
- [BNNS.ReductionFunction.logicalAnd](bnns/reductionfunction/logicaland.md)
  A reduction function that computes the logical AND of all values.
- [BNNS.ReductionFunction.all](bnns/reductionfunction/all.md)
  An alias of the logical AND reduction function.
- [BNNS.ReductionFunction.logicalOr](bnns/reductionfunction/logicalor.md)
  A reduction function that computes the logical OR of all values.
- [BNNS.ReductionFunction.any](bnns/reductionfunction/any.md)
  An alias of the logical OR reduction function.
### Instance Properties
- [var bnnsReduceFunction: BNNSReduceFunction](bnns/reductionfunction/bnnsreducefunction.md)
  The underlying reduction function structure.
### Deprecated Symbols
- [BNNS.ReductionFunction.maxIndex](bnns/reductionfunction/maxindex.md)
  A function for reduction that computes the index of the maximum value.
- [BNNS.ReductionFunction.minIndex](bnns/reductionfunction/minindex.md)
  A function for reduction that computes the index of the minimum value.
### Enumeration Cases
- [BNNS.ReductionFunction.l2Norm](bnns/reductionfunction/l2norm.md)
- [BNNS.ReductionFunction.logSumExp](bnns/reductionfunction/logsumexp.md)
- [BNNS.ReductionFunction.product](bnns/reductionfunction/product.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/reductionfunction)*