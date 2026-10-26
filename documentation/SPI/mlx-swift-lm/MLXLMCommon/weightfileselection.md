---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/weightfileselection"
framework: "mlx-swift-lm/MLXLMCommon"
---

# WeightFileSelection

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

How the safetensors files holding a model’s weights are chosen.

## Declaration

```swift
enum WeightFileSelection
```

## Topics

### Enumeration Cases
- [WeightFileSelection.allFilesPresent](./weightfileselection/allfilespresent.md)
  Load every safetensors file in the model directory.
- [WeightFileSelection.automatic](./weightfileselection/automatic.md)
  Use `model.safetensors.index.json` when it names files that exist, otherwise the conventional `model*.safetensors` (then `weight*.safetensors`) names.
### Default Implementations
- [Equatable Implementations](./weightfileselection/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Related Documentation
- [var weightFileSelection: WeightFileSelection](./modelconfiguration/weightfileselection.md)
  How to choose which safetensors files in the model directory hold the model’s weights.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/weightfileselection)*