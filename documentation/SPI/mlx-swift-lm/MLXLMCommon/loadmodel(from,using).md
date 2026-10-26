---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loadmodel(from:using:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# loadModel(from:using:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Load a model from a local directory of configuration and weights.

## Declaration

```swift
func loadModel(from directory: URL, using tokenizerLoader: any TokenizerLoader) async throws -> sending ModelContext
```

#### Return Value

A [`ModelContext`](./modelcontext.md)

#### Discussion

Returns a [`ModelContext`](./modelcontext.md) holding the model and tokenizer without an `actor` providing an isolation context.

## Parameters

- `directory`: Directory of configuration and weights
- `tokenizerLoader`: The [`TokenizerLoader`](./tokenizerloader.md) to use for loading the tokenizer


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loadmodel(from:using:))*