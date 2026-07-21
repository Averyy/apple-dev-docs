# init(_:)

**Framework**: Core AI  
**Kind**: init

Initialize an async value from an existing mutable async value.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(_ mutableValue: consuming InferenceFunction.AsyncMutableValue)
```

## Parameters

- `mutableValue`: The mutable value that this value will be initialized from. The resulting value will reference the same underlying value within the mutable value and carry the same event to signal when the value is ready.

## See Also

- [init(CVReadOnlyPixelBuffer)](inferencefunction/asyncvalue/init(_:)-5qtut.md)
  Initialize the `AsyncValue` holding the provided pixel buffer.
- [init(consuming NDArray)](inferencefunction/asyncvalue/init(_:)-9wk3.md)
  Initialize the `AsyncValue` holding the provided ndArray.
- [init(unsafeBuffer: consuming any MTLBuffer, byteOffset: Int, scalarType: NDArray.ScalarType, shape: [Int], strides: [Int], interleaveLayout: NDArray.InterleaveLayout?)](inferencefunction/asyncvalue/init(unsafebuffer:byteoffset:scalartype:shape:strides:interleavelayout:).md)
  Creates an async ndArray value that directly references the provided metal buffer, interpreted as the specified scalar type and shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/asyncvalue/init(_:)-90hbj)*