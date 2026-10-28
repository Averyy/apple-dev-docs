---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/languagemodel/perform(with:perform:)-64w62"
framework: "mlx-swift-lm/MLXLMCommon"
---

# perform(with:perform:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Temporarily loads an adapter, performs an asynchronous action, then unloads the adapter.

## Declaration

```swift
func perform<R>(with adapter: ModelAdapter, perform: () async throws -> R) async throws -> R
```

## Discussion

Example:

```swift
let model: any LanguageModel = ...
let adapter: any ModelAdapter = ...
try await model.perform(with: adapter) {
    await generate(inputs: ...)
}
// Adapter is automatically unloaded after execution
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/languagemodel/perform(with:perform:)-64w62)*