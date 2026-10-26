---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdraftermodelfactory/load(from:using:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# load(from:using:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Load a model from a local directory, producing a [`ModelContext`](../modelcontext.md).

## Declaration

```swift
func load(from directory: URL, using tokenizerLoader: any TokenizerLoader) async throws -> sending ContextType
```

#### Discussion

No downloader is needed — the model and tokenizer are loaded from the given directory.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdraftermodelfactory/load(from:using:))*