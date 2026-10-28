---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/llmmodel/messagegenerator(tokenizer:)"
framework: "mlx-swift-lm/MLXLLM"
---

# messageGenerator(tokenizer:)

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Models can implement this is they need a custom `MessageGenerator`.

## Declaration

```swift
func messageGenerator(tokenizer: Tokenizer) -> MessageGenerator
```

## Discussion

The default implementation returns `DefaultMessageGenerator`.

## Default Implementations

### LLMModel Implementations
- [func messageGenerator(tokenizer: Tokenizer) -> MessageGenerator](./messagegenerator%28tokenizer%29-8eiyq.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/llmmodel/messagegenerator(tokenizer:))*