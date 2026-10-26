---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconfiguration/weightfileselection"
framework: "mlx-swift-lm/MLXLMCommon"
---

# weightFileSelection

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

How to choose which safetensors files in the model directory hold the model’s weights.

## Declaration

```swift
var weightFileSelection: WeightFileSelection
```

#### Discussion

The default, [`WeightFileSelection.automatic`](../weightfileselection/automatic.md), handles a well-packaged checkpoint and the common packaging mistakes. Set [`WeightFileSelection.allFilesPresent`](../weightfileselection/allfilespresent.md) for a checkpoint whose index is known to omit weights the model needs – see the caveats on that case before reaching for it.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconfiguration/weightfileselection)*