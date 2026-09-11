# contextSize

**Framework**: Foundation Models  
**Kind**: property

The maximum context size in tokens supported by the model.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
nonisolated
(nonsending) final var contextSize: Int { get async throws }
```

#### Discussion

The context size represents the total number of tokens that can be used in a single session, including both input prompts and generated responses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/privatecloudcomputelanguagemodel/contextsize)*