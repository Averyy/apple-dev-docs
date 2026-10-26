---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/userinput/init(prompt:images:videos:audios:tools:additionalcontext:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# init(prompt:images:videos:audios:tools:additionalContext:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: init  
**Role**: Initializer

Initialize the `UserInput` with a single text prompt.

## Declaration

```swift
init(prompt: String, images: [Image] = [Image](), videos: [Video] = [Video](), audios: [Audio] = [Audio](), tools: [ToolSpec]? = nil, additionalContext: [String : any Sendable]? = nil)
```

##### See Also

- [`UserInput.Prompt.text(_:)`](./prompt-swift.enum/text%28_%29.md)
- [`init(chat:processing:tools:additionalContext:)`](./init%28chat,processing,tools,additionalcontext%29.md)

## Parameters

- `prompt`: Text prompt
- `images`: Optional images
- `videos`: Optional videos
- `audios`: Optional audios
- `tools`: Optional tool specifications
- `additionalContext`: Optional context (model specific)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/userinput/init(prompt:images:videos:audios:tools:additionalcontext:))*