---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loadmodelcontainer(from:using:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# loadModelContainer(from:using:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Load a model from a local directory of configuration and weights.

## Declaration

```swift
func loadModelContainer(from directory: URL, using tokenizerLoader: any TokenizerLoader) async throws -> sending ModelContainer
```

## Return Value

A [`ModelContainer`](./modelcontainer.md)

## Discussion

Returns a [`ModelContainer`](./modelcontainer.md) holding a [`ModelContext`](./modelcontext.md) inside an actor providing isolation control for the values.

## Parameters

- `directory`: Directory of configuration and weights
- `tokenizerLoader`: The [`TokenizerLoader`](./tokenizerloader.md) to use for loading the tokenizer


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loadmodelcontainer(from:using:))*