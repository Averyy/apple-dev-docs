# InferenceFunction.AsyncMutableValue

**Framework**: Core AI  
**Kind**: struct  
**Role**: Structure

An async value which can be provided as a mutable argument to an inference function.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct AsyncMutableValue
```

#### Overview

When dispatching an [`encode(inputs:states:outputViews:to:)`](./encode%28inputs,states,outputviews,to%29.md), mutable values are what is included in the states and output vaiews.

Similar to [`InferenceFunction.AsyncValue`](./asyncvalue.md), this type is a wrapper around an underlying inference value, however this type may be mutated repeatedly after construction by providing it as a state argument in sequence to one or more inference functions.

When encoding a sequence of inferences which each mutate the same `AsyncMutableValue`, the framework will insert the necessary synchronization to avoid it being read or written while a previous write is occurring.

## Topics

### Creating an async mutable value
- [init(consuming CVMutablePixelBuffer)](./asyncmutablevalue/init%28_%29-4aqgq.md)
  Initialize the state from an existing pixel buffer.
- [init(consuming NDArray)](./asyncmutablevalue/init%28_%29-x6se.md)
  Initialize the state from an existing ndArray.
- [init(descriptor: consuming InferenceValue.Descriptor)](./asyncmutablevalue/init%28descriptor%29.md)
  Initialize a new state by creating a value matching the provided descriptor.
- [init(unsafeBuffer: consuming any MTLBuffer, byteOffset: Int, scalarType: NDArray.ScalarType, shape: [Int], strides: [Int], interleaveLayout: NDArray.InterleaveLayout?)](./asyncmutablevalue/init%28unsafebuffer,byteoffset,scalartype,shape,strides,interleavelayout%29.md)
  Creates an async ndArray value that directly references the provided metal buffer, interpreted as the specified scalar type and shape.
### Accessing an async mutable value
- [var ndArray: NDArray?](./asyncmutablevalue/ndarray.md)
  Consume this value to access the underlying NDArray once any pending write is complete.
- [var pixelBuffer: CVMutablePixelBuffer?](./asyncmutablevalue/pixelbuffer.md)
  Consume this value to access the underlying pixel buffer once any pending write is complete.

## See Also

### Asynchronous inference
- [InferenceFunction.AsyncValue](./asyncvalue.md)
  A future which will provide an inference value once any pending write is complete.
- [InferenceFunction.AsyncMutableViews](./asyncmutableviews.md)
  A collection of mutable references to async states, used as the states argument to an inference function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/asyncmutablevalue)*