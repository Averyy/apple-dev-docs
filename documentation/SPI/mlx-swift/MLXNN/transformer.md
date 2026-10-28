---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/transformer"
framework: "mlx-swift/MLXNN"
---

# Transformer

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

Implements a standard Transformer model.

## Declaration

```swift
class Transformer
```

## Overview

The implementation is based on “Attention Is All You Need” [https://arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762).

The Transformer model contains an encoder and a decoder. The encoder processes the input sequence and the decoder generates the output sequence. The interaction between encoder and decoder happens through the attention mechanism.

### See Also

- [Transformer](./transformers.md)
- [https://arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762)

## Topics

### Initializers
- [init(dimensions: Int, numHeads: Int, encoderLayerCount: Int, decoderLayerCount: Int, mlpDimensions: Int?, dropout: Float, activation: any UnaryLayer, normFirst: Bool)](./transformer/init%28dimensions,numheads,encoderlayercount,decoderlayercount,mlpdimensions,dropout,activation,normfirst%29.md)
  Initialize the transformer.
### Instance Methods
- [func callAsFunction(source: MLXArray, target: MLXArray, sourceMask: MLXArray, targetMask: MLXArray, memoryMask: MLXArray) -> MLXArray](./transformer/callasfunction%28source,target,sourcemask,targetmask,memorymask%29.md)

## Relationships

### Inherits From
- [Module](./module.md)
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- Swift.CustomStringConvertible

## See Also

### Transformer Layers
- [class MultiHeadAttention](./multiheadattention.md)
  Implements the scaled dot product attention with multiple heads.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/transformer)*