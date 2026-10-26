---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/init(_:instructions:speculativedecoding:generateparameters:components:processing:additionalcontext:tools:tooldispatch:)-943t6"
framework: "mlx-swift-lm/MLXLMCommon"
---

# init(_:instructions:speculativeDecoding:generateParameters:components:processing:additionalContext:tools:toolDispatch:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: init  
**Role**: Initializer

Initialize the `ChatSession`.

## Declaration

```swift
init(_ model: ModelContainer, instructions: String? = nil, speculativeDecoding: SpeculativeDecodingConfig? = nil, generateParameters: GenerateParameters = .init(), components: GenerationComponents = .init(), processing: UserInput.Processing = .init(resize: CGSize(width: 512, height: 512)), additionalContext: [String : any Sendable]? = nil, tools: [ToolSpec]? = nil, toolDispatch: (@Sendable (ToolCall) async throws -> String)? = nil)
```

## Parameters

- `model`: The [`ModelContainer`](../modelcontainer.md)
- `instructions`: Optional system instructions for the session
- `speculativeDecoding`: Optional speculative decoding configuration for faster generation
- `generateParameters`: Parameters that control generation
- `components`: Optional behavioral components, e.g. a custom [`LogitProcessor`](../logitprocessor.md)
- `processing`: Media processing configuration for images/videos
- `additionalContext`: Optional model-specific context
- `tools`: Optional tool specifications
- `toolDispatch`: Optional tool dispatch – required for toolcalls if streaming strings rather than details


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/init(_:instructions:speculativedecoding:generateparameters:components:processing:additionalcontext:tools:tooldispatch:)-943t6)*