---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generatecompletioninfo/prompttokencount"
framework: "mlx-swift-lm/MLXLMCommon"
---

# promptTokenCount

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

The number of prompt tokens actually prefilled during this generation.

## Declaration

```swift
let promptTokenCount: Int
```

## Discussion

When a session reuses a KV-cache prefix only the remaining suffix is fed to the model, so this counts fewer tokens than the rendered prompt. See [`cachedPromptTokenCount`](./cachedprompttokencount.md) and [`totalPromptTokenCount`](./totalprompttokencount.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generatecompletioninfo/prompttokencount)*