# init(_:)

**Framework**: Core AI  
**Kind**: init  
**Role**: Initializer

Initialize an async value from an existing mutable async value.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(_ mutableValue: consuming InferenceFunction.AsyncMutableValue)
```

## Parameters

- `mutableValue`: The mutable value that this value will be initialized from. The resulting value will reference the same underlying value within the mutable value and carry the same event to signal when the value is ready.

## See Also

### Creating an async value
- [init(CVReadOnlyPixelBuffer)](./init%28_%29-5qtut.md)
  Initialize the `AsyncValue` holding the provided pixel buffer.
- [init(consuming NDArray)](./init%28_%29-9wk3.md)
  Initialize the `AsyncValue` holding the provided ndArray.
- [init(unsafeBuffer: consuming any MTLBuffer, byteOffset: Int, scalarType: NDArray.ScalarType, shape: [Int], strides: [Int], interleaveLayout: NDArray.InterleaveLayout?)](./init%28unsafebuffer,byteoffset,scalartype,shape,strides,interleavelayout%29.md)
  Creates an async ndArray value that directly references the provided metal buffer, interpreted as the specified scalar type and shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/asyncvalue/init(_:)-90hbj)*