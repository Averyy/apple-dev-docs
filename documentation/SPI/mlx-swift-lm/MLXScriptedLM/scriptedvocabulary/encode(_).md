---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedvocabulary/encode(_:)"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# encode(_:)

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: method  
**Role**: Instance Method

Longest-match encoding. Specials are matched first at every position, and a piece never extends over the start of a special. Unmatched bytes use byte fallback.

## Declaration

```swift
func encode(_ text: String) -> [Int]
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedvocabulary/encode(_:))*