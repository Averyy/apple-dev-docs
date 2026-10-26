---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/pooling"
framework: "mlx-swift-lm/MLXEmbedders"
---

# Pooling

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: class  
**Role**: Class

A module that performs pooling operations on hidden states to produce fixed-sized sentence embeddings.

## Declaration

```swift
class Pooling
```

#### Overview

`Pooling` takes the sequence of hidden states from a transformer model and collapses them into a single vector using strategies like mean, max, or token selection.

## Topics

### Initializers
- [init(config: PoolingConfiguration)](./pooling/init%28config%29.md)
  Initializes a `Pooling` module from a `PoolingConfiguration`.
- [init(strategy: Strategy, dimension: Int?)](./pooling/init%28strategy,dimension%29.md)
  Initializes a `Pooling` module with a specific strategy.
### Instance Properties
- [var dimension: Int?](./pooling/dimension.md)
  Optional dimension to truncate the resulting embedding to.
- [var strategy: Strategy](./pooling/strategy-swift.property.md)
  The active strategy used for pooling hidden states.
### Instance Methods
- [func callAsFunction(EmbeddingModelOutput, mask: MLXArray?, normalize: Bool, applyLayerNorm: Bool) -> MLXArray](./pooling/callasfunction%28_,mask,normalize,applylayernorm%29.md)
  Processes the input hidden states according to the configured strategy.
### Enumerations
- [Pooling.Strategy](./pooling/strategy-swift.enum.md)
  Supported pooling strategies.

## Relationships

### Inherits From
- MLXNN.Module
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- Swift.CustomStringConvertible


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/pooling)*