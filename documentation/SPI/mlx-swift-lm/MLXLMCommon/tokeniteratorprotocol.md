---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokeniteratorprotocol"
framework: "mlx-swift-lm/MLXLMCommon"
---

# TokenIteratorProtocol

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

Common properties shared by token-generating iterators.

## Declaration

```swift
protocol TokenIteratorProtocol : IteratorProtocol, Sequence where Self.Element == Int
```

## Topics

### Instance Properties
- [var evictedTokenCount: Int](./tokeniteratorprotocol/evictedtokencount.md)
- [var lastLogProbabilities: DeferredTokenLogProbabilities?](./tokeniteratorprotocol/lastlogprobabilities.md)
- [var maxTokens: Int?](./tokeniteratorprotocol/maxtokens.md)
- [var promptPrefillTime: TimeInterval](./tokeniteratorprotocol/promptprefilltime.md)
- [var reasoningTokenCount: Int?](./tokeniteratorprotocol/reasoningtokencount.md)
- [var speculativeDecodingTelemetry: SpeculativeDecodingTelemetry?](./tokeniteratorprotocol/speculativedecodingtelemetry.md)
- [var state: LMOutput.State?](./tokeniteratorprotocol/state.md)
- [var tokenCount: Int](./tokeniteratorprotocol/tokencount.md)
### Instance Methods
- [func discardGeneratedToken()](./tokeniteratorprotocol/discardgeneratedtoken%28%29.md)
- [func recordEmittedToken(Int)](./tokeniteratorprotocol/recordemittedtoken%28_%29.md)
  Records a token included in the generated completion.

## Relationships

### Inherits From
- Swift.IteratorProtocol
- Swift.Sequence
### Conforming Types
- [MTPSpeculativeTokenIterator](./mtpspeculativetokeniterator.md)
- [SpeculativeTokenIterator](./speculativetokeniterator.md)
- [TokenIterator](./tokeniterator.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokeniteratorprotocol)*