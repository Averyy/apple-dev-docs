---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedchattemplate"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# ScriptedChatTemplate

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: protocol  
**Role**: Protocol

A chat template for scripted tests.

## Declaration

```swift
protocol ScriptedChatTemplate : Sendable
```

## Overview

[`render(messages:tools:additionalContext:)`](./scriptedchattemplate/render%28messages,tools,additionalcontext%29.md) returns strings that the tokenizer encodes one at a time and concatenates. Encoding each string separately keeps a message’s tokens independent of its neighbors, which `ChatSession` prefix reuse depends on. Output is vocabulary-independent.

A template declares the tokens it needs. [`ScriptedTokenizer`](./scriptedtokenizer.md) adds them to the vocabulary, so scenario authors list only their own text.

## Topics

### Instance Properties
- [var corpus: [String]](./scriptedchattemplate/corpus.md)
  Literal text the template emits, such as role names, added to the corpus so it tokenizes into pieces rather than byte fallback.
- [var endOfTurnToken: String?](./scriptedchattemplate/endofturntoken.md)
  The token that ends an assistant turn, used as the default EOS. Must be one of [`specialTokens`](./scriptedchattemplate/specialtokens.md).
- [var specialTokens: [String]](./scriptedchattemplate/specialtokens.md)
  Markers that must be single (atomic) special tokens, such as `<|im_end|>`.
- [var textMarkers: [String]](./scriptedchattemplate/textmarkers.md)
  Markers that must encode to two or more ordinary tokens.
### Instance Methods
- [func render(messages: [[String : any Sendable]], tools: [[String : any Sendable]]?, additionalContext: [String : any Sendable]?) throws -> [String]](./scriptedchattemplate/render%28messages,tools,additionalcontext%29.md)

## Relationships

### Inherits From
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [ChatMLTemplate](./chatmltemplate.md)
- [MinimalChatTemplate](./minimalchattemplate.md)

## See Also

### Chat Templates
- [struct MinimalChatTemplate](./minimalchattemplate.md)
  A minimal one-marker-per-role template for mechanics tests. Not a real model family: prompts stay short and segment assertions stay readable.
- [struct ChatMLTemplate](./chatmltemplate.md)
  Plain ChatML, as used by the Qwen family without its tool extensions.
- [enum ScriptedTemplateMessage](./scriptedtemplatemessage.md)
  Message helpers shared by template implementations.
- [enum ScriptedTemplateError](./scriptedtemplateerror.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedchattemplate)*