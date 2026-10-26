---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/trimpromptcache(_:numtokens:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# trimPromptCache(_:numTokens:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Trim the model’s cache by the given number of tokens.

## Declaration

```swift
@discardableResult
func trimPromptCache(_ cache: [KVCache], numTokens: Int) -> Int
```

## Mentions

- [KV Cache Quantization](./kv-cache-quantization.md)

#### Discussion

This function will trim the cache if possible (in-place) and return the number of tokens that were trimmed.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/trimpromptcache(_:numtokens:))*