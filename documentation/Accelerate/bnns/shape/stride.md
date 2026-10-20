# stride

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The stride, in elements, of each dimension of the shape.

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
var stride: (Int, Int, Int, Int, Int, Int, Int, Int) { get }
```

## See Also

### Inspecting the Properties of a Shape
- [var batchStride: Int](./batchstride.md)
  The number of elements between each batch of data in the shape.
- [var layout: BNNSDataLayout](./layout.md)
  The data layout of the shape.
- [var rank: Int](./rank.md)
  The number of dimensions of the shape.
- [var size: (Int, Int, Int, Int, Int, Int, Int, Int)](./size.md)
  The size, in elements, of each dimension of the shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/shape/stride)*