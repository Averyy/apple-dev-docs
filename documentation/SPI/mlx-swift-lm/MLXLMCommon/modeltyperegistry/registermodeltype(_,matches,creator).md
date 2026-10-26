---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modeltyperegistry/registermodeltype(_:matches:creator:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# registerModelType(_:matches:creator:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Add a new model to the type registry with a predicate for ambiguous `model_type` strings shared by multiple package targets.

## Declaration

```swift
func registerModelType(_ type: String, matches: @escaping (Data) -> Bool, creator: @escaping (Data) throws -> T)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modeltyperegistry/registermodeltype(_:matches:creator:))*