# InferenceFunction.AsyncValue

**Framework**: Core AI  
**Kind**: class

A future which will provide an inference value once any pending write is complete.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class AsyncValue
```

#### Overview

An `AsyncValue` contains an underlying `InferenceValue` however that value may be actively in-use by some previously dispatched async work, and thus accessing the underlying value below an `AsyncValue` requires an `await` to wait for any previous compute writing it to be complete.

An `AsyncValue` is immutable once any previous compute has completed.

Async values can be used in async pipelines of inference to dispatch multiple inference functions in sequence without waiting for each to complete before dispatching the next. This can improve performance by parallelizing phases of the inferences which are not data dependent:

```swift
 // Pipeline encoding of a text embedding function followed by decoder
 var textTokens: NDArray = ...
 let embeddingOutputs = try textEmbeddingFunction.encode(inputs: ["tokens": .init(textTokens)])
 let embeddings: InferenceFunction.AsyncValue = embeddingsOutputs["embeddings"]

 let decoderOutputs = try decodingFunction.encode(inputs: ["embeddings": embeddings])
 let logits = decoderOutputs["logits"]!
 // Await the compute of logits to be complete
 let logitsNDArray = try await logits.ndArray
```

## Topics

### Initializers
- [init(CVReadOnlyPixelBuffer)](inferencefunction/asyncvalue/init(_:)-5qtut.md)
  Initialize the `AsyncValue` holding the provided pixel buffer.
- [init(consuming InferenceFunction.AsyncMutableValue)](inferencefunction/asyncvalue/init(_:)-90hbj.md)
  Initialize an async value from an existing mutable async value.
- [init(consuming NDArray)](inferencefunction/asyncvalue/init(_:)-9wk3.md)
  Initialize the `AsyncValue` holding the provided ndArray.
- [init(unsafeBuffer: consuming any MTLBuffer, byteOffset: Int, scalarType: NDArray.ScalarType, shape: [Int], strides: [Int], interleaveLayout: NDArray.InterleaveLayout?)](inferencefunction/asyncvalue/init(unsafebuffer:byteoffset:scalartype:shape:strides:interleavelayout:).md)
  Creates an async ndArray value that directly references the provided metal buffer, interpreted as the specified scalar type and shape.
### Instance Properties
- [var kind: InferenceValue.Kind](inferencefunction/asyncvalue/kind.md)
  The kind of inference value held by this async value.
- [var ndArray: NDArray?](inferencefunction/asyncvalue/ndarray.md)
  Waits for any pending write access on the underlying ndArray to complete, then returns it.
- [var pixelBuffer: CVReadOnlyPixelBuffer?](inferencefunction/asyncvalue/pixelbuffer.md)
  Waits for any pending write access on the underlying pixel buffer to complete, then returns it.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction/asyncvalue)*