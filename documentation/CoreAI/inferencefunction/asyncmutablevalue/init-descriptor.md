# init(descriptor:)

**Framework**: Core AI  
**Kind**: init

Initialize a new state by creating a value matching the provided descriptor.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(descriptor: consuming InferenceValue.Descriptor)
```

#### Discussion

Note that the descriptor must not have a dynamic shape.

## Parameters

- `descriptor`: The descriptor of the inference value to be constructed and held by this state.

## See Also

- [init(consuming CVMutablePixelBuffer)](inferencefunction/asyncmutablevalue/init(_:)-4aqgq.md)
  Initialize the state from an existing pixel buffer.
- [init(consuming NDArray)](inferencefunction/asyncmutablevalue/init(_:)-x6se.md)
  Initialize the state from an existing ndArray.
- [init(unsafeBuffer: consuming any MTLBuffer, byteOffset: Int, scalarType: NDArray.ScalarType, shape: [Int], strides: [Int], interleaveLayout: NDArray.InterleaveLayout?)](inferencefunction/asyncmutablevalue/init(unsafebuffer:byteoffset:scalartype:shape:strides:interleavelayout:).md)
  Creates an async ndArray value that directly references the provided metal buffer, interpreted as the specified scalar type and shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/asyncmutablevalue/init(descriptor:))*