# strides

**Framework**: Core AI  
**Kind**: property

The distance, in elements, between consecutive values along each dimension.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var strides: [Int] { get }
```

#### Discussion

The strides array has the same number of elements as [`shape`](ndarray/shape.md), where `strides[i]` describes the distance between consecutive elements in the `i`th dimension.

## See Also

- [var shape: [Int]](ndarray/shape.md)
  The length of each dimension of the array.
- [var scalarType: NDArray.ScalarType](ndarray/scalartype-swift.property.md)
  The scalar type of the array.
- [var interleaveLayout: NDArray.InterleaveLayout?](ndarray/interleavelayout-swift.property.md)
  Returns the interleaved layout of this ndArray, or `nil` if there is no interleave.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/strides)*