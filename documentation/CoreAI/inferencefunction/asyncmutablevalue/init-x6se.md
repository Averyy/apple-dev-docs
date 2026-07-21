# init(_:)

**Framework**: Core AI  
**Kind**: init

Initialize the state from an existing ndArray.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(_ ndArray: consuming NDArray)
```

#### Discussion

> **Note**: The ndArray will be eagerly copied if not uniquely referenced.

## Parameters

- `ndArray`: The starting ndArray value of this state.

## See Also

- [init(consuming CVMutablePixelBuffer)](inferencefunction/asyncmutablevalue/init(_:)-4aqgq.md)
  Initialize the state from an existing pixel buffer.
- [init(descriptor: consuming InferenceValue.Descriptor)](inferencefunction/asyncmutablevalue/init(descriptor:).md)
  Initialize a new state by creating a value matching the provided descriptor.
- [init(unsafeBuffer: consuming any MTLBuffer, byteOffset: Int, scalarType: NDArray.ScalarType, shape: [Int], strides: [Int], interleaveLayout: NDArray.InterleaveLayout?)](inferencefunction/asyncmutablevalue/init(unsafebuffer:byteoffset:scalartype:shape:strides:interleavelayout:).md)
  Creates an async ndArray value that directly references the provided metal buffer, interpreted as the specified scalar type and shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/asyncmutablevalue/init(_:)-x6se)*