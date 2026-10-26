---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/thinkingbudgeterror"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ThinkingBudgetError

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

Errors raised while configuring a reasoning-token budget.

## Declaration

```swift
enum ThinkingBudgetError
```

## Topics

### Enumeration Cases
- [ThinkingBudgetError.generationTokenRequirementOverflow](./thinkingbudgeterror/generationtokenrequirementoverflow.md)
  The configured budget and reserves cannot be represented by `Int`.
- [ThinkingBudgetError.insufficientGenerationTokenLimit(required:actual:)](./thinkingbudgeterror/insufficientgenerationtokenlimit%28required,actual%29.md)
  `maxTokens` cannot contain the budget, protocol headroom and answer reserve.
- [ThinkingBudgetError.invalidMaximumTokenCount(_:)](./thinkingbudgeterror/invalidmaximumtokencount%28_%29.md)
  A token budget cannot be negative. Zero means close reasoning immediately.
- [ThinkingBudgetError.invalidMinimumAnswerTokenCount(_:)](./thinkingbudgeterror/invalidminimumanswertokencount%28_%29.md)
  The answer reserve cannot be negative.
- [ThinkingBudgetError.invalidTokenID(_:)](./thinkingbudgeterror/invalidtokenid%28_%29.md)
  The tokenizer produced an ID that cannot be represented by MLX token tensors.
- [ThinkingBudgetError.unencodableBoundary(_:)](./thinkingbudgeterror/unencodableboundary%28_%29.md)
  A protocol boundary could not be represented by the tokenizer.
- [ThinkingBudgetError.unencodableTransition(_:)](./thinkingbudgeterror/unencodabletransition%28_%29.md)
  The tokenizer could not represent the model’s forced transition.
- [ThinkingBudgetError.unsupportedReasoningProtocol](./thinkingbudgeterror/unsupportedreasoningprotocol.md)
  The model declares reasoning, but neither it nor the caller supplied a safe budget transition.
### Instance Properties
- [var errorDescription: String?](./thinkingbudgeterror/errordescription.md)
### Default Implementations
- [Equatable Implementations](./thinkingbudgeterror/equatable-implementations.md)
- [Error Implementations](./thinkingbudgeterror/error-implementations.md)
- [LocalizedError Implementations](./thinkingbudgeterror/localizederror-implementations.md)

## Relationships

### Conforms To
- Foundation.LocalizedError
- Swift.Equatable
- Swift.Error
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/thinkingbudgeterror)*