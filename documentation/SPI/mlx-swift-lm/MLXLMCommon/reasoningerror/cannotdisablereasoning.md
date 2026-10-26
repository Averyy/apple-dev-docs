---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningerror/cannotdisablereasoning"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ReasoningError.cannotDisableReasoning

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: case  
**Role**: Case

The caller asked to disable reasoning on a model whose reasoning cannot be turned off (e.g. DeepSeek-R1).

## Declaration

```swift
case cannotDisableReasoning
```

#### Discussion

This is a package-internal error. The `MLXFoundationModels` layer translates it into the framework’s `LanguageModelError.unsupportedCapability` so app developers see a first-party error type.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningerror/cannotdisablereasoning)*