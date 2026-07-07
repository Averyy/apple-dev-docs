# init(unsafeBuffer:byteOffset:scalarType:shape:strides:interleaveLayout:)

**Framework**: Core AI  
**Kind**: init

Creates an async ndArray value that directly references the provided metal buffer, interpreted as the specified scalar type and shape.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(unsafeBuffer: consuming any MTLBuffer, byteOffset: Int = 0, scalarType: NDArray.ScalarType, shape: [Int], strides: [Int] = [], interleaveLayout: NDArray.InterleaveLayout? = nil)
```

#### Discussion

`unsafeBuffer` must have `shared` storage mode.

Initializing an async value this way requires that you manually ensure the provided metal buffer is not mutated while this value is being used by an inference function.

- unsafeBuffer: The metal buffer to be referenced by the resulting value.
- byteOffset: The offset into this metal buffer to be interpreted as the start of this value.
- scalarType: The type of scalars in the provided buffer.
- shape: The shape of the resulting value.
- strides: The strides of the resulting value. If left empty, they will be computed as contiguous row-major.
- interleaveLayout: Which dimension is interleaved and by what factor. See [`NDArray.InterleaveLayout`](ndarray/interleavelayout-swift.struct.md).

## See Also

- [init(CVReadOnlyPixelBuffer)](inferencefunction/asyncvalue/init(_:)-5qtut.md)
  Initialize the `AsyncValue` holding the provided pixel buffer.
- [init(consuming InferenceFunction.AsyncMutableValue)](inferencefunction/asyncvalue/init(_:)-90hbj.md)
  Initialize an async value from an existing mutable async value.
- [init(consuming NDArray)](inferencefunction/asyncvalue/init(_:)-9wk3.md)
  Initialize the `AsyncValue` holding the provided ndArray.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/asyncvalue/init(unsafebuffer:byteoffset:scalartype:shape:strides:interleavelayout:))*