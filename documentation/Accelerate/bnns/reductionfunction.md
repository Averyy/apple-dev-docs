# BNNS.ReductionFunction

**Framework**: Accelerate  
**Kind**: enum  
**Role**: Enumeration

Constants that describe reduction functions.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

## Declaration

```swift
enum ReductionFunction
```

## Topics

### Reduction Functions
- [BNNS.ReductionFunction.max](./reductionfunction/max.md)
  A reduction function that computes the maximum value.
- [BNNS.ReductionFunction.argMax](./reductionfunction/argmax.md)
  A reduction function that computes the index of the maximum value.
- [BNNS.ReductionFunction.mean](./reductionfunction/mean.md)
  A function for reduction that computes the mean value.
- [BNNS.ReductionFunction.meanNonZero](./reductionfunction/meannonzero.md)
  A reduction function that computes the mean value of nonzero elements.
- [BNNS.ReductionFunction.min](./reductionfunction/min.md)
  A reduction function that computes the minimum value.
- [BNNS.ReductionFunction.argMin](./reductionfunction/argmin.md)
  A reduction function that computes the index of the minimum value.
- [BNNS.ReductionFunction.sum](./reductionfunction/sum.md)
  A reduction function that computes the sum of all values.
- [BNNS.ReductionFunction.sumOfAbsolutes](./reductionfunction/sumofabsolutes.md)
  A reduction function that computes the sum of all absolute values.
- [BNNS.ReductionFunction.sumOfLogs(epsilon:)](./reductionfunction/sumoflogs%28epsilon%29.md)
  A reduction function that computes the sum of the natural logarithm of all values.
- [BNNS.ReductionFunction.sumOfSquares](./reductionfunction/sumofsquares.md)
  A reduction function that computes the sum of the square of all values.
- [BNNS.ReductionFunction.logicalAnd](./reductionfunction/logicaland.md)
  A reduction function that computes the logical AND of all values.
- [BNNS.ReductionFunction.all](./reductionfunction/all.md)
  An alias of the logical AND reduction function.
- [BNNS.ReductionFunction.logicalOr](./reductionfunction/logicalor.md)
  A reduction function that computes the logical OR of all values.
- [BNNS.ReductionFunction.any](./reductionfunction/any.md)
  An alias of the logical OR reduction function.
### Instance Properties
- [var bnnsReduceFunction: BNNSReduceFunction](./reductionfunction/bnnsreducefunction.md)
  The underlying reduction function structure.
### Deprecated Symbols
- [BNNS.ReductionFunction.maxIndex](./reductionfunction/maxindex.md)
  A function for reduction that computes the index of the maximum value.
- [BNNS.ReductionFunction.minIndex](./reductionfunction/minindex.md)
  A function for reduction that computes the index of the minimum value.
### Enumeration Cases
- [BNNS.ReductionFunction.l2Norm](./reductionfunction/l2norm.md)
- [BNNS.ReductionFunction.logSumExp](./reductionfunction/logsumexp.md)
- [BNNS.ReductionFunction.product](./reductionfunction/product.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/reductionfunction)*