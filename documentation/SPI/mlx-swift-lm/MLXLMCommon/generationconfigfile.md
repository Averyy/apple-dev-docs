---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generationconfigfile"
framework: "mlx-swift-lm/MLXLMCommon"
---

# GenerationConfigFile

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

JSON wrapper for `generation_config.json` file.

## Declaration

```swift
struct GenerationConfigFile
```

## Overview

This file can override values from `config.json`, particularly `eos_token_id`. Following mlx-lm Python behavior, if `generation_config.json` exists and contains `eos_token_id`, it takes precedence over the value in `config.json`.

It can also declare `suppress_tokens`: token IDs that must never be sampled during generation (see `SuppressTokensLogitsProcessor` in Hugging Face transformers). Model factories merge these into the model’s [`suppressedTokenIds`](./suppressedtokensproviding/suppressedtokenids.md).

## Topics

### Initializers
- [init(eosTokenIds: IntOrIntArray?, stopStrings: Set<String>, suppressTokens: IntOrIntArray?)](./generationconfigfile/init%28eostokenids,stopstrings,suppresstokens%29.md)
- [init(from: Decoder) throws](./generationconfigfile/init%28from%29.md)
### Instance Properties
- [var eosTokenIds: IntOrIntArray?](./generationconfigfile/eostokenids.md)
- [var stopStrings: Set<String>](./generationconfigfile/stopstrings.md)
- [var suppressTokens: IntOrIntArray?](./generationconfigfile/suppresstokens.md)
### Instance Methods
- [func encode(to: Encoder) throws](./generationconfigfile/encode%28to%29.md)
### Default Implementations
- [Encodable Implementations](./generationconfigfile/encodable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generationconfigfile)*