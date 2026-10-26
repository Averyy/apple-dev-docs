---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/init(arrayliteral:)"
framework: "mlx-swift/MLX"
---

# init(arrayLiteral:)

**Framework**: mlx-swift/MLX  
**Kind**: init  
**Role**: Initializer

Initializer allowing creation of 1d `MLXArray` from an array literal.

## Declaration

```swift
convenience init(arrayLiteral elements: Int32...)
```

#### Discussion

```swift
let a: MLXArray = [1, 2, 3]
```

This is convenient for methods that have `MLXArray` parameters:

```swift
print(array.take([1, 2, 3], axis: 0))
```

##### See Also

- [Initialization](../initialization.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/init(arrayliteral:))*