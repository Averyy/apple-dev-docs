---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcheckpoint/mapnames(_:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# mapNames(_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Rename or exclude complete module paths, including their quantization settings. A `nil` name excludes the tensor or layer. Aliases must not overwrite each other.

## Declaration

```swift
func mapNames(_ transform: (String) -> String?) throws -> ModelCheckpoint
```

## Mentions

- [Model Compatibility](../model-compatibility.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcheckpoint/mapnames(_:))*