---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/baselanguagemodel/sanitize(weights:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# sanitize(weights:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Optionally preprocess the weights and modify / remove values as needed. Errors propagate to the checkpoint loader.

## Declaration

```swift
func sanitize(weights: [String : MLXArray]) throws -> [String : MLXArray]
```

## Default Implementations

### BaseLanguageModel Implementations
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./sanitize%28weights%29-77701.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/baselanguagemodel/sanitize(weights:))*