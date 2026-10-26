---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/pseudowordtokenizer"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# PseudoWordTokenizer

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: struct  
**Role**: Structure

A deterministic tokenizer for random-weight models.

## Declaration

```swift
struct PseudoWordTokenizer
```

#### Overview

Most tests should use [`ScriptedTokenizer`](./scriptedtokenizer.md). Use this one when the model’s output is arbitrary ids, as with random weights, and the text does not matter.

Every id is in `0 ..< vocabularySize`, so any id fits a tiny model’s embedding and any id the model emits decodes. Each id is a fixed pseudo-word (`ka`, `lomi`, …), and decoding joins words with spaces, so random output is readable text.

There is no EOS or unknown token: random output never stops early, and generation ends at `maxTokens`.

`encode` splits on whitespace. A vocabulary word maps to its own id, so model output re-encodes to the same ids. Any other word maps to a stable hash of itself. Not lossless, and it does not need to be.

## Topics

### Initializers
- [init(vocabularySize: Int, template: any ScriptedChatTemplate)](./pseudowordtokenizer/init%28vocabularysize,template%29.md)
### Instance Properties
- [var bosToken: String?](./pseudowordtokenizer/bostoken.md)
- [var eosToken: String?](./pseudowordtokenizer/eostoken.md)
- [let template: any ScriptedChatTemplate](./pseudowordtokenizer/template.md)
- [var unknownToken: String?](./pseudowordtokenizer/unknowntoken.md)
- [let vocabularySize: Int](./pseudowordtokenizer/vocabularysize.md)
### Instance Methods
- [func applyChatTemplate(messages: [[String : any Sendable]], tools: [[String : any Sendable]]?, additionalContext: [String : any Sendable]?) throws -> [Int]](./pseudowordtokenizer/applychattemplate%28messages,tools,additionalcontext%29.md)
- [func convertIdToToken(Int) -> String?](./pseudowordtokenizer/convertidtotoken%28_%29.md)
- [func convertTokenToId(String) -> Int?](./pseudowordtokenizer/converttokentoid%28_%29.md)
- [func decode(tokenIds: [Int], skipSpecialTokens: Bool) -> String](./pseudowordtokenizer/decode%28tokenids,skipspecialtokens%29.md)
- [func encode(text: String, addSpecialTokens: Bool) -> [Int]](./pseudowordtokenizer/encode%28text,addspecialtokens%29.md)
### Type Methods
- [static func word(Int) -> String](./pseudowordtokenizer/word%28_%29.md)
  The word for `id`: its base-10 digits as syllables, so every id is distinct.
### Default Implementations
- [Tokenizer Implementations](./pseudowordtokenizer/tokenizer-implementations.md)

## Relationships

### Conforms To
- MLXLMCommon.Tokenizer
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Tokenizers
- [struct ScriptedTokenizer](./scriptedtokenizer.md)
  A deterministic `Tokenizer` for scripted tests.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/pseudowordtokenizer)*