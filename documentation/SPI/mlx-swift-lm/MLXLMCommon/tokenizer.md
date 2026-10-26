---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokenizer"
framework: "mlx-swift-lm/MLXLMCommon"
---

# Tokenizer

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

A protocol for tokenizing text into token IDs and decoding token IDs into text.

## Declaration

```swift
protocol Tokenizer : Sendable
```

## Mentions

- [Using mlx-swift-lm](./using.md)

## Topics

### Instance Properties
- [var bosToken: String?](./tokenizer/bostoken.md)
- [var eosToken: String?](./tokenizer/eostoken.md)
- [var eosTokenId: Int?](./tokenizer/eostokenid.md)
- [var unknownToken: String?](./tokenizer/unknowntoken.md)
- [var unknownTokenId: Int?](./tokenizer/unknowntokenid.md)
### Instance Methods
- [func applyChatTemplate(messages: [[String : any Sendable]]) throws -> [Int]](./tokenizer/applychattemplate%28messages%29.md)
- [func applyChatTemplate(messages: [[String : any Sendable]], tools: [[String : any Sendable]]?) throws -> [Int]](./tokenizer/applychattemplate%28messages,tools%29.md)
- [func applyChatTemplate(messages: [[String : any Sendable]], tools: [[String : any Sendable]]?, additionalContext: [String : any Sendable]?) throws -> [Int]](./tokenizer/applychattemplate%28messages,tools,additionalcontext%29.md)
- [func convertIdToToken(Int) -> String?](./tokenizer/convertidtotoken%28_%29.md)
- [func convertTokenToId(String) -> Int?](./tokenizer/converttokentoid%28_%29.md)
- [func decode(tokenIds: [Int]) -> String](./tokenizer/decode%28tokenids%29.md)
- [func decode(tokenIds: [Int], skipSpecialTokens: Bool) -> String](./tokenizer/decode%28tokenids,skipspecialtokens%29.md)
- [func encode(text: String) -> [Int]](./tokenizer/encode%28text%29.md)
- [func encode(text: String, addSpecialTokens: Bool) -> [Int]](./tokenizer/encode%28text,addspecialtokens%29.md)
- [func makeStreamingDetokenizer() -> any StreamingDetokenizer](./tokenizer/makestreamingdetokenizer%28%29.md)
  Creates independent decoding state for one generated sequence. Override to supply a tokenizer-specific incremental implementation.

## Relationships

### Inherits From
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokenizer)*