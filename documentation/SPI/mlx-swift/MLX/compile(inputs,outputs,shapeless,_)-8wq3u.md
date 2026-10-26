---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/compile(inputs:outputs:shapeless:_:)-8wq3u"
framework: "mlx-swift/MLX"
---

# compile(inputs:outputs:shapeless:_:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Returns a compiled function that produces the same output as `f()`.

## Declaration

```swift
func compile(inputs: [any Updatable] = [], outputs: [any Updatable] = [], shapeless: Bool = false, _ f: @escaping ([MLXArray]) -> [MLXArray]) -> @Sendable ([MLXArray]) -> [MLXArray]
```

#### Return Value

A new function that produces the same output as `f()`

#### Discussion

Any mutable state must be provided via the state parameter – see [Compilation](./compilation.md) for more information.

##### See Also

- [Compilation](./compilation.md)

## Parameters

- `inputs`: Input state
- `outputs`: Output state
- `shapeless`: A function compiled with the `shapeless` option enabled will not be recompiled when the input shape changes. Not all functions can be compiled with `shapeless` enabled. Attempting to compile such functions with shapeless enabled will throw. Note, changing the number of dimensions or type of any input will result in a recompilation even with `shapeless` set to `true`
- `f`: Function to compile

## See Also

### Functions
- [func compile(inputs: [any Updatable], outputs: [any Updatable], shapeless: Bool, (MLXArray) -> MLXArray) -> (MLXArray) -> MLXArray](./compile%28inputs,outputs,shapeless,_%29-10e2w.md)
  Overload of [`compile(inputs:outputs:shapeless:_:)`](./compile%28inputs,outputs,shapeless,_%29-8wq3u.md) that takes a single [`MLXArray`](./mlxarray.md) and produces a single [`MLXArray`](./mlxarray.md).
- [func compile(inputs: [any Updatable], outputs: [any Updatable], shapeless: Bool, (MLXArray, MLXArray) -> MLXArray) -> (MLXArray, MLXArray) -> MLXArray](./compile%28inputs,outputs,shapeless,_%29-15bpz.md)
  Overload of [`compile(inputs:outputs:shapeless:_:)`](./compile%28inputs,outputs,shapeless,_%29-8wq3u.md) that takes two [`MLXArray`](./mlxarray.md) and produces a single [`MLXArray`](./mlxarray.md).
- [func compile(enable: Bool)](./compile%28enable%29.md)
  Globally enable or disable [`compile(inputs:outputs:shapeless:_:)`](./compile%28inputs,outputs,shapeless,_%29-8wq3u.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/compile(inputs:outputs:shapeless:_:)-8wq3u)*