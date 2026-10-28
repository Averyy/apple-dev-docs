---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generatetokentask(prompttokencount:modelconfiguration:tokenizer:iterator:includestoptoken:wiredmemoryticket:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# generateTokenTask(promptTokenCount:modelConfiguration:tokenizer:iterator:includeStopToken:wiredMemoryTicket:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Low-level raw token generation using a `TokenIterator`, returning an `AsyncStream<TokenGeneration>` and a `Task`.

## Declaration

```swift
func generateTokenTask(promptTokenCount: Int, modelConfiguration: ModelConfiguration, tokenizer: Tokenizer, iterator: consuming TokenIterator, includeStopToken: Bool = false, wiredMemoryTicket: WiredMemoryTicket? = nil) -> (AsyncStream<TokenGeneration>, Task<Void, Never>)
```

## Return Value

An `AsyncStream` that emits token IDs and a final `.info`, plus a `Task`.

## Discussion

This is useful for parsers that need access to token IDs directly, without detokenization or tool-call parsing.

## Parameters

- `promptTokenCount`: Number of tokens in the prompt
- `modelConfiguration`: Model configuration (for EOS/extra EOS tokens)
- `tokenizer`: Tokenizer (for EOS id and unknown token id)
- `iterator`: Token iterator
- `includeStopToken`: When true, the terminating EOS/unknown token is yielded before finishing
- `wiredMemoryTicket`: Optional wired memory ticket for policy-based coordination across concurrent tasks. This is opt-in and only applied on GPU devices that support wired memory control (macOS 15 / iOS 18 / tvOS 18 or newer).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generatetokentask(prompttokencount:modelconfiguration:tokenizer:iterator:includestoptoken:wiredmemoryticket:))*