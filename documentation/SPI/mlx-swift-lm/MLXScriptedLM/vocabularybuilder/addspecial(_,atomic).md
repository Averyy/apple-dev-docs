---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/vocabularybuilder/addspecial(_:atomic:)"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# addSpecial(_:atomic:)

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: method  
**Role**: Instance Method

Registers a marker such as `<|end|>` or `<think>`.

## Declaration

```swift
mutating func addSpecial(_ token: String, atomic: Bool = true)
```

## Discussion

Atomic markers become single special tokens: never split, and dropped by `decode(skipSpecialTokens: true)`. Non-atomic markers are ordinary text that must encode to two or more tokens, like multi-token markers in some real model families.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/vocabularybuilder/addspecial(_:atomic:))*