# contextSize

**Framework**: Foundation Models  
**Kind**: property

Returns the maximum context size (in tokens) supported by the model.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@backDeployed(before: iOS 26.4, macOS 26.4, visionOS 26.4)
final var contextSize: Int { get async throws }
```

#### Return Value

The maximum number of tokens the model can process in a single context.

#### Discussion

The context size represents the total number of tokens that can be used in a single session, including both input prompts and generated responses.

> **Note**: An error if the context size cannot be determined. Typically this is due to the model not being available or Apple Intelligence is disabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/contextsize)*