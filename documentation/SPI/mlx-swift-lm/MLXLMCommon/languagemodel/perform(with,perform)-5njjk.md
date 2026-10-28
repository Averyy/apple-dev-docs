---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/languagemodel/perform(with:perform:)-5njjk"
framework: "mlx-swift-lm/MLXLMCommon"
---

# perform(with:perform:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Temporarily loads an adapter, performs a synchronous action, then unloads the adapter.

## Declaration

```swift
func perform<R>(with adapter: ModelAdapter, perform: () throws -> R) throws -> R
```

## Discussion

Example:

```swift
let model: any LanguageModel = ...
let adapter: any ModelAdapter = ...
try model.perform(with: adapter) {
    generate(inputs: ...)
}
// Adapter is automatically unloaded after execution
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/languagemodel/perform(with:perform:)-5njjk)*