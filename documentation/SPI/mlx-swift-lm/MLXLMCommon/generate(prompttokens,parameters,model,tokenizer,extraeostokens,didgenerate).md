---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generate(prompttokens:parameters:model:tokenizer:extraeostokens:didgenerate:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# generate(promptTokens:parameters:model:tokenizer:extraEOSTokens:didGenerate:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Given prompt tokens generate text using the given model and parameters.

> **Deprecated**: Use the AsyncStream-based generate(input:cache:state:parameters:context:) instead for better Swift concurrency support

## Declaration

```swift
func generate(promptTokens: [Int], parameters: GenerateParameters, model: any LanguageModel, tokenizer: Tokenizer, extraEOSTokens: Set<String>? = nil, didGenerate: ([Int]) -> GenerateDisposition) throws -> GenerateResult
```

#### Discussion

[`generate(input:cache:state:parameters:context:components:wiredMemoryTicket:tools:)`](./generate%28input,cache,state,parameters,context,components,wiredmemoryticket,tools%29.md) returning `AsyncStream<Generation>` is the preferred call.

## Parameters

- `promptTokens`: Tokenized prompt
- `parameters`: Generation parameters
- `model`: Model to evaluate
- `tokenizer`: Tokenizer to convert tokens back into strings and recognize special tokens
- `extraEOSTokens`: Any additional stop tokens
- `didGenerate`: Visitor for the tokens as they are generated


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generate(prompttokens:parameters:model:tokenizer:extraeostokens:didgenerate:))*