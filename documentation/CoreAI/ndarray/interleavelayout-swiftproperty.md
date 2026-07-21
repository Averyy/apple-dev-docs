# interleaveLayout

**Framework**: Core AI  
**Kind**: property

Returns the interleaved layout of this ndArray, or `nil` if there is no interleave.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var interleaveLayout: NDArray.InterleaveLayout? { get }
```

#### Discussion

See [`NDArray.InterleaveLayout`](ndarray/interleavelayout-swift.struct.md) for full documentation.

## See Also

- [var shape: [Int]](ndarray/shape.md)
  The length of each dimension of the array.
- [var scalarType: NDArray.ScalarType](ndarray/scalartype-swift.property.md)
  The scalar type of the array.
- [var strides: [Int]](ndarray/strides.md)
  The distance, in elements, between consecutive values along each dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/interleavelayout-swift.property)*