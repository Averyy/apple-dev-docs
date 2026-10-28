---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mergegenerationconfigsuppressedtokens(_:into:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# mergeGenerationConfigSuppressedTokens(_:into:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Merge `suppress_tokens` from `generation_config.json` into the model’s suppressed-token set.

## Declaration

```swift
func mergeGenerationConfigSuppressedTokens(_ generationConfig: GenerationConfigFile?, into model: any LanguageModel)
```

## Discussion

Models conforming to [`SuppressedTokensProviding`](./suppressedtokensproviding.md) receive the IDs in [`suppressedTokenIds`](./suppressedtokensproviding/suppressedtokenids.md); every other model is tracked in a weak side table, so `generation_config.json` is honored regardless of conformance. No-op when the configuration declares no suppressed tokens. Called by the model factories after the model is created.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mergegenerationconfigsuppressedtokens(_:into:))*