---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/prefillparameters/chunking-swift.enum"
framework: "mlx-swift-lm/MLXLMCommon"
---

# PrefillParameters.Chunking

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

Strategy dividing the prompt into prefill forwards.

## Declaration

```swift
enum Chunking
```

## Topics

### Enumeration Cases
- [PrefillParameters.Chunking.balanced](./chunking-swift.enum/balanced.md)
  The fewest equal chunks that respect the step-size ceiling, so no forward is disproportionately small at large KV length (the default).
- [PrefillParameters.Chunking.remainder](./chunking-swift.enum/remainder.md)
  Legacy stride: chunks of exactly the step size. An escape hatch back to each model’s pre-[`PrefillParameters.Chunking.balanced`](./chunking-swift.enum/balanced.md) chunk boundaries and their exact outputs — on the default `LLMModel` path the remainder rides along with the `TokenIterator`’s first forward; models that reserve one position for the logits keep that shape and stride the rest.
- [PrefillParameters.Chunking.unchunked](./chunking-swift.enum/unchunked.md)
  The whole prompt in one forward — the reference computation that any chunking approximates. Attention scores are quadratic in the prompt length and the logits materialize at `[1, L, vocab]`, so this is for validation at short lengths, not production.
### Default Implementations
- [Equatable Implementations](./chunking-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/prefillparameters/chunking-swift.enum)*