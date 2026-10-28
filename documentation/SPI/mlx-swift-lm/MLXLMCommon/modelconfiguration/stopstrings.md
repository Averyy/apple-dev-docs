---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconfiguration/stopstrings"
framework: "mlx-swift-lm/MLXLMCommon"
---

# stopStrings

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Text sequences that stop decoded generation when encountered.

## Declaration

```swift
var stopStrings: Set<String>?
```

## Discussion

If this is `nil`, decoded stop strings fall back to [`extraEOSTokens`](./extraeostokens.md). Set this explicitly, including to an empty set, to override that fallback.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconfiguration/stopstrings)*