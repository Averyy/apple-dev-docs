---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantizedembedding"
framework: "mlx-swift/MLXNN"
---

# QuantizedEmbedding

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

The same as [`Embedding`](./embedding.md) but with a quantized weight matrix.

## Declaration

```swift
class QuantizedEmbedding
```

## Topics

### Initializers
- [convenience init(Embedding, groupSize: Int, bits: Int, mode: QuantizationMode)](./quantizedembedding/init%28_,groupsize,bits,mode%29.md)
- [convenience init(embeddingCount: Int, dimensions: Int, groupSize: Int, bits: Int, mode: QuantizationMode)](./quantizedembedding/init%28embeddingcount,dimensions,groupsize,bits,mode%29.md)
- [init(weight: MLXArray, groupSize: Int, bits: Int, mode: QuantizationMode, globalScale: MLXArray?)](./quantizedembedding/init%28weight,groupsize,bits,mode,globalscale%29.md)
- [init(weight: MLXArray, scales: MLXArray, biases: MLXArray?, groupSize: Int, bits: Int, mode: QuantizationMode, globalScale: MLXArray?)](./quantizedembedding/init%28weight,scales,biases,groupsize,bits,mode,globalscale%29.md)
  Initializer meant for subclasses to provide arrays directly.
### Instance Properties
- [let biases: MLXArray?](./quantizedembedding/biases.md)
- [let bits: Int](./quantizedembedding/bits.md)
- [var globalScale: MLXArray?](./quantizedembedding/globalscale.md)
- [let groupSize: Int](./quantizedembedding/groupsize.md)
- [let mode: QuantizationMode](./quantizedembedding/mode.md)
- [let scales: MLXArray](./quantizedembedding/scales.md)
- [var shape: (Int, Int)](./quantizedembedding/shape.md)
### Instance Methods
- [func asLinear(MLXArray) -> MLXArray](./quantizedembedding/aslinear%28_%29.md)
  Call the embedding layer as a linear layer.
- [func callAsFunction(MLXArray) -> MLXArray](./quantizedembedding/callasfunction%28_%29.md)

## Relationships

### Inherits From
- [Embedding](./embedding.md)
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- [Quantizable](./quantizable.md)
- [Quantized](./quantized.md)
- Swift.CustomStringConvertible
- [UnaryLayer](./unarylayer.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantizedembedding)*