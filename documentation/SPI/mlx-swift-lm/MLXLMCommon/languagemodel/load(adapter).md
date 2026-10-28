---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/languagemodel/load(adapter:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# load(adapter:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Loads an adapter into the model.

## Declaration

```swift
func load(adapter: ModelAdapter) throws
```

## Discussion

Example:

```swift
let model: any LanguageModel = ...
let adapter: any ModelAdapter = ...
try model.load(adapter: adapter)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/languagemodel/load(adapter:))*