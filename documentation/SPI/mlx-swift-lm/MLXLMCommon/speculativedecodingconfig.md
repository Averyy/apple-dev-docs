---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/speculativedecodingconfig"
framework: "mlx-swift-lm/MLXLMCommon"
---

# SpeculativeDecodingConfig

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Configuration for speculative decoding in a `ChatSession`.

## Declaration

```swift
struct SpeculativeDecodingConfig
```

#### Overview

Speculative decoding uses a small draft model to propose candidate tokens that the main model then verifies in a single forward pass, providing a speedup with no quality degradation when both models fit comfortably in memory.

Both models must share the same tokenizer vocabulary.

Example usage:

```swift
let main  = try await LLMModelFactory.shared.loadContainer(configuration: mainConfig)
let draft = try await LLMModelFactory.shared.loadContainer(configuration: draftConfig)

let session = ChatSession(
    main,
    speculativeDecoding: SpeculativeDecodingConfig(draftModel: draft, numDraftTokens: 5)
)
```

To avoid loading a draft model that would exceed a memory policy, pass a byte estimate and a loader closure:

```swift
let session = ChatSession(
    main,
    speculativeDecoding: SpeculativeDecodingConfig(
        draftModelBytes: estimatedDraftBytes,
        memoryPolicy: .recommendedWorkingSet
    ) {
        try await LLMModelFactory.shared.loadContainer(configuration: draftConfig)
    }
)
```

## Topics

### Initializers
- [init(draftModel: ModelContainer, numDraftTokens: Int, memoryPolicy: SpeculativeDecodingMemoryPolicy?)](./speculativedecodingconfig/init%28draftmodel,numdrafttokens,memorypolicy%29.md)
- [init(draftModelBytes: Int, numDraftTokens: Int, memoryPolicy: SpeculativeDecodingMemoryPolicy?, loadDraftModel: @Sendable () async throws -> ModelContainer)](./speculativedecodingconfig/init%28draftmodelbytes,numdrafttokens,memorypolicy,loaddraftmodel%29.md)
  Initialize speculative decoding with a draft model loader.
### Instance Properties
- [var draftModel: ModelContainer?](./speculativedecodingconfig/draftmodel.md)
  The lightweight model used to propose candidate tokens, when it was provided eagerly.
- [let memoryPolicy: SpeculativeDecodingMemoryPolicy?](./speculativedecodingconfig/memorypolicy.md)
  Optional memory policy used to decide whether auxiliary-model speculation should run. Pass `.recommendedWorkingSet` to fall back to regular generation when the combined main and draft model parameters exceed the recommended working set.
- [let numDraftTokens: Int](./speculativedecodingconfig/numdrafttokens.md)
  Number of tokens proposed by the draft model per verification cycle. The default value of 5 offers a good balance between speed and accuracy.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/speculativedecodingconfig)*