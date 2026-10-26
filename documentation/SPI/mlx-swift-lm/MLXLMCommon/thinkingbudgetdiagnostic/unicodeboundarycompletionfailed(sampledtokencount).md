---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/thinkingbudgetdiagnostic/unicodeboundarycompletionfailed(sampledtokencount:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ThinkingBudgetDiagnostic.unicodeBoundaryCompletionFailed(sampledTokenCount:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: case  
**Role**: Case

The tokenizer still produced incomplete Unicode after the maximum possible UTF-8 continuation length. Enforcement was disabled rather than injecting a protocol transition into malformed text.

## Declaration

```swift
case unicodeBoundaryCompletionFailed(sampledTokenCount: Int)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/thinkingbudgetdiagnostic/unicodeboundarycompletionfailed(sampledtokencount:))*