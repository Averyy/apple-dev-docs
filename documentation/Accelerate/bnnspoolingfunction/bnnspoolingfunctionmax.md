# BNNSPoolingFunctionMax

**Framework**: Accelerate  
**Kind**: case  
**Role**: Enumeration Case

A function for pooling that computes the maximum of each element in the pooling kernel.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```c
BNNSPoolingFunctionMax
```

## See Also

### Raw Values
- [var BNNSPoolingFunctionUnMax: BNNSPoolingFunction](../bnnspoolingfunctionunmax.md)
  A function for pooling that’s the partial inverse of max pooling and sets all nonmaximal values to zero.
- [BNNSPoolingFunctionAverage](./bnnspoolingfunctionaverage.md)
  A function for pooling that computes the average of each element in the pooling kernel.
- [var BNNSPoolingFunctionAverageCountIncludePadding: BNNSPoolingFunction](../bnnspoolingfunctionaveragecountincludepadding.md)
  A function for pooling that computes the average of each element in the pooling kernel, including zero-padding.
- [var BNNSPoolingFunctionAverageCountExcludePadding: BNNSPoolingFunction](../bnnspoolingfunctionaveragecountexcludepadding.md)
  A function for pooling that computes the average of each element in the pooling kernel, excluding zero-padding.
- [var BNNSPoolingFunctionL2Norm: BNNSPoolingFunction](../bnnspoolingfunctionl2norm.md)
  A function for pooling that computes the square root of the sum of squares of each element in the pooling kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnspoolingfunction/bnnspoolingfunctionmax)*