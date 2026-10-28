---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generatelooptask(prompttokencount:modelconfiguration:tokenizer:iterator:wiredmemoryticket:includestoptoken:handler:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# generateLoopTask(promptTokenCount:modelConfiguration:tokenizer:iterator:wiredMemoryTicket:includeStopToken:handler:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Runs a token iterator with a custom output handler.

## Declaration

```swift
func generateLoopTask<Handler>(promptTokenCount: Int, modelConfiguration: ModelConfiguration, tokenizer: Tokenizer, iterator: consuming any TokenIteratorProtocol, wiredMemoryTicket: WiredMemoryTicket? = nil, includeStopToken: Bool = false, handler: consuming Handler) -> (AsyncStream<Handler.Output>, Task<Void, Never>) where Handler : TokenLoopHandler
```

## Mentions

- [Observing token log probabilities](./generation-observability.md)

## Discussion

The task owns the iterator and handler until generation finishes. Await its value after cancelling or stopping consumption to wait for MLX cleanup.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generatelooptask(prompttokencount:modelconfiguration:tokenizer:iterator:wiredmemoryticket:includestoptoken:handler:))*