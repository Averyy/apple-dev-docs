# inputDescriptor(of:)

**Framework**: Core AI  
**Kind**: method

Returns the descriptor for the specified input.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func inputDescriptor(of inputName: String) -> InferenceValue.Descriptor?
```

## Mentions

- [Integrating on-device AI models in your app with Core AI](integrating-on-device-ai-models-in-your-app-with-core-ai.md)

#### Return Value

The descriptor for the input, or `nil` if the function doesn’t have an input with the specified name.

## Parameters

- `inputName`: The name of the input.

## See Also

- [var inputCount: Int](inferencefunctiondescriptor/inputcount.md)
  The number of inputs the function accepts.
- [var inputNames: [String]](inferencefunctiondescriptor/inputnames.md)
  The names of the function’s inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencefunctiondescriptor/inputdescriptor(of:))*