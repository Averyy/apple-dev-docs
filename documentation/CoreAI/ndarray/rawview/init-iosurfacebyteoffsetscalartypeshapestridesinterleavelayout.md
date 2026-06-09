# init(ioSurface:byteOffset:scalarType:shape:strides:interleaveLayout:)

**Framework**: Core AI  
**Kind**: init

Initialize a raw view from an existing IOSurface, interpreted as the specified scalar type.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(ioSurface: borrowing IOSurface, byteOffset: Int = 0, scalarType: NDArray.ScalarType, shape: [Int], strides: [Int] = [], interleaveLayout: NDArray.InterleaveLayout? = nil)
```

#### Discussion

Note that the pixel format of the IOSurface will be ignored and the `scalarType` you specify will be used. However the `shape` argument will be checked with respect to the `height/width` fields of the IOSurface. For the `height` and `width` fields of the IOSurface, they must meet one of the following conditions:

1. The height/width must be unspecified in which case the `shape` parameter is unconstrained.
2. If the `height/width` fields are present, then the final dimension of `shape` must be equal to `width`, and the product of the remaining dimensions must be equal to `height`.

You are responsible for having locked the base address of the IOSurface before constructing the view from it.

Note that the provided `scalarType` will be stored and later checked if you attempt to convert the raw view to a typed view.

Also note that the `shape/strides` must not be able to produce offsets that go outside of the range of the IOSurface.

This initializer is unsafe, you are responsible for ensuring that no other code writes to the IOSurface while the resulting view is alive.

- ioSurface: The IOSurface to be referenced by the resulting view.
- byteOffset: The offset into this IOSurface to be interpreted as the start of this view.
- scalarType: The type of scalars in the provided span.
- shape: The shape of the resulting view.
- strides: The strides of the resulting view. If left empty, they will be computed as contiguous row-major.
- interleaveLayout: Which dimension is interleaved and by what factor. See [`NDArray.InterleaveLayout`](ndarray/interleavelayout-swift.struct.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/rawview/init(iosurface:byteoffset:scalartype:shape:strides:interleavelayout:))*