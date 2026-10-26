---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/weightfileselection/automatic"
framework: "mlx-swift-lm/MLXLMCommon"
---

# WeightFileSelection.automatic

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: case  
**Role**: Case

Use `model.safetensors.index.json` when it names files that exist, otherwise the conventional `model*.safetensors` (then `weight*.safetensors`) names.

## Declaration

```swift
case automatic
```

#### Discussion

This is what a well-packaged checkpoint wants and it is the default.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/weightfileselection/automatic)*