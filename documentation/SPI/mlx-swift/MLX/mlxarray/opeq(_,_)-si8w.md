---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/_=(_:_:)-si8w"
framework: "mlx-swift/MLX"
---

# /=(_:_:)

**Framework**: mlx-swift/MLX  
**Kind**: op  
**Role**: Operator

Element-wise division.

## Declaration

```swift
static func /= (lhs: inout MLXArray, rhs: MLXArray)
```

#### Discussion

Divide two arrays with [Numpy Style Broadcasting](../broadcasting.md) and store the result in the left-hand side array.

For example:

```swift
let a = MLXArray(0 ..< 12, [4, 3])
let b = MLXArray([4, 5, 6])

a /= b
```

##### See Also

- [Arithmetic](../arithmetic.md)
- [`divide(_:_:stream:)`](../divide%28_,_,stream%29.md)
- [`floorDivide(_:_:stream:)`](../floordivide%28_,_,stream%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/_=(_:_:)-si8w)*