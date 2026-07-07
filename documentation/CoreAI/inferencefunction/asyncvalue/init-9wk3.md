# init(_:)

**Framework**: Core AI  
**Kind**: init

Initialize the `AsyncValue` holding the provided ndArray.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(_ ndArray: consuming NDArray)
```

## See Also

- [init(CVReadOnlyPixelBuffer)](inferencefunction/asyncvalue/init(_:)-5qtut.md)
  Initialize the `AsyncValue` holding the provided pixel buffer.
- [init(consuming InferenceFunction.AsyncMutableValue)](inferencefunction/asyncvalue/init(_:)-90hbj.md)
  Initialize an async value from an existing mutable async value.
- [init(unsafeBuffer: consuming any MTLBuffer, byteOffset: Int, scalarType: NDArray.ScalarType, shape: [Int], strides: [Int], interleaveLayout: NDArray.InterleaveLayout?)](inferencefunction/asyncvalue/init(unsafebuffer:byteoffset:scalartype:shape:strides:interleavelayout:).md)
  Creates an async ndArray value that directly references the provided metal buffer, interpreted as the specified scalar type and shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/asyncvalue/init(_:)-9wk3)*