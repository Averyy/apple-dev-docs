---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/init(_:instructions:history:speculativedecoding:generateparameters:components:processing:additionalcontext:tools:tooldispatch:)-5cb5s"
framework: "mlx-swift-lm/MLXLMCommon"
---

# init(_:instructions:history:speculativeDecoding:generateParameters:components:processing:additionalContext:tools:toolDispatch:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: init  
**Role**: Initializer

Initialize the `ChatSession` with an existing message history.

## Declaration

```swift
init(_ model: ModelContext, instructions: String? = nil, history: [Chat.Message], speculativeDecoding: SpeculativeDecodingConfig? = nil, generateParameters: GenerateParameters = .init(), components: GenerationComponents = .init(), processing: UserInput.Processing = .init(resize: CGSize(width: 512, height: 512)), additionalContext: [String : any Sendable]? = nil, tools: [ToolSpec]? = nil, toolDispatch: (@Sendable (ToolCall) async throws -> String)? = nil)
```

## Discussion

This enables “Prompt Re-hydration” for persistent chat applications.

## Parameters

- `model`: The [`ModelContext`](../modelcontext.md)
- `instructions`: Optional system instructions for the session
- `history`: The full array of messages to restore (including system prompt)
- `speculativeDecoding`: Optional speculative decoding configuration for faster generation
- `generateParameters`: Parameters that control generation
- `components`: Optional behavioral components, e.g. a custom [`LogitProcessor`](../logitprocessor.md)
- `processing`: Media processing configuration for images/videos
- `additionalContext`: Optional model-specific context
- `tools`: Optional tool specifications
- `toolDispatch`: Optional tool dispatch – required for toolcalls if streaming strings rather than details


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/init(_:instructions:history:speculativedecoding:generateparameters:components:processing:additionalcontext:tools:tooldispatch:)-5cb5s)*