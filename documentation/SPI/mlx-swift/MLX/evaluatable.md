---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/evaluatable"
framework: "mlx-swift/MLX"
---

# Evaluatable

**Framework**: mlx-swift/MLX  
**Kind**: protocol  
**Role**: Protocol

An object that can be passed to [`eval(_:)`](./eval%28_%29-45gpq.md) and can produce a list of interior [`MLXArray`](./mlxarray.md) to be evaluated.

## Declaration

```swift
protocol Evaluatable
```

## Overview

Types such as:

- [`MLXArray`](./mlxarray.md)
- `MLXRandom.state`
- `MLXNN.Module`
- `MLXOptimizers.Optimizer`

Are all evaluatable.

## Topics

### Instance Methods
- [func innerState() -> [MLXArray]](./evaluatable/innerstate%28%29.md)

## Relationships

### Conforming Types
- [Array](./swift/array.md)
- [MLXArray](./mlxarray.md)
- [MLXRandom.RandomState](./mlxrandom/randomstate.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/evaluatable)*