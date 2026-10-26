---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedtokenizer/endofsequence"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# ScriptedTokenizer.EndOfSequence

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: enum  
**Role**: Enumeration

Which token, if any, ends generation.

## Declaration

```swift
enum EndOfSequence
```

## Topics

### Enumeration Cases
- [ScriptedTokenizer.EndOfSequence.none](./endofsequence/none.md)
  No EOS: generation runs until `maxTokens`.
- [ScriptedTokenizer.EndOfSequence.template](./endofsequence/template.md)
  The template’s end-of-turn token.
- [ScriptedTokenizer.EndOfSequence.token(_:)](./endofsequence/token%28_%29.md)
  A specific atomic special.
### Default Implementations
- [Equatable Implementations](./endofsequence/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedtokenizer/endofsequence)*