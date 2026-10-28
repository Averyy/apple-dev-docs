---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/userinput/init(messages:images:videos:audios:tools:additionalcontext:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# init(messages:images:videos:audios:tools:additionalContext:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: init  
**Role**: Initializer

Initialize the `UserInput` with model specific mesage structures.

## Declaration

```swift
init(messages: [Message], images: [Image] = [Image](), videos: [Video] = [Video](), audios: [Audio] = [Audio](), tools: [ToolSpec]? = nil, additionalContext: [String : any Sendable]? = nil)
```

## Discussion

For example, the Qwen2VL model wants input in this format:

```
[
    [
        "role": "user",
        "content": [
            [
                "type": "text",
                "text": "What is this?"
            ],
            [
                "type": "image",
            ],
        ]
    ]
]
```

Typically the [`init(chat:processing:tools:additionalContext:)`](./init%28chat,processing,tools,additionalcontext%29.md) should be used instead along with a model specific [`MessageGenerator`](../messagegenerator.md) (supplied by the [`UserInputProcessor`](../userinputprocessor.md)).

### See Also

- [`UserInput.Prompt.text(_:)`](./prompt-swift.enum/text%28_%29.md)
- [`init(chat:processing:tools:additionalContext:)`](./init%28chat,processing,tools,additionalcontext%29.md)

## Parameters

- `messages`: Array of dictionaries representing the prompt in a model specific format
- `images`: Optional images
- `videos`: Optional videos
- `audios`: Optional audios
- `tools`: Optional tool specifications
- `additionalContext`: Optional context (model specific)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/userinput/init(messages:images:videos:audios:tools:additionalcontext:))*