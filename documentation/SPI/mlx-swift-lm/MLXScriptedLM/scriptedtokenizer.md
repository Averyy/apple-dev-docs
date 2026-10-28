---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedtokenizer"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# ScriptedTokenizer

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: struct  
**Role**: Structure

A deterministic `Tokenizer` for scripted tests.

## Declaration

```swift
struct ScriptedTokenizer
```

## Overview

Encoding is longest-match over a [`ScriptedVocabulary`](./scriptedvocabulary.md), with atomic specials matched first. `decode(encode(s)) == s` for every string, so text survives the decode and re-encode that `ChatSession` performs on each turn.

## Topics

### Initializers
- [init(corpus: [String], template: any ScriptedChatTemplate, specials: [String], textMarkers: [String], configuration: VocabularyBuilder.Configuration, eos: EndOfSequence, bosToken: String?)](./scriptedtokenizer/init%28corpus,template,specials,textmarkers,configuration,eos,bostoken%29.md)
  Builds the vocabulary from `corpus` plus everything the template declares.
- [init(transcript: Transcript, template: any ScriptedChatTemplate, specials: [String], textMarkers: [String], configuration: VocabularyBuilder.Configuration)](./scriptedtokenizer/init%28transcript,template,specials,textmarkers,configuration%29.md)
  Builds a tokenizer whose vocabulary covers the transcript’s text.
- [init(vocabulary: ScriptedVocabulary, template: any ScriptedChatTemplate, eos: EndOfSequence, bosToken: String?)](./scriptedtokenizer/init%28vocabulary,template,eos,bostoken%29.md)
  Uses a prebuilt vocabulary, which must hold the template’s special tokens.
### Instance Properties
- [let bosToken: String?](./scriptedtokenizer/bostoken.md)
- [let eosToken: String?](./scriptedtokenizer/eostoken.md)
- [let template: any ScriptedChatTemplate](./scriptedtokenizer/template.md)
- [var unknownToken: String?](./scriptedtokenizer/unknowntoken.md)
  Byte fallback encodes everything, so there is no unknown token.
- [let vocabulary: ScriptedVocabulary](./scriptedtokenizer/vocabulary.md)
### Instance Methods
- [func applyChatTemplate(messages: [[String : any Sendable]], tools: [[String : any Sendable]]?, additionalContext: [String : any Sendable]?) throws -> [Int]](./scriptedtokenizer/applychattemplate%28messages,tools,additionalcontext%29.md)
- [func convertIdToToken(Int) -> String?](./scriptedtokenizer/convertidtotoken%28_%29.md)
- [func convertTokenToId(String) -> Int?](./scriptedtokenizer/converttokentoid%28_%29.md)
- [func decode(tokenIds: [Int], skipSpecialTokens: Bool) -> String](./scriptedtokenizer/decode%28tokenids,skipspecialtokens%29.md)
- [func encode(text: String, addSpecialTokens: Bool) -> [Int]](./scriptedtokenizer/encode%28text,addspecialtokens%29.md)
- [func render(messages: [[String : any Sendable]], tools: [[String : any Sendable]]?, additionalContext: [String : any Sendable]?) throws -> [String]](./scriptedtokenizer/render%28messages,tools,additionalcontext%29.md)
### Enumerations
- [ScriptedTokenizer.EndOfSequence](./scriptedtokenizer/endofsequence.md)
  Which token, if any, ends generation.
### Default Implementations
- [Tokenizer Implementations](./scriptedtokenizer/tokenizer-implementations.md)

## Relationships

### Conforms To
- MLXLMCommon.Tokenizer
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Tokenizers
- [struct PseudoWordTokenizer](./pseudowordtokenizer.md)
  A deterministic tokenizer for random-weight models.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedtokenizer)*