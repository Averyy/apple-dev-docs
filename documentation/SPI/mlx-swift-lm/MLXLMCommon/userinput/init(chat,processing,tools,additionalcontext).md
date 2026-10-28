---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/userinput/init(chat:processing:tools:additionalcontext:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# init(chat:processing:tools:additionalContext:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: init  
**Role**: Initializer

Initialize the `UserInput` with a model agnostic structured context.

## Declaration

```swift
init(chat: [Chat.Message], processing: Processing = .init(), tools: [ToolSpec]? = nil, additionalContext: [String : any Sendable]? = nil)
```

## Discussion

For example:

```
let chat: [Chat.Message] = [
    .system("You are a helpful photographic assistant."),
    .user("Please describe the photo.", images: [image1]),
]
let userInput = UserInput(chat: chat)
```

A model specific [`MessageGenerator`](../messagegenerator.md) (supplied by the [`UserInputProcessor`](../userinputprocessor.md)) is used to convert this into a model specific format.

### See Also

- [`UserInput.Prompt.text(_:)`](./prompt-swift.enum/text%28_%29.md)
- [`init(chat:processing:tools:additionalContext:)`](./init%28chat,processing,tools,additionalcontext%29.md)

## Parameters

- `chat`: Structured content
- `processing`: Optional processing to be applied to media
- `tools`: Optional tool specifications
- `additionalContext`: Optional context (model specific)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/userinput/init(chat:processing:tools:additionalcontext:))*