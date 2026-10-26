---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/multioptimizer/init(optimizers:filters:)"
framework: "mlx-swift/MLXOptimizers"
---

# init(optimizers:filters:)

**Framework**: mlx-swift/MLXOptimizers  
**Kind**: init  
**Role**: Initializer

## Declaration

```swift
init(optimizers: [any Optimizer], filters: [(String, MLXArray) -> Bool] = [])
```

## Parameters

- `optimizers`: The optimizers to delegate to (at least one)
- `filters`: Predicates selecting which parameters route to each optimizer; there must be `optimizers.count - 1` of them (the last optimizer is the unconditioned fallback)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxoptimizers/multioptimizer/init(optimizers:filters:))*