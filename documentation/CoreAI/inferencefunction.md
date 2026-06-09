# InferenceFunction

**Framework**: Core AI  
**Kind**: struct

A function that performs inference on input values and produces output values.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct InferenceFunction
```

## Mentions

- [Integrating on-device AI models in your app with Core AI](integrating-on-device-ai-models-in-your-app-with-core-ai.md)

#### Overview

An `InferenceFunction` owns the resources needed for inference, including model weights and intermediate buffers. You load a function from an [`AIModel`](aimodel.md) and call `run(inputs:states:outputViews:)` to perform inference.

This type is `Sendable`, so you can run it concurrently from multiple tasks. The function automatically allocates additional intermediate buffers as needed to support concurrency.

## Topics

### Inspecting a function
- [let descriptor: InferenceFunctionDescriptor](inferencefunction/descriptor.md)
  The descriptor for this function’s inputs, outputs, and states.
### Supporting types
- [InferenceFunction.Inputs](inferencefunction/inputs.md)
  A collection of named input values for an inference function.
- [InferenceFunction.Outputs](inferencefunction/outputs.md)
  The output values produced by running an inference function.
### Classes
- [InferenceFunction.AsyncValue](inferencefunction/asyncvalue.md)
  A future which will provide an inference value once any pending write is complete.
### Structures
- [InferenceFunction.AsyncMutableValue](inferencefunction/asyncmutablevalue.md)
  An async value which can be provided as a mutable argument to an inference function.
- [InferenceFunction.AsyncMutableViews](inferencefunction/asyncmutableviews.md)
  A collection of mutable references to async states, used as the states argument to an inference function.
- [InferenceFunction.MutableViews](inferencefunction/mutableviews.md)
  A collection of `InferenceValue.MutableView`s which can be updated in-place by an `InferenceFunction`.
### Instance Methods
- [func encode(inputs: [String : InferenceFunction.AsyncValue], states: consuming InferenceFunction.AsyncMutableViews, outputViews: consuming InferenceFunction.AsyncMutableViews, to: ComputeStream) throws -> [String : InferenceFunction.AsyncValue]](inferencefunction/encode(inputs:states:outputviews:to:).md)
  Encodes the inference to the provided compute stream, returning async values for the outputs.
- [func run(inputs: borrowing InferenceFunction.Inputs, states: consuming InferenceFunction.MutableViews, outputViews: consuming InferenceFunction.MutableViews) async throws -> InferenceFunction.Outputs](inferencefunction/run(inputs:states:outputviews:)-14emi.md)
  Runs the function on the provided input values and returns the output values.
- [func run(inputs: [String : NDArray], states: consuming InferenceFunction.MutableViews, outputViews: consuming InferenceFunction.MutableViews) async throws -> InferenceFunction.Outputs](inferencefunction/run(inputs:states:outputviews:)-mqfb.md)
  Runs the function on the provided input arrays and returns the output values.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct InferenceFunctionDescriptor](inferencefunctiondescriptor.md)
  A description of an inference function’s signature.
- [struct InferenceValue](inferencevalue.md)
  A value that an inference function accepts as input or produces as output.
- [struct ImageDescriptor](imagedescriptor.md)
  A description of an image’s dimensions and pixel format.
- [class ComputeStream](computestream.md)
  A stream of work to be run asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunction)*