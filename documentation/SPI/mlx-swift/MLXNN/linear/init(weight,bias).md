---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/linear/init(weight:bias:)"
framework: "mlx-swift/MLXNN"
---

# init(weight:bias:)

**Framework**: mlx-swift/MLXNN  
**Kind**: init  
**Role**: Initializer

Initializer meant for subclasses to provide weight and bias arrays directly.

## Declaration

```swift
init(weight: MLXArray, bias: MLXArray? = nil)
```

#### Discussion

This is used e.g. by [`QuantizedLinear`](../quantizedlinear.md) to provide quantized weights and biases rather than have [`Linear`](../linear.md) compute them.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/linear/init(weight:bias:))*