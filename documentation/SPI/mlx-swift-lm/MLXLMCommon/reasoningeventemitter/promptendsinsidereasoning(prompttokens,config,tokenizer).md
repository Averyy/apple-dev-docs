---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningeventemitter/promptendsinsidereasoning(prompttokens:config:tokenizer:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# promptEndsInsideReasoning(promptTokens:config:tokenizer:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Type Method

Whether a rendered prompt, given as its token ids, ends inside an open reasoning block.

## Declaration

```swift
static func promptEndsInsideReasoning(promptTokens: [Int], config: ReasoningConfig, tokenizer: any Tokenizer) -> Bool
```

## Discussion

Decodes only the prompt tail, since a prefilled delimiter is the last thing a generation prompt writes. Special tokens are kept: families whose delimiters are special tokens (Gemma 4, Qwen3) would otherwise decode to nothing.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningeventemitter/promptendsinsidereasoning(prompttokens:config:tokenizer:))*