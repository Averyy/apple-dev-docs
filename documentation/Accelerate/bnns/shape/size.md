# size

**Framework**: Accelerate  
**Kind**: property

The size, in elements, of each dimension of the shape.

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
var size: (Int, Int, Int, Int, Int, Int, Int, Int) { get }
```

## See Also

- [var batchStride: Int](bnns/shape/batchstride.md)
  The number of elements between each batch of data in the shape.
- [var layout: BNNSDataLayout](bnns/shape/layout.md)
  The data layout of the shape.
- [var rank: Int](bnns/shape/rank.md)
  The number of dimensions of the shape.
- [var stride: (Int, Int, Int, Int, Int, Int, Int, Int)](bnns/shape/stride.md)
  The stride, in elements, of each dimension of the shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/shape/size)*