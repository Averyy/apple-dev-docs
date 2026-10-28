---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modeladapter/load(into:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# load(into:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Loads the adapter into the specified model.

## Declaration

```swift
func load(into model: LanguageModel) throws
```

## Discussion

Prefer [`load(adapter:)`](../languagemodel/load%28adapter%29.md) when invoking an adapter so the model can rebuild derived inference state after the topology change.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modeladapter/load(into:))*