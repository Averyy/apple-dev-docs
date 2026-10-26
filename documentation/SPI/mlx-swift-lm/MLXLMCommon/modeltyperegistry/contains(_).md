---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modeltyperegistry/contains(_:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# contains(_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Whether a creator is registered for `modelType` — i.e. this registry can instantiate that architecture. Lets a caller check support without attempting a (throwing, allocating) `createModel`, e.g. to decide before a multi-GB download whether a Hub repo’s `model_type` is runnable.

## Declaration

```swift
func contains(_ modelType: String) -> Bool
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modeltyperegistry/contains(_:))*