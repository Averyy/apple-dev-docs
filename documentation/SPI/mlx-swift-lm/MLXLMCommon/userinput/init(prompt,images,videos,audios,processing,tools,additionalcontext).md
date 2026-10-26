---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/userinput/init(prompt:images:videos:audios:processing:tools:additionalcontext:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# init(prompt:images:videos:audios:processing:tools:additionalContext:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: init  
**Role**: Initializer

Initialize the `UserInput` with a preconfigured [`UserInput.Prompt`](./prompt-swift.enum.md).

## Declaration

```swift
init(prompt: Prompt, images: [Image] = [Image](), videos: [Video] = [Video](), audios: [Audio] = [Audio](), processing: Processing = .init(), tools: [ToolSpec]? = nil, additionalContext: [String : any Sendable]? = nil)
```

#### Discussion

[`init(chat:processing:tools:additionalContext:)`](./init%28chat,processing,tools,additionalcontext%29.md) is the preferred mechanism.

##### See Also

- [`UserInput.Prompt.text(_:)`](./prompt-swift.enum/text%28_%29.md)
- [`init(chat:processing:tools:additionalContext:)`](./init%28chat,processing,tools,additionalcontext%29.md)

## Parameters

- `prompt`: The prompt
- `images`: Optional images
- `videos`: Optional videos
- `audios`: Optional audios
- `processing`: Optional processing to be applied to media
- `tools`: Optional tool specifications
- `additionalContext`: Optional context (model specific)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/userinput/init(prompt:images:videos:audios:processing:tools:additionalcontext:))*