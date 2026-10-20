# scalarType

**Framework**: Core AI  
**Kind**: property  
**Role**: Instance Property

The scalar type of the array.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var scalarType: NDArray.ScalarType { get }
```

## See Also

### Inspecting an array
- [var shape: [Int]](./shape.md)
  The length of each dimension of the array.
- [var strides: [Int]](./strides.md)
  The distance, in elements, between consecutive values along each dimension.
- [var interleaveLayout: NDArray.InterleaveLayout?](./interleavelayout-swift.property.md)
  Returns the interleaved layout of this ndArray, or `nil` if there is no interleave.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/scalartype-swift.property)*