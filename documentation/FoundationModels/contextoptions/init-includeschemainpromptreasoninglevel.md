# init(includeSchemaInPrompt:reasoningLevel:)

**Framework**: Foundation Models  
**Kind**: init

Creates prompting options that controls how the model is prompted.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(includeSchemaInPrompt: Bool? = nil, reasoningLevel: ContextOptions.ReasoningLevel? = nil)
```

## Parameters

- `includeSchemaInPrompt`: Inject the schema into the prompt to bias the model.
- `reasoningLevel`: Controls the amount of thinking that the model is allowed to output before producing a response


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/contextoptions/init(includeschemainprompt:reasoninglevel:))*