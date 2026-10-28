---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/compile(inputs:outputs:shapeless:_:)-36fp4"
framework: "mlx-swift/MLX"
---

# compile(inputs:outputs:shapeless:_:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Overload of [`compile(inputs:outputs:shapeless:_:)`](./compile%28inputs,outputs,shapeless,_%29-8wq3u.md) that takes three [`MLXArray`](./mlxarray.md) and produces a single [`MLXArray`](./mlxarray.md).

## Declaration

```swift
func compile(inputs: [any Updatable] = [], outputs: [any Updatable] = [], shapeless: Bool = false, _ f: @escaping @Sendable (MLXArray, MLXArray, MLXArray) -> MLXArray) -> @Sendable (MLXArray, MLXArray, MLXArray) -> MLXArray
```

### See Also

- [Compilation](./compilation.md)
- [`compile(inputs:outputs:shapeless:_:)`](./compile%28inputs,outputs,shapeless,_%29-8wq3u.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/compile(inputs:outputs:shapeless:_:)-36fp4)*