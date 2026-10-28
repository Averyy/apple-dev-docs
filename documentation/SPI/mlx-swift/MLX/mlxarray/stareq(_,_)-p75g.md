---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/*=(_:_:)-p75g"
framework: "mlx-swift/MLX"
---

# *=(_:_:)

**Framework**: mlx-swift/MLX  
**Kind**: op  
**Role**: Operator

Element-wise multiplication.

## Declaration

```swift
static func *= (lhs: inout MLXArray, rhs: MLXArray)
```

## Discussion

Multiply two arrays with [Numpy Style Broadcasting](../broadcasting.md) and store the result in the left-hand side array.

For example:

```swift
let a = MLXArray(0 ..< 12, [4, 3])
let b = MLXArray([4, 5, 6])

a *= b
```

### See Also

- [Arithmetic](../arithmetic.md)
- [`multiply(_:_:stream:)`](../multiply%28_,_,stream%29.md)
- [`matmul(_:stream:)`](./matmul%28_,stream%29.md)
- [`matmul(_:_:stream:)`](../matmul%28_,_,stream%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/*=(_:_:)-p75g)*