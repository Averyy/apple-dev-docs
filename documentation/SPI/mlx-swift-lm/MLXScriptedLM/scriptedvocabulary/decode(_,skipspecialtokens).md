---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedvocabulary/decode(_:skipspecialtokens:)"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# decode(_:skipSpecialTokens:)

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: method  
**Role**: Instance Method

Concatenates token bytes. Invalid UTF-8 (a partial character) decodes to U+FFFD. Ids outside the vocabulary are ignored.

## Declaration

```swift
func decode(_ ids: [Int], skipSpecialTokens: Bool = false) -> String
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedvocabulary/decode(_:skipspecialtokens:))*