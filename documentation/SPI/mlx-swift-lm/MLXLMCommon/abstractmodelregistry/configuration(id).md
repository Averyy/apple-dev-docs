---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/abstractmodelregistry/configuration(id:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# configuration(id:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Returns configuration from [`modelRegistry`](../genericmodelfactory/modelregistry.md).

## Declaration

```swift
func configuration(id: String) -> ModelConfiguration
```

## Discussion

> **Note**: If the id doesn’t exists in the configuration, this will return a new instance of it. If you want to check if the configuration in model registry, you should use [`contains(id:)`](./contains%28id%29.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/abstractmodelregistry/configuration(id:))*