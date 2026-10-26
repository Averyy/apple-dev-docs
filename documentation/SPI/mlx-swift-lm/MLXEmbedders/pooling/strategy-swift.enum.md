---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/pooling/strategy-swift.enum"
framework: "mlx-swift-lm/MLXEmbedders"
---

# Pooling.Strategy

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: enum  
**Role**: Enumeration

Supported pooling strategies.

## Declaration

```swift
enum Strategy
```

## Topics

### Enumeration Cases
- [Pooling.Strategy.cls](./strategy-swift.enum/cls.md)
  Use the pooled output (CLS) provided by the model.
- [Pooling.Strategy.first](./strategy-swift.enum/first.md)
  Use the first token in the sequence.
- [Pooling.Strategy.last](./strategy-swift.enum/last.md)
  Use the last token in the sequence.
- [Pooling.Strategy.max](./strategy-swift.enum/max.md)
  Use the maximum value across the sequence length for each dimension.
- [Pooling.Strategy.mean](./strategy-swift.enum/mean.md)
  Average all token embeddings (weighted by mask).
- [Pooling.Strategy.none](./strategy-swift.enum/none.md)
  Return the existing pooled output or the raw hidden states.
### Default Implementations
- [Equatable Implementations](./strategy-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/pooling/strategy-swift.enum)*