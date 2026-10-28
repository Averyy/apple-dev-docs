---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loracontainer/fuse(with:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# fuse(with:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Permanently fuses the adapter weights into the model’s base layers.

## Declaration

```swift
func fuse(with model: LanguageModel) throws
```

## Discussion

After fusion, adapter weights become part of the model’s original parameters, and adapter layers are no longer needed.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loracontainer/fuse(with:))*