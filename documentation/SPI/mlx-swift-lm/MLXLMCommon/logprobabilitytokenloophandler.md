---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/logprobabilitytokenloophandler"
framework: "mlx-swift-lm/MLXLMCommon"
---

# LogProbabilityTokenLoopHandler

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Adds per-token log probabilities to another handler’s output.

## Declaration

```swift
struct LogProbabilityTokenLoopHandler<Base> where Base : TokenLoopHandler
```

## Mentions

- [Observing token log probabilities](./generation-observability.md)

## Overview

Enable reporting with [`logProbabilities`](./generateparameters/logprobabilities.md) when constructing a [`TokenIterator`](./tokeniterator.md). Text chunks can span several tokens; probability events follow the token sequence, including tokens consumed by tool or reasoning parsers. This handler materializes the values, so only streams that use it copy them from the GPU.

## Topics

### Initializers
- [init(consuming Base)](./logprobabilitytokenloophandler/init%28_%29.md)
### Instance Properties
- [var additionalStopTokenIDs: Set<Int>](./logprobabilitytokenloophandler/additionalstoptokenids.md)
- [var receivesStopTokens: Bool](./logprobabilitytokenloophandler/receivesstoptokens.md)
### Instance Methods
- [func infoEvent(GenerateCompletionInfo) -> Output](./logprobabilitytokenloophandler/infoevent%28_%29.md)
- [func onGenerationEnd(emit: (sending Output) -> Bool) -> TokenLoopDisposition](./logprobabilitytokenloophandler/ongenerationend%28emit%29.md)
- [func onStopToken(Int, logProbabilities: DeferredTokenLogProbabilities?, emit: (sending Output) -> Bool) -> TokenLoopDisposition](./logprobabilitytokenloophandler/onstoptoken%28_,logprobabilities,emit%29.md)
- [func onToken(Int, logProbabilities: DeferredTokenLogProbabilities?, emit: (sending Output) -> Bool) -> TokenLoopDisposition](./logprobabilitytokenloophandler/ontoken%28_,logprobabilities,emit%29.md)
### Type Aliases
- [LogProbabilityTokenLoopHandler.Output](./logprobabilitytokenloophandler/output.md)

## Relationships

### Conforms To
- Swift.SendableMetatype
- [TokenLoopHandler](./tokenloophandler.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/logprobabilitytokenloophandler)*