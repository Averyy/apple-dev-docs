---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generatetask(prompttokencount:modelconfiguration:tokenizer:iterator:wiredmemoryticket:tools:toolcallpolicy:reasoningprimedinside:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# generateTask(promptTokenCount:modelConfiguration:tokenizer:iterator:wiredMemoryTicket:tools:toolCallPolicy:reasoningPrimedInside:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Low-level token generation returning an `AsyncStream<Generation>` and a `Task`.

## Declaration

```swift
func generateTask<TOKEN>(promptTokenCount: Int, modelConfiguration: ModelConfiguration, tokenizer: Tokenizer, iterator: consuming TOKEN, wiredMemoryTicket: WiredMemoryTicket? = nil, tools: [[String : any Sendable]]? = nil, toolCallPolicy: ToolCallPolicy = .init(), reasoningPrimedInside: Bool = false) -> (AsyncStream<Generation>, Task<Void, Never>) where TOKEN : TokenIteratorProtocol
```

## Return Value

An `AsyncStream` that emits `Generation` values and a `Task`

## Discussion

Accepts any [`TokenIteratorProtocol`](./tokeniteratorprotocol.md) conformer, including [`TokenIterator`](./tokeniterator.md) and [`SpeculativeTokenIterator`](./speculativetokeniterator.md). Swift infers the concrete type at the call site.

> ❗ **Important**: If the stream is terminated early (e.g. break from the loop) computation will continue using the model, parameters, KVCache, etc. for some time (typically a few ms).  Callers can await the `task` to observe when the use of the parameters is complete.

## Parameters

- `promptTokenCount`: Number of tokens in the prompt
- `modelConfiguration`: Model configuration (for EOS/extra EOS tokens and tool-call format)
- `tokenizer`: Tokenizer (for EOS id, unknown token id, and detokenization)
- `iterator`: A token iterator conforming to [`TokenIteratorProtocol`](./tokeniteratorprotocol.md)
- `wiredMemoryTicket`: Optional wired memory ticket for policy-based coordination.
- `tools`: Optional tool schemas used to parse tool-call arguments into their declared types.
- `toolCallPolicy`: Recovery and validation rules for generated tool calls.
- `reasoningPrimedInside`: Whether the rendered prompt ends inside an open reasoning block, which some families prefill (e.g. DeepSeek-R1’s trailing `<think>`). Callers holding the prompt should pass [`promptEndsInsideReasoning(promptTokens:config:tokenizer:)`](./reasoningeventemitter/promptendsinsidereasoning%28prompttokens,config,tokenizer%29.md); leaving it `false` would misroute a primed model’s whole thought block into `.chunk`. Check the whole rendered prompt, not only the part a prompt cache left to prefill.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generatetask(prompttokencount:modelconfiguration:tokenizer:iterator:wiredmemoryticket:tools:toolcallpolicy:reasoningprimedinside:))*