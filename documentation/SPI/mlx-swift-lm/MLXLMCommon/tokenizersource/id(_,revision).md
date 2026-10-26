---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokenizersource/id(_:revision:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# TokenizerSource.id(_:revision:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: case  
**Role**: Case

A provider-specific repository identifier for downloading tokenizer files.

## Declaration

```swift
case id(String, revision: String? = nil)
```

## Parameters

- `id`: The repository identifier (e.g. `"org/tokenizer-name"`).
- `revision`: Optional revision (branch, tag, commit hash). When `nil`, the [`Downloader`](../downloader.md) decides the default (typically `"main"`).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokenizersource/id(_:revision:))*