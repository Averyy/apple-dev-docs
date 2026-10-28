---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/at"
framework: "mlx-swift/MLX"
---

# at

**Framework**: mlx-swift/MLX  
**Kind**: property  
**Role**: Instance Property

Used to apply update at given indices.

## Declaration

```swift
var at: ArrayAt { get }
```

## Discussion

An assignment through indices `array[indices]` will produce a result where each index will only be updated once.  For example:

```swift
// this references each index twice
let idx = MLXArray([0, 1, 0, 1])

let a1 = MLXArray([0, 0])
a1[idx] += 1
assertEqual(a1, MLXArray([1, 1]))

// this will update 0 and 1 twice
var a2 = MLXArray([0, 0])
a2 = a2.at[idx].add(1)
assertEqual(a2, MLXArray([2, 2]))
```

This is because the assignment through `array[indices]` writes a sub-array of `array` rather than performing the operation on each resolved index.

The `at` property produces an intermediate value that can take a subscript `[]` and produce an [`ArrayAtIndices`](../arrayatindices.md) that has several methods to update values.

### See Also

- [`ArrayAt`](../arrayat.md)
- [`ArrayAtIndices`](../arrayatindices.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/at)*