---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/prefillparameters/chunking-swift.enum/unchunked"
framework: "mlx-swift-lm/MLXLMCommon"
---

# PrefillParameters.Chunking.unchunked

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: case  
**Role**: Case

The whole prompt in one forward — the reference computation that any chunking approximates. Attention scores are quadratic in the prompt length and the logits materialize at `[1, L, vocab]`, so this is for validation at short lengths, not production.

## Declaration

```swift
case unchunked
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/prefillparameters/chunking-swift.enum/unchunked)*