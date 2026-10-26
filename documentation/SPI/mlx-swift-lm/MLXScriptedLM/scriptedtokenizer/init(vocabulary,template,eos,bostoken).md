---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedtokenizer/init(vocabulary:template:eos:bostoken:)"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# init(vocabulary:template:eos:bosToken:)

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: init  
**Role**: Initializer

Uses a prebuilt vocabulary, which must hold the template’s special tokens.

## Declaration

```swift
init(vocabulary: ScriptedVocabulary, template: any ScriptedChatTemplate = MinimalChatTemplate(), eos: EndOfSequence = .template, bosToken: String? = nil)
```

## Parameters

- `vocabulary`: Must hold the template’s special tokens, and the EOS and BOS tokens.
- `template`: Renders chat messages.
- `eos`: Defaults to the template’s end-of-turn token.
- `bosToken`: Added by `encode(text:addSpecialTokens: true)`. Must be an atomic special.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedtokenizer/init(vocabulary:template:eos:bostoken:))*