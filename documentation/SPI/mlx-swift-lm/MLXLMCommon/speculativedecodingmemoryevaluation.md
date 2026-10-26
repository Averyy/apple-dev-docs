---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/speculativedecodingmemoryevaluation"
framework: "mlx-swift-lm/MLXLMCommon"
---

# SpeculativeDecodingMemoryEvaluation

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Result of evaluating speculative decoding against a memory policy.

## Declaration

```swift
struct SpeculativeDecodingMemoryEvaluation
```

## Topics

### Instance Properties
- [let action: SpeculativeDecodingMemoryAction](./speculativedecodingmemoryevaluation/action.md)
  Action selected by the policy.
- [let additionalBytes: Int](./speculativedecodingmemoryevaluation/additionalbytes.md)
  Additional caller-provided budget for KV cache, workspace, or other resident data.
- [let draftModelBytes: Int](./speculativedecodingmemoryevaluation/draftmodelbytes.md)
  Estimated draft-model parameter bytes.
- [var estimatedBytes: Int](./speculativedecodingmemoryevaluation/estimatedbytes.md)
  Total estimated resident bytes for speculative decoding.
- [var isWithinBudget: Bool](./speculativedecodingmemoryevaluation/iswithinbudget.md)
  Whether speculative decoding is within the available budget.
- [let limitBytes: Int?](./speculativedecodingmemoryevaluation/limitbytes.md)
  Memory budget used for the decision. `nil` means no budget was available.
- [let mainModelBytes: Int](./speculativedecodingmemoryevaluation/mainmodelbytes.md)
  Estimated main-model parameter bytes.
- [var shouldUseSpeculativeDecoding: Bool](./speculativedecodingmemoryevaluation/shouldusespeculativedecoding.md)
  Whether speculative decoding should be used.
### Default Implementations
- [Equatable Implementations](./speculativedecodingmemoryevaluation/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/speculativedecodingmemoryevaluation)*