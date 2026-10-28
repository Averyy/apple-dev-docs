---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/init(_:instructions:promptcache:speculativedecoding:generateparameters:components:processing:additionalcontext:tools:tooldispatch:)-7of4u"
framework: "mlx-swift-lm/MLXLMCommon"
---

# init(_:instructions:promptCache:speculativeDecoding:generateParameters:components:processing:additionalContext:tools:toolDispatch:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: init  
**Role**: Initializer

Initialize the `ChatSession` with a prompt cache and the model state that belongs with it.

## Declaration

```swift
convenience init(_ model: ModelContext, instructions: String? = nil, promptCache: consuming PromptCacheSnapshot, speculativeDecoding: SpeculativeDecodingConfig? = nil, generateParameters: GenerateParameters = .init(), components: GenerationComponents = .init(), processing: UserInput.Processing = .init(resize: CGSize(width: 512, height: 512)), additionalContext: [String : any Sendable]? = nil, tools: [ToolSpec]? = nil, toolDispatch: (@Sendable (ToolCall) async throws -> String)? = nil)
```

## Discussion

See [`init(_:instructions:promptCache:speculativeDecoding:generateParameters:components:processing:additionalContext:tools:toolDispatch:)`](./init%28_,instructions,promptcache,speculativedecoding,generateparameters,components,processing,additionalcontext,tools,tooldispatch%29-4h2u4.md) for the continuation behavior a snapshot implies.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/init(_:instructions:promptcache:speculativedecoding:generateparameters:components:processing:additionalcontext:tools:tooldispatch:)-7of4u)*