# init(metalBuffer:byteOffset:scalarType:shape:strides:interleaveLayout:)

**Framework**: Core AI  
**Kind**: init

Initialize a raw view from an existing metal buffer, interpreted as the specified scalar type.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(metalBuffer: borrowing any MTLBuffer, byteOffset: Int = 0, scalarType: NDArray.ScalarType, shape: [Int], strides: [Int] = [], interleaveLayout: NDArray.InterleaveLayout? = nil)
```

#### Discussion

`metalBuffer` must have `shared` storage mode.

Note that the provided `scalarType` will be stored and later checked if you attempt to convert the raw view to a typed view.

Also note that the `shape/strides` must not be able to produce offsets that go outside of the range of `metalBuffer`.

This initializer is unsafe, you are responsible for ensuring that no other code (or GPU pipeline) writes to the buffer while the resulting view is alive.

- metalBuffer: The metal buffer to be referenced by the resulting view.
- byteOffset: The offset into this metal buffer to be interpreted as the start of this view.
- scalarType: The type of scalars in the provided span.
- shape: The shape of the resulting view.
- strides: The strides of the resulting view. If left empty, they will be computed as contiguous row-major.
- interleaveLayout: Which dimension is interleaved and by what factor. See [`NDArray.InterleaveLayout`](ndarray/interleavelayout-swift.struct.md).

## See Also

- [init(bytes: RawSpan, byteOffset: Int, scalarType: NDArray.ScalarType, shape: [Int], strides: [Int], interleaveLayout: NDArray.InterleaveLayout?)](ndarray/rawview/init(bytes:byteoffset:scalartype:shape:strides:interleavelayout:).md)
  Initialize a raw view from existing raw memory, interpreted as the specified scalar type.
- [init(ioSurface: borrowing IOSurface, byteOffset: Int, scalarType: NDArray.ScalarType, shape: [Int], strides: [Int], interleaveLayout: NDArray.InterleaveLayout?)](ndarray/rawview/init(iosurface:byteoffset:scalartype:shape:strides:interleavelayout:).md)
  Initialize a raw view from an existing IOSurface, interpreted as the specified scalar type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/rawview/init(metalbuffer:byteoffset:scalartype:shape:strides:interleavelayout:))*