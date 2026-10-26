---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallrecoverypolicy/permissive"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ToolCallRecoveryPolicy.permissive

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: case  
**Role**: Case

Everything [`ToolCallRecoveryPolicy.conservative`](./conservative.md) does, plus promotion of exact markerless `declaredTool[ARGS]{...}` rehearsals in committed response text, and documented end-of-stream repair of calls whose outer closing marker is missing while their payload is structurally complete. Every promotion and repair is recorded in [`recoveryEvents`](../toolcallprocessor/recoveryevents.md) with its provenance. Markerless candidates that fail validation remain response text.

## Declaration

```swift
case permissive
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallrecoverypolicy/permissive)*