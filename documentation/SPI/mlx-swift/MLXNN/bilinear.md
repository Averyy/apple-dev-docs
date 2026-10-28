---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/bilinear"
framework: "mlx-swift/MLXNN"
---

# Bilinear

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

Applies a bilinear transformation to the inputs.

## Declaration

```swift
class Bilinear
```

## Overview

Concretely:

```swift
y = x1.matmul(w.T)
y = x2.matmul(y)
y = y + b
```

where `w` has shape `[outputDimensions, inputDimensions2, inputDimensions1]` and `b` has shape `[outputDimensions]`.

The values are initialized from the uniform distribution:

```swift
scale = sqrt(1.0 / inputDimensions)
W = MLXRandom.uniform(-scale ..< scale, [outputDimensions, inputDimensions2, inputDimensions1])
b = MLXRandom.uniform(-scale ..< scale, [outputDimensions])
```

### See Also

- [Creating Modules](./custom-layers.md)
- [`Linear`](./linear.md)

## Topics

### Initializers
- [init(Int, Int, Int, bias: Bool)](./bilinear/init%28_,_,_,bias%29.md)
### Instance Properties
- [let bias: MLXArray?](./bilinear/bias.md)
- [let weight: MLXArray](./bilinear/weight.md)
### Instance Methods
- [func callAsFunction(MLXArray, MLXArray) -> MLXArray](./bilinear/callasfunction%28_,_%29.md)
- [func describeExtra(Int) -> String](./bilinear/describeextra%28_%29.md)
  Describe the `inputDimensions` and `outputDimensions`.

## Relationships

### Inherits From
- [Module](./module.md)
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- Swift.CustomStringConvertible

## See Also

### Other Layers
- [class MultiHeadAttention](./multiheadattention.md)
  Implements the scaled dot product attention with multiple heads.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/bilinear)*