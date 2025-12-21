# BNNS.PoolingType

**Framework**: Accelerate  
**Kind**: enum

Constants that describe pooling types.

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
enum PoolingType
```

## Topics

### Pooling Types
- [BNNS.PoolingType.average(countIncludesPadding:)](bnns/poolingtype/average(countincludespadding:).md)
  A function for pooling that computes the average of each element in the pooling kernel.
- [BNNS.PoolingType.l2Norm](bnns/poolingtype/l2norm.md)
  A function for pooling that computes the square root of the sum of squares of each element in the pooling kernel.
- [case max(indices: UnsafeMutableBufferPointer<Int>?, xDilationStride: Int, yDilationStride: Int)](bnns/poolingtype/max(indices:xdilationstride:ydilationstride:).md)
  A function for pooling that computes the maximum of each element in the pooling kernel.
- [case unMax(indices: UnsafeMutableBufferPointer<Int>?, xDilationStride: Int, yDilationStride: Int)](bnns/poolingtype/unmax(indices:xdilationstride:ydilationstride:).md)
  A function for pooling that’s the partial inverse of max pooling and sets all nonmaximal values to zero.
### Instance Properties
- [var bnnsPoolingFunction: BNNSPoolingFunction](bnns/poolingtype/bnnspoolingfunction.md)
  The underlying pooling function structure.
### Enumeration Cases
- [case maxEx(indicesDescriptor: BNNSNDArrayDescriptor?, xDilationStride: Int, yDilationStride: Int)](bnns/poolingtype/maxex(indicesdescriptor:xdilationstride:ydilationstride:).md)
- [case unMaxEx(indicesDescriptor: BNNSNDArrayDescriptor, xDilationStride: Int, yDilationStride: Int)](bnns/poolingtype/unmaxex(indicesdescriptor:xdilationstride:ydilationstride:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/poolingtype)*