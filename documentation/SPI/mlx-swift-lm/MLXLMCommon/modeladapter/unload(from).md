---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modeladapter/unload(from:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# unload(from:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Unloads the adapter from the specified model.

## Declaration

```swift
func unload(from model: LanguageModel)
```

## Discussion

Prefer [`unload(adapter:)`](../languagemodel/unload%28adapter%29.md) when invoking an adapter so the model can rebuild derived inference state after the topology change.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modeladapter/unload(from:))*