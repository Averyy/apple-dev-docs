# shape

**Framework**: Core AI  
**Kind**: property

The length of each dimension of the array.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var shape: [Int] { get }
```

## See Also

- [var scalarType: NDArray.ScalarType](ndarray/scalartype-swift.property.md)
  The scalar type of the array.
- [var strides: [Int]](ndarray/strides.md)
  The distance, in elements, between consecutive values along each dimension.
- [var interleaveLayout: NDArray.InterleaveLayout?](ndarray/interleavelayout-swift.property.md)
  Returns the interleaved layout of this ndArray, or `nil` if there is no interleave.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/shape)*