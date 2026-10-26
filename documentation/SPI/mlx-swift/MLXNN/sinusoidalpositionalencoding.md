---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/sinusoidalpositionalencoding"
framework: "mlx-swift/MLXNN"
---

# SinusoidalPositionalEncoding

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

Implements sinusoidal positional encoding.

## Declaration

```swift
class SinusoidalPositionalEncoding
```

#### Overview

For more details see the paper “Attention Is All You Need” [https://arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762).

##### See Also

- [Positional Encoding](./positional-encoding.md)

## Topics

### Initializers
- [init(dimensions: Int, minFrequency: Float, maxFrequency: Float, scale: Float?, cosineFirst: Bool, fullTurns: Bool)](./sinusoidalpositionalencoding/init%28dimensions,minfrequency,maxfrequency,scale,cosinefirst,fullturns%29.md)
  Initialize the layer.
### Instance Properties
- [let cosineFirst: Bool](./sinusoidalpositionalencoding/cosinefirst.md)
- [let scale: Float](./sinusoidalpositionalencoding/scale.md)
### Instance Methods
- [func callAsFunction(MLXArray) -> MLXArray](./sinusoidalpositionalencoding/callasfunction%28_%29.md)

## Relationships

### Inherits From
- [Module](./module.md)
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- Swift.CustomStringConvertible
- [UnaryLayer](./unarylayer.md)

## See Also

### Positional Encoding Layers
- [class RoPE](./rope.md)
  Implements the rotary positional encoding.
- [class ALiBi](./alibi.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/sinusoidalpositionalencoding)*