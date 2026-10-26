---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modeladapter/fuse(with:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# fuse(with:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Permanently fuses the adapter into the specified model.

## Declaration

```swift
func fuse(with model: LanguageModel) throws
```

#### Discussion

Prefer [`fuse(with:)`](../languagemodel/fuse%28with%29.md) when invoking an adapter so the model can rebuild derived inference state after the topology change.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modeladapter/fuse(with:))*