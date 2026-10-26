---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokenloophandler"
framework: "mlx-swift-lm/MLXLMCommon"
---

# TokenLoopHandler

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

Converts generated tokens into stream events.

## Declaration

```swift
protocol TokenLoopHandler : SendableMetatype
```

#### Overview

Handlers run on the generation worker and may own non-Sendable decoding state. Only their output crosses into the consumer’s task. The `emit` closure returns `false` when the consumer has ended the stream.

## Topics

### Associated Types
- [associatedtype Output : Sendable](./tokenloophandler/output.md)
### Instance Properties
- [var additionalStopTokenIDs: Set<Int>](./tokenloophandler/additionalstoptokenids.md)
  Semantic boundaries contributed by the response protocol handled by this consumer. Raw-token consumers intentionally contribute none.
- [var receivesStopTokens: Bool](./tokenloophandler/receivesstoptokens.md)
  Whether semantic parsing needs to observe EOS tokens even though they are not included in the public output or generation token count.
### Instance Methods
- [func infoEvent(GenerateCompletionInfo) -> Output](./tokenloophandler/infoevent%28_%29.md)
- [func onGenerationEnd(emit: (sending Output) -> Bool) -> TokenLoopDisposition](./tokenloophandler/ongenerationend%28emit%29.md)
  Called after the token loop finishes, before the info event.
- [func onStopToken(Int, logProbabilities: DeferredTokenLogProbabilities?, emit: (sending Output) -> Bool) -> TokenLoopDisposition](./tokenloophandler/onstoptoken%28_,logprobabilities,emit%29.md)
  Called when `includeStopToken` is true or [`receivesStopTokens`](./tokenloophandler/receivesstoptokens.md) is true and a stop token was hit.
- [func onToken(Int, logProbabilities: DeferredTokenLogProbabilities?, emit: (sending Output) -> Bool) -> TokenLoopDisposition](./tokenloophandler/ontoken%28_,logprobabilities,emit%29.md)
  Return `.stop` for semantic generation stops, or `.cancelled` for consumer termination.

## Relationships

### Inherits From
- Swift.SendableMetatype
### Conforming Types
- [LogProbabilityTokenLoopHandler](./logprobabilitytokenloophandler.md)
- [RawTokenLoopHandler](./rawtokenloophandler.md)
- [TextToolTokenLoopHandler](./texttooltokenloophandler.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokenloophandler)*