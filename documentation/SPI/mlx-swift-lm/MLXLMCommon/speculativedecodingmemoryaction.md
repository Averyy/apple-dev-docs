---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/speculativedecodingmemoryaction"
framework: "mlx-swift-lm/MLXLMCommon"
---

# SpeculativeDecodingMemoryAction

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

Action to take when speculative decoding exceeds a memory budget.

## Declaration

```swift
enum SpeculativeDecodingMemoryAction
```

## Topics

### Enumeration Cases
- [SpeculativeDecodingMemoryAction.allow](./speculativedecodingmemoryaction/allow.md)
  Use speculative decoding even if the estimate exceeds the budget.
- [SpeculativeDecodingMemoryAction.fail](./speculativedecodingmemoryaction/fail.md)
  Throw an error instead of silently falling back.
- [SpeculativeDecodingMemoryAction.fallbackToDefault](./speculativedecodingmemoryaction/fallbacktodefault.md)
  Fall back to regular generation.
### Default Implementations
- [Equatable Implementations](./speculativedecodingmemoryaction/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/speculativedecodingmemoryaction)*