---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generate(input:context:iterator:didgenerate:)-pi3z"
framework: "mlx-swift-lm/MLXLMCommon"
---

# generate(input:context:iterator:didGenerate:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Low-level token generation using a [`TokenIterator`](./tokeniterator.md).

> **Deprecated**: Use the AsyncStream-based generate(input:cache:state:parameters:context:) instead for better Swift concurrency support

## Declaration

```swift
func generate(input: LMInput, context: ModelContext, iterator: TokenIterator, didGenerate: ([Int]) -> GenerateDisposition) -> GenerateResult
```

#### Return Value

The generated output

#### Discussion

[`generate(input:cache:state:parameters:context:components:wiredMemoryTicket:tools:)`](./generate%28input,cache,state,parameters,context,components,wiredmemoryticket,tools%29.md) returning `AsyncStream<Generation>` is the preferred call.

## Parameters

- `input`: Prepared language model input
- `context`: Model context (model and tokenizer)
- `iterator`: Token iterator
- `didGenerate`: Token visitor that can output tokens as they are generated and indicate early stop


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generate(input:context:iterator:didgenerate:)-pi3z)*