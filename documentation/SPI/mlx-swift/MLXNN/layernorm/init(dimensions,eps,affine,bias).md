---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/layernorm/init(dimensions:eps:affine:bias:)"
framework: "mlx-swift/MLXNN"
---

# init(dimensions:eps:affine:bias:)

**Framework**: mlx-swift/MLXNN  
**Kind**: init  
**Role**: Initializer

Applies layer normalization [1] on the inputs.

## Declaration

```swift
init(dimensions: Int, eps: Float = 1e-5, affine: Bool = true, bias: Bool = true)
```

#### Discussion

See [LayerNorm python docs](https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.LayerNorm.html) for more information.

##### References

1. [https://arxiv.org/abs/1607.06450](https://arxiv.org/abs/1607.06450)

## Parameters

- `dimensions`: Number of features in the input
- `eps`: Value added to the denominator for numerical stability
- `affine`: If `true` adds a trainable `weight`
- `bias`: If `true` adds a trainable `bias`


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/layernorm/init(dimensions:eps:affine:bias:))*