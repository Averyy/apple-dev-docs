# inputDescriptor(of:)

**Framework**: Core AI  
**Kind**: method  
**Role**: Instance Method

Returns the descriptor for the specified input.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func inputDescriptor(of inputName: String) -> InferenceValue.Descriptor?
```

## Mentions

- [Integrating on-device AI models in your app with Core AI](../integrating-on-device-ai-models-in-your-app-with-core-ai.md)

## Return Value

The descriptor for the input, or `nil` if the function doesn’t have an input with the specified name.

## Parameters

- `inputName`: The name of the input.

## See Also

### Describing inputs
- [var inputCount: Int](./inputcount.md)
  The number of inputs the function accepts.
- [var inputNames: [String]](./inputnames.md)
  The names of the function’s inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunctiondescriptor/inputdescriptor(of:))*