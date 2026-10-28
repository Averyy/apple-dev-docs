---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/baselanguagemodel/sanitize(weights:metadata:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# sanitize(weights:metadata:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Optionally preprocess the weights with access to safetensor metadata.

## Declaration

```swift
func sanitize(weights: [String : MLXArray], metadata: [String : String]) throws -> [String : MLXArray]
```

## Discussion

The default implementation forwards to [`sanitize(weights:)`](./sanitize%28weights%29.md). Models can override this to inspect metadata (e.g. check `metadata["format"] == "mlx"`) and skip or customize sanitization accordingly.

## Default Implementations

### BaseLanguageModel Implementations
- [func sanitize(weights: [String : MLXArray], metadata: [String : String]) throws -> [String : MLXArray]](./sanitize%28weights,metadata%29-9kmfx.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/baselanguagemodel/sanitize(weights:metadata:))*