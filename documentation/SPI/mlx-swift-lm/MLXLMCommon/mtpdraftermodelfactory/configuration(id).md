---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdraftermodelfactory/configuration(id:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# configuration(id:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Resolve a model identifier, e.g. “mlx-community/Llama-3.2-3B-Instruct-4bit”, into a [`ModelConfiguration`](../modelconfiguration.md).

## Declaration

```swift
func configuration(id: String) -> ModelConfiguration
```

#### Discussion

This will either create a new (mostly unconfigured) [`ModelConfiguration`](../modelconfiguration.md) or return a registered instance that matches the id.

> **Note**: If the id doesn’t exists in the configuration, this will return a new instance of it. If you want to check if the configuration in model registry, you should use [`contains(id:)`](./contains%28id%29.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdraftermodelfactory/configuration(id:))*