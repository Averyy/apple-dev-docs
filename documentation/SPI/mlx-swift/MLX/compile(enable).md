---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/compile(enable:)"
framework: "mlx-swift/MLX"
---

# compile(enable:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Globally enable or disable [`compile(inputs:outputs:shapeless:_:)`](./compile%28inputs,outputs,shapeless,_%29-8wq3u.md).

## Declaration

```swift
func compile(enable: Bool = true)
```

## Discussion

Default is enabled.

## See Also

### Functions
- [func compile(inputs: [any Updatable], outputs: [any Updatable], shapeless: Bool, ([MLXArray]) -> [MLXArray]) -> ([MLXArray]) -> [MLXArray]](./compile%28inputs,outputs,shapeless,_%29-8wq3u.md)
  Returns a compiled function that produces the same output as `f()`.
- [func compile(inputs: [any Updatable], outputs: [any Updatable], shapeless: Bool, (MLXArray) -> MLXArray) -> (MLXArray) -> MLXArray](./compile%28inputs,outputs,shapeless,_%29-10e2w.md)
  Overload of [`compile(inputs:outputs:shapeless:_:)`](./compile%28inputs,outputs,shapeless,_%29-8wq3u.md) that takes a single [`MLXArray`](./mlxarray.md) and produces a single [`MLXArray`](./mlxarray.md).
- [func compile(inputs: [any Updatable], outputs: [any Updatable], shapeless: Bool, (MLXArray, MLXArray) -> MLXArray) -> (MLXArray, MLXArray) -> MLXArray](./compile%28inputs,outputs,shapeless,_%29-15bpz.md)
  Overload of [`compile(inputs:outputs:shapeless:_:)`](./compile%28inputs,outputs,shapeless,_%29-8wq3u.md) that takes two [`MLXArray`](./mlxarray.md) and produces a single [`MLXArray`](./mlxarray.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/compile(enable:))*