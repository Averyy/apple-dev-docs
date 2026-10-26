---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/languagemodel/prepare(_:cache:state:windowsize:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# prepare(_:cache:state:windowSize:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

> **Deprecated**: prefill now defaults to balanced chunking; use prefill.chunking = .remainder for the legacy chunk boundaries

## Declaration

```swift
func prepare(_ input: LMInput, cache: [KVCache], state: LMOutput.State?, windowSize: Int?) throws -> PrepareResult
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/languagemodel/prepare(_:cache:state:windowsize:))*