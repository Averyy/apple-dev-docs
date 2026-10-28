# init(_:)

**Framework**: Core AI  
**Kind**: init  
**Role**: Initializer

Initialize the state from an existing ndArray.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(_ ndArray: consuming NDArray)
```

## Discussion

> **Note**: The ndArray will be eagerly copied if not uniquely referenced.

## Parameters

- `ndArray`: The starting ndArray value of this state.

## See Also

### Creating an async mutable value
- [init(consuming CVMutablePixelBuffer)](./init%28_%29-4aqgq.md)
  Initialize the state from an existing pixel buffer.
- [init(descriptor: consuming InferenceValue.Descriptor)](./init%28descriptor%29.md)
  Initialize a new state by creating a value matching the provided descriptor.
- [init(unsafeBuffer: consuming any MTLBuffer, byteOffset: Int, scalarType: NDArray.ScalarType, shape: [Int], strides: [Int], interleaveLayout: NDArray.InterleaveLayout?)](./init%28unsafebuffer,byteoffset,scalartype,shape,strides,interleavelayout%29.md)
  Creates an async ndArray value that directly references the provided metal buffer, interpreted as the specified scalar type and shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/asyncmutablevalue/init(_:)-x6se)*