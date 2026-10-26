---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/vmap(_:inaxes:outaxes:)-124np"
framework: "mlx-swift/MLX"
---

# vmap(_:inAxes:outAxes:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Returns a vectorized version of `f()`.

## Declaration

```swift
func vmap(_ f: @escaping ([MLXArray]) -> [MLXArray], inAxes: some Sequence<Optional<Int>> = [0], outAxes: some Sequence<Optional<Int>> = [0]) -> ([MLXArray]) -> [MLXArray]
```

#### Return Value

A vectorized function

#### Discussion

The returned function applies `f()` independently over the axis specified by `inAxes` and stacks the results along `outAxes`.

##### See Also

- [Vectorization](./vmap.md)

## Parameters

- `f`: Function to vectorize
- `inAxes`: Axis of each input to map over. `nil` disables mapping for that input.
- `outAxes`: Axis of each output to stack the results along


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/vmap(_:inaxes:outaxes:)-124np)*