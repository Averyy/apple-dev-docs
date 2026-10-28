---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/compile(inputs:outputs:shapeless:_:)-10e2w"
framework: "mlx-swift/MLX"
---

# compile(inputs:outputs:shapeless:_:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Overload of [`compile(inputs:outputs:shapeless:_:)`](./compile%28inputs,outputs,shapeless,_%29-8wq3u.md) that takes a single [`MLXArray`](./mlxarray.md) and produces a single [`MLXArray`](./mlxarray.md).

## Declaration

```swift
func compile(inputs: [any Updatable] = [], outputs: [any Updatable] = [], shapeless: Bool = false, _ f: @escaping (MLXArray) -> MLXArray) -> @Sendable (MLXArray) -> MLXArray
```

### See Also

- [Compilation](./compilation.md)
- [`compile(inputs:outputs:shapeless:_:)`](./compile%28inputs,outputs,shapeless,_%29-8wq3u.md)

## See Also

### Functions
- [func compile(inputs: [any Updatable], outputs: [any Updatable], shapeless: Bool, ([MLXArray]) -> [MLXArray]) -> ([MLXArray]) -> [MLXArray]](./compile%28inputs,outputs,shapeless,_%29-8wq3u.md)
  Returns a compiled function that produces the same output as `f()`.
- [func compile(inputs: [any Updatable], outputs: [any Updatable], shapeless: Bool, (MLXArray, MLXArray) -> MLXArray) -> (MLXArray, MLXArray) -> MLXArray](./compile%28inputs,outputs,shapeless,_%29-15bpz.md)
  Overload of [`compile(inputs:outputs:shapeless:_:)`](./compile%28inputs,outputs,shapeless,_%29-8wq3u.md) that takes two [`MLXArray`](./mlxarray.md) and produces a single [`MLXArray`](./mlxarray.md).
- [func compile(enable: Bool)](./compile%28enable%29.md)
  Globally enable or disable [`compile(inputs:outputs:shapeless:_:)`](./compile%28inputs,outputs,shapeless,_%29-8wq3u.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/compile(inputs:outputs:shapeless:_:)-10e2w)*