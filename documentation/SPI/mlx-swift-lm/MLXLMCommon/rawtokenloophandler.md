---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rawtokenloophandler"
framework: "mlx-swift-lm/MLXLMCommon"
---

# RawTokenLoopHandler

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Emits raw token IDs and completion information as [`TokenGeneration`](./tokengeneration.md) events.

## Declaration

```swift
struct RawTokenLoopHandler
```

## Mentions

- [Observing token log probabilities](./generation-observability.md)

## Topics

### Initializers
- [init(additionalStopTokenIDs: Set<Int>, receivesStopTokens: Bool)](./rawtokenloophandler/init%28additionalstoptokenids,receivesstoptokens%29.md)
### Instance Properties
- [let additionalStopTokenIDs: Set<Int>](./rawtokenloophandler/additionalstoptokenids.md)
- [let receivesStopTokens: Bool](./rawtokenloophandler/receivesstoptokens.md)
### Instance Methods
- [func infoEvent(GenerateCompletionInfo) -> TokenGeneration](./rawtokenloophandler/infoevent%28_%29.md)
- [func onGenerationEnd(emit: (sending TokenGeneration) -> Bool) -> TokenLoopDisposition](./rawtokenloophandler/ongenerationend%28emit%29.md)
- [func onStopToken(Int, logProbabilities: DeferredTokenLogProbabilities?, emit: (sending TokenGeneration) -> Bool) -> TokenLoopDisposition](./rawtokenloophandler/onstoptoken%28_,logprobabilities,emit%29.md)
- [func onToken(Int, logProbabilities: DeferredTokenLogProbabilities?, emit: (sending TokenGeneration) -> Bool) -> TokenLoopDisposition](./rawtokenloophandler/ontoken%28_,logprobabilities,emit%29.md)
### Type Aliases
- [RawTokenLoopHandler.Output](./rawtokenloophandler/output.md)

## Relationships

### Conforms To
- Swift.SendableMetatype
- [TokenLoopHandler](./tokenloophandler.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rawtokenloophandler)*