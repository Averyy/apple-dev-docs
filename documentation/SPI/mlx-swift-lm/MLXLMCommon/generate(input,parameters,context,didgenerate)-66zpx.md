---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generate(input:parameters:context:didgenerate:)-66zpx"
framework: "mlx-swift-lm/MLXLMCommon"
---

# generate(input:parameters:context:didGenerate:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Generate tokens from an [`LMInput`](./lminput.md) and a [`ModelContext`](./modelcontext.md).

> **Deprecated**: Use the AsyncStream-based generate(input:cache:state:parameters:context:) instead for better Swift concurrency support

## Declaration

```swift
func generate(input: LMInput, parameters: GenerateParameters, context: ModelContext, didGenerate: (Int) -> GenerateDisposition) throws -> GenerateCompletionInfo
```

## Return Value

Information about the generation

## Discussion

Prefer using [`generate(input:cache:state:parameters:context:components:wiredMemoryTicket:tools:)`](./generate%28input,cache,state,parameters,context,components,wiredmemoryticket,tools%29.md) returning `AsyncStream<Generation>` instead.

## Parameters

- `input`: Prepared language model input
- `parameters`: Parameters controlling the token generation
- `context`: Model context (model and tokenizer)
- `didGenerate`: Token visitor that can output tokens as they are generated and indicate early stop


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generate(input:parameters:context:didgenerate:)-66zpx)*