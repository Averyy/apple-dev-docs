# BNNS.PoolingType.average(countIncludesPadding:)

**Framework**: Accelerate  
**Kind**: case

A function for pooling that computes the average of each element in the pooling kernel.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
case average(countIncludesPadding: Bool)
```

## See Also

- [BNNS.PoolingType.l2Norm](bnns/poolingtype/l2norm.md)
  A function for pooling that computes the square root of the sum of squares of each element in the pooling kernel.
- [case max(indices: UnsafeMutableBufferPointer<Int>?, xDilationStride: Int, yDilationStride: Int)](bnns/poolingtype/max(indices:xdilationstride:ydilationstride:).md)
  A function for pooling that computes the maximum of each element in the pooling kernel.
- [case unMax(indices: UnsafeMutableBufferPointer<Int>?, xDilationStride: Int, yDilationStride: Int)](bnns/poolingtype/unmax(indices:xdilationstride:ydilationstride:).md)
  A function for pooling that’s the partial inverse of max pooling and sets all nonmaximal values to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/poolingtype/average(countincludespadding:))*