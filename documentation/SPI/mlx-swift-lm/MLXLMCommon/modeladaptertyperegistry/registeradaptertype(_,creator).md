---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modeladaptertyperegistry/registeradaptertype(_:creator:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# registerAdapterType(_:creator:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Add a new model adapter to the type registry.

## Declaration

```swift
func registerAdapterType(_ type: String, creator: @Sendable @escaping (URL) throws -> any ModelAdapter)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modeladaptertyperegistry/registeradaptertype(_:creator:))*