---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/speculativedecodingconfig/init(draftmodelbytes:numdrafttokens:memorypolicy:loaddraftmodel:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# init(draftModelBytes:numDraftTokens:memoryPolicy:loadDraftModel:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: init  
**Role**: Initializer

Initialize speculative decoding with a draft model loader.

## Declaration

```swift
init(draftModelBytes: Int, numDraftTokens: Int = 5, memoryPolicy: SpeculativeDecodingMemoryPolicy? = nil, loadDraftModel: @escaping @Sendable () async throws -> ModelContainer)
```

#### Discussion

When a memory policy is present, `draftModelBytes` lets `ChatSession` decide whether to use speculative decoding before it loads the draft model. This is the preferred initializer when the draft model may not fit comfortably beside the main model.

## Parameters

- `draftModelBytes`: Estimated resident parameter bytes for the draft model
- `numDraftTokens`: Number of tokens proposed by the draft model per verification cycle
- `memoryPolicy`: Optional memory policy used before loading the draft model
- `loadDraftModel`: Closure that loads the draft model only if speculation is admitted


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/speculativedecodingconfig/init(draftmodelbytes:numdrafttokens:memorypolicy:loaddraftmodel:))*