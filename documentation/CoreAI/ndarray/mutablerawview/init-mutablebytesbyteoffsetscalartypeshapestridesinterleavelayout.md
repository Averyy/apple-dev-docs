# init(mutableBytes:byteOffset:scalarType:shape:strides:interleaveLayout:)

**Framework**: Core AI  
**Kind**: init

Initialize a raw view from existing raw memory, interpreted as the specified scalar type.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(mutableBytes: consuming MutableRawSpan, byteOffset: Int = 0, scalarType: NDArray.ScalarType, shape: [Int], strides: [Int] = [], interleaveLayout: NDArray.InterleaveLayout? = nil)
```

#### Discussion

The lifetime of the resulting view copies the lifetime of the provided span.

Note that the provided `scalarType` will be stored and later checked if you attempt to convert the raw view to a typed view.

```swift
let myBytes: MutableRawSpan = ...
let ndArrayMutableRawView = NDArray.MutableRawView(bytes: myBytes, scalarType: .float32, shape: [4, 5])

// This conversion is checked. If the type does not match the originally provided scalar type
// it will trap at runtime.
let floatView = ndArrayMutableRawView.view(as: Float32.self)
```

Also note that the `shape/strides` must not be able to produce offsets that go outside of the range of `mutableBytes`.

**Performance note**: Making an ndArray view from a normal VM pointer to be used as an input or backing of an [`InferenceFunction`](inferencefunction.md) could be a performance anti-pattern if you intend to pass the same underlying memory in repeatedly to many inferences. This can be a function of which compute units the model was specialized for. For example if the inference function runs compute on the GPU or Neural Engine, you may incur a copy of the view into the required memory primitive if it cannot be toll-free converted.

- bytes: The raw bytes to be referenced by the resulting view.
- byteOffset: The offset into the span to be interpreted as the start of this view.
- scalarType: The type of scalars in the provided span.
- shape: The shape of the resulting view.
- strides: The strides of the resulting view. If left empty, they will be computed as contiguous row-major.
- interleaveLayout: Which dimension is interleaved and by what factor. See [`NDArray.InterleaveLayout`](ndarray/interleavelayout-swift.struct.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/mutablerawview/init(mutablebytes:byteoffset:scalartype:shape:strides:interleavelayout:))*