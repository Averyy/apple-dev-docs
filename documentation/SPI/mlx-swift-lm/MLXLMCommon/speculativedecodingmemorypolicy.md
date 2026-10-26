---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/speculativedecodingmemorypolicy"
framework: "mlx-swift-lm/MLXLMCommon"
---

# SpeculativeDecodingMemoryPolicy

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Policy for gating auxiliary-model speculative decoding by resident memory estimates.

## Declaration

```swift
struct SpeculativeDecodingMemoryPolicy
```

## Topics

### Initializers
- [init(limitBytes: Int?, additionalBytes: Int, action: SpeculativeDecodingMemoryAction)](./speculativedecodingmemorypolicy/init%28limitbytes,additionalbytes,action%29.md)
### Instance Properties
- [let action: SpeculativeDecodingMemoryAction](./speculativedecodingmemorypolicy/action.md)
  Action to take when the estimate exceeds the budget.
- [let additionalBytes: Int](./speculativedecodingmemorypolicy/additionalbytes.md)
  Extra bytes to reserve for KV cache, workspace, or application memory.
- [let limitBytes: Int?](./speculativedecodingmemorypolicy/limitbytes.md)
  Optional absolute budget in bytes. When nil, no budget is enforced.
### Instance Methods
- [func evaluate(mainModelBytes: Int, draftModelBytes: Int) -> SpeculativeDecodingMemoryEvaluation](./speculativedecodingmemorypolicy/evaluate%28mainmodelbytes,draftmodelbytes%29.md)
  Evaluate explicit byte estimates. This is useful before loading a draft model.
### Type Properties
- [static var recommendedWorkingSet: `Self`](./speculativedecodingmemorypolicy/recommendedworkingset.md)
  Default policy using `GPU.maxRecommendedWorkingSetBytes()` when available.
### Default Implementations
- [Equatable Implementations](./speculativedecodingmemorypolicy/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/speculativedecodingmemorypolicy)*