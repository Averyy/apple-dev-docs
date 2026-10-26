---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/weightfileselection/allfilespresent"
framework: "mlx-swift-lm/MLXLMCommon"
---

# WeightFileSelection.allFilesPresent

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: case  
**Role**: Case

Load every safetensors file in the model directory.

## Declaration

```swift
case allFilesPresent
```

#### Discussion

This is an escape hatch for a checkpoint whose index is known to be wrong in a way [`WeightFileSelection.automatic`](./automatic.md) cannot detect – an index that names files that all exist but omits weights the model needs. It loads files that may not belong to this model, and a stray tensor whose name collides with one the model’s `sanitize(weights:)` rewrites is loaded silently rather than reported, so prefer a model that declares its own extra files (see [`AdditionalWeightFilesProviding`](../additionalweightfilesproviding.md)) where that is possible.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/weightfileselection/allfilespresent)*