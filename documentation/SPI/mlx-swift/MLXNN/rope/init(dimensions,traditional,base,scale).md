---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/rope/init(dimensions:traditional:base:scale:)"
framework: "mlx-swift/MLXNN"
---

# init(dimensions:traditional:base:scale:)

**Framework**: mlx-swift/MLXNN  
**Kind**: init  
**Role**: Initializer

Initialize [`RoPE`](../rope.md).

## Declaration

```swift
init(dimensions: Int, traditional: Bool = false, base: Float = 10_000, scale: Float = 1)
```

## Parameters

- `dimensions`: The feature dimensions to be rotated. If the input feature is larger than dims then the rest is left unchanged
- `traditional`: If `true` choose the traditional implementation which is slightly less efficient
- `base`: The base used to compute angular frequency for each dimension in the positional encodings
- `scale`: Scale used to scale the positions


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/rope/init(dimensions:traditional:base:scale:))*