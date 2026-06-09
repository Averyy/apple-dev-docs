# InferenceFunctionDescriptor

**Framework**: Core AI  
**Kind**: struct

A description of an inference function’s signature.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct InferenceFunctionDescriptor
```

## Mentions

- [Integrating on-device AI models in your app with Core AI](integrating-on-device-ai-models-in-your-app-with-core-ai.md)

#### Overview

Use a descriptor to inspect the names and types of a function’s inputs, outputs, and states before running inference. You obtain a descriptor from [`functionDescriptor(for:)`](aimodel/functiondescriptor(for:).md) or from the [`descriptor`](inferencefunction/descriptor.md) property.

## Topics

### Identifying the function
- [var name: String](inferencefunctiondescriptor/name.md)
  The function’s name.
### Describing inputs
- [var inputCount: Int](inferencefunctiondescriptor/inputcount.md)
  The number of inputs the function accepts.
- [var inputNames: [String]](inferencefunctiondescriptor/inputnames.md)
  The names of the function’s inputs.
- [func inputDescriptor(of: String) -> InferenceValue.Descriptor?](inferencefunctiondescriptor/inputdescriptor(of:).md)
  Returns the descriptor for the specified input.
### Describing outputs
- [var outputCount: Int](inferencefunctiondescriptor/outputcount.md)
  The number of outputs the function produces.
- [var outputNames: [String]](inferencefunctiondescriptor/outputnames.md)
  The names of the function’s outputs.
- [func outputDescriptor(of: String) -> InferenceValue.Descriptor?](inferencefunctiondescriptor/outputdescriptor(of:).md)
  Returns the descriptor for the specified output.
### Describing state
- [var stateNames: [String]](inferencefunctiondescriptor/statenames.md)
  The names of the function’s states.
- [func stateDescriptor(of: String) -> InferenceValue.Descriptor?](inferencefunctiondescriptor/statedescriptor(of:).md)
  Returns the descriptor for the specified state.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct InferenceFunction](inferencefunction.md)
  A function that performs inference on input values and produces output values.
- [struct InferenceValue](inferencevalue.md)
  A value that an inference function accepts as input or produces as output.
- [struct ImageDescriptor](imagedescriptor.md)
  A description of an image’s dimensions and pixel format.
- [class ComputeStream](computestream.md)
  A stream of work to be run asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunctiondescriptor)*