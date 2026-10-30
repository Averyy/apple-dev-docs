---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/texttooltokenloophandler"
framework: "mlx-swift-lm/MLXLMCommon"
---

# TextToolTokenLoopHandler

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Decodes response text and tool calls into [`Generation`](./generation.md) events.

## Declaration

```swift
struct TextToolTokenLoopHandler
```

## Mentions

- [Observing token log probabilities](./generation-observability.md)

## Topics

### Initializers
- [init(tokenizer: Tokenizer, stopStrings: Set<String>, format: ToolCallFormat, tools: [[String : any Sendable]]?, toolCallPolicy: ToolCallPolicy, reasoning: (config: ReasoningConfig, primedInside: Bool)?)](./texttooltokenloophandler/init%28tokenizer,stopstrings,format,tools,toolcallpolicy,reasoning%29.md)
### Instance Properties
- [var additionalStopTokenIDs: Set<Int>](./texttooltokenloophandler/additionalstoptokenids.md)
- [var receivesStopTokens: Bool](./texttooltokenloophandler/receivesstoptokens.md)
### Instance Methods
- [func infoEvent(GenerateCompletionInfo) -> Generation](./texttooltokenloophandler/infoevent%28_%29.md)
- [func onGenerationEnd(emit: (sending Generation) -> Bool) -> TokenLoopDisposition](./texttooltokenloophandler/ongenerationend%28emit%29.md)
- [func onStopToken(Int, logProbabilities: DeferredTokenLogProbabilities?, emit: (sending Generation) -> Bool) -> TokenLoopDisposition](./texttooltokenloophandler/onstoptoken%28_,logprobabilities,emit%29.md)
- [func onToken(Int, logProbabilities: DeferredTokenLogProbabilities?, emit: (sending Generation) -> Bool) -> TokenLoopDisposition](./texttooltokenloophandler/ontoken%28_,logprobabilities,emit%29.md)
### Type Aliases
- [TextToolTokenLoopHandler.Output](./texttooltokenloophandler/output.md)

## Relationships

### Conforms To
- Swift.SendableMetatype
- [TokenLoopHandler](./tokenloophandler.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/texttooltokenloophandler)*