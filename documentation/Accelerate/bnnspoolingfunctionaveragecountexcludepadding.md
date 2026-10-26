# BNNSPoolingFunctionAverageCountExcludePadding

**Framework**: Accelerate  
**Kind**: var  
**Role**: Global Variable

A function for pooling that computes the average of each element in the pooling kernel, excluding zero-padding.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var BNNSPoolingFunctionAverageCountExcludePadding: BNNSPoolingFunction { get }
```

```c
BNNSPoolingFunctionAverageCountExcludePadding
```

## See Also

### Raw Values
- [init(UInt32)](./bnnspoolingfunction/init%28_%29.md)
- [init(rawValue: UInt32)](./bnnspoolingfunction/init%28rawvalue%29.md)
- [var rawValue: UInt32](./bnnspoolingfunction/rawvalue.md)
- [var BNNSPoolingFunctionUnMax: BNNSPoolingFunction](./bnnspoolingfunctionunmax.md)
  A function for pooling that’s the partial inverse of max pooling and sets all nonmaximal values to zero.
- [var BNNSPoolingFunctionAverageCountIncludePadding: BNNSPoolingFunction](./bnnspoolingfunctionaveragecountincludepadding.md)
  A function for pooling that computes the average of each element in the pooling kernel, including zero-padding.
- [var BNNSPoolingFunctionL2Norm: BNNSPoolingFunction](./bnnspoolingfunctionl2norm.md)
  A function for pooling that computes the square root of the sum of squares of each element in the pooling kernel.
- [BNNSPoolingFunctionMax](./bnnspoolingfunction/bnnspoolingfunctionmax.md)
  A function for pooling that computes the maximum of each element in the pooling kernel.
- [BNNSPoolingFunctionAverage](./bnnspoolingfunction/bnnspoolingfunctionaverage.md)
  A function for pooling that computes the average of each element in the pooling kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnspoolingfunctionaveragecountexcludepadding)*