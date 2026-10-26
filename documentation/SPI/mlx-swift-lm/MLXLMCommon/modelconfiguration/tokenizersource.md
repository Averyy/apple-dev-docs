---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconfiguration/tokenizersource"
framework: "mlx-swift-lm/MLXLMCommon"
---

# tokenizerSource

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Where to load the tokenizer from when it differs from the model directory.

## Declaration

```swift
let tokenizerSource: TokenizerSource?
```

## Mentions

- [Model Compatibility](../model-compatibility.md)

#### Discussion

- `.id`: download from a remote provider (requires a [`Downloader`](../downloader.md))
- `.directory`: load from a local path
- `nil`: use the same directory as the model


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconfiguration/tokenizersource)*