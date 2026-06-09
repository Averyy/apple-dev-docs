# init(shape:scalarType:strides:interleaveLayout:)

**Framework**: Core AI  
**Kind**: init

Initialize an NDArray with the provided shape, scalar type, strides, and interleaved dimension.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(shape: [Int], scalarType: NDArray.ScalarType, strides: [Int], interleaveLayout: NDArray.InterleaveLayout)
```

#### Discussion

`shape` and `strides` must have the same number of elements.

## Parameters

- `shape`: The length of each dimension of the ndArray.
- `scalarType`: The type of elements in the ndArray.
- `strides`: The strides of the ndArray.
- `interleaveLayout`: Which dimension is interleaved and by what factor. See [`NDArray.InterleaveLayout`](ndarray/interleavelayout-swift.struct.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/init(shape:scalartype:strides:interleavelayout:))*