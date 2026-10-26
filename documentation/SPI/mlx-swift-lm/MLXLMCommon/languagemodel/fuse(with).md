---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/languagemodel/fuse(with:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# fuse(with:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Fuses an adapter permanently into the model.

## Declaration

```swift
func fuse(with adapter: ModelAdapter) throws
```

#### Discussion

Example:

```swift
let model: any LanguageModel = ...
let adapter: any ModelAdapter = ...
try model.fuse(with: adapter)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/languagemodel/fuse(with:))*