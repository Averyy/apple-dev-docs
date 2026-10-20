# functionNames

**Framework**: Core AI  
**Kind**: property  
**Role**: Instance Property

The names of the inference functions in this model.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var functionNames: [String] { get }
```

## Mentions

- [Integrating on-device AI models in your app with Core AI](../integrating-on-device-ai-models-in-your-app-with-core-ai.md)

## See Also

### Loading inference functions
- [func loadFunction(named: String) throws -> InferenceFunction?](./loadfunction%28named%29.md)
- [func functionDescriptor(for: String) -> InferenceFunctionDescriptor?](./functiondescriptor%28for%29.md)
  Returns a descriptor for the specified function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodel/functionnames)*