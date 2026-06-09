# InferenceValue

**Framework**: Core AI  
**Kind**: struct

A value that an inference function accepts as input or produces as output.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct InferenceValue
```

## Mentions

- [Integrating on-device AI models in your app with Core AI](integrating-on-device-ai-models-in-your-app-with-core-ai.md)

#### Overview

An `InferenceValue` wraps either an [`NDArray`](ndarray.md) or a pixel buffer, and you retrieve it after inference using the [`ndArray`](inferencevalue/ndarray.md) property.

## Topics

### Inspecting a value
- [var kind: InferenceValue.Kind](inferencevalue/kind-swift.property.md)
  The kind of data this value contains.
- [var ndArray: NDArray?](inferencevalue/ndarray.md)
  The array that the value wraps.
### Creating a value
- [init(consuming CVMutablePixelBuffer)](inferencevalue/init(_:).md)
  Creates an inference value that wraps the specified pixel buffer.
### Describing values
- [InferenceValue.Descriptor](inferencevalue/descriptor.md)
  A description of the type and shape of an inference value.
- [InferenceValue.Kind](inferencevalue/kind-swift.enum.md)
  The type of data an inference value contains.
### Accessing views
- [InferenceValue.View](inferencevalue/view.md)
  A borrowed, read-only view of an inference value.
- [InferenceValue.MutableView](inferencevalue/mutableview.md)
  A borrowed, mutable view of an inference value.
- [InferenceValue.NamedMutableViews](inferencevalue/namedmutableviews.md)
  A collection of named mutable views into inference values.
### Adopting representable protocols
- [InferenceValue.ViewRepresentable](inferencevalue/viewrepresentable.md)
  A type that can provide a read-only view of itself as an inference value.
- [InferenceValue.MutableViewRepresentable](inferencevalue/mutableviewrepresentable.md)
  A type that can provide a mutable view of itself as an inference value.
### Instance Properties
- [var pixelBuffer: CVMutablePixelBuffer?](inferencevalue/pixelbuffer.md)
  Consume this value to access the underlying pixel buffer.

## See Also

- [struct InferenceFunction](inferencefunction.md)
  A function that performs inference on input values and produces output values.
- [struct InferenceFunctionDescriptor](inferencefunctiondescriptor.md)
  A description of an inference function’s signature.
- [struct ImageDescriptor](imagedescriptor.md)
  A description of an image’s dimensions and pixel format.
- [class ComputeStream](computestream.md)
  A stream of work to be run asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencevalue)*