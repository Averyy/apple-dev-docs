---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/thinkingbudgetdiagnostic"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ThinkingBudgetDiagnostic

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

Diagnostics emitted when a hard reasoning budget cannot remain authoritative.

## Declaration

```swift
enum ThinkingBudgetDiagnostic
```

## Topics

### Enumeration Cases
- [ThinkingBudgetDiagnostic.enforcementDisabled(expectedTokenIDs:sampledTokenID:)](./thinkingbudgetdiagnostic/enforcementdisabled%28expectedtokenids,sampledtokenid%29.md)
  Another processor or a tokenizer/model mismatch produced a token outside the constraint. Enforcement was disabled to avoid corrupting generation.
- [ThinkingBudgetDiagnostic.unicodeBoundaryCompletionFailed(sampledTokenCount:)](./thinkingbudgetdiagnostic/unicodeboundarycompletionfailed%28sampledtokencount%29.md)
  The tokenizer still produced incomplete Unicode after the maximum possible UTF-8 continuation length. Enforcement was disabled rather than injecting a protocol transition into malformed text.
### Default Implementations
- [Equatable Implementations](./thinkingbudgetdiagnostic/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/thinkingbudgetdiagnostic)*