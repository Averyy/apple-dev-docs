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

- [init(consuming CVMutablePixelBuffer)](inferencefunction/asyncmutablevalue/init(_:)-4aqgq.md)
  Initialize the state from an existing pixel buffer.
- [init(consuming NDArray)](inferencefunction/asyncmutablevalue/init(_:)-x6se.md)
  Initialize the state from an existing ndArray.
- [init(descriptor: consuming InferenceValue.Descriptor)](inferencefunction/asyncmutablevalue/init(descriptor:).md)
  Initialize a new state by creating a value matching the provided descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/asyncmutablevalue/init(unsafebuffer:byteoffset:scalartype:shape:strides:interleavelayout:))*