# init(includeSchemaInPrompt:reasoningLevel:)

**Framework**: Foundation Models  
**Kind**: init

Creates options that control how the model is prompted.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(includeSchemaInPrompt: Bool? = nil, reasoningLevel: ContextOptions.ReasoningLevel? = nil)
```

## Parameters

- `includeSchemaInPrompt`: If `true`, injects the schema into the prompt to bias the model.
- `reasoningLevel`: Controls the amount of reasoning that the model is allowed to output before producing a response


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/contextoptions/init(includeschemainprompt:reasoninglevel:))*