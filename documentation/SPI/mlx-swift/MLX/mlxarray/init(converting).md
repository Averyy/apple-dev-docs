---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/init(converting:)"
framework: "mlx-swift/MLX"
---

# init(converting:)

**Framework**: mlx-swift/MLX  
**Kind**: init  
**Role**: Initializer

Initializer allowing creation of a multi dimensional `MLXArray` from a nested array of `Double` values.

## Declaration

```swift
convenience init<N>(converting value: [[N]]) where N : NestedArrayElement, N.Scalar == Double
```

#### Discussion

Note: this converts the values to `Float`, matching [`init(converting:_:)`](./init%28converting,_%29.md).  Unlike the one dimensional case, [`init(_:)`](./init%28_%29-1ocp6.md) also accepts `[[Double]]` and produces a [`DType.float64`](../dtype/float64.md) result.

```swift
let a = MLXArray(converting: [[0.5, 0.9], [1.5, 1.9]])
```

##### See Also

- [Initialization](../initialization.md)
- [`init(_:)`](./init%28_%29-1ocp6.md)

## See Also

### MLXArray Nested Array Initializers
- [convenience init<N>([[N]])](./init%28_%29-1ocp6.md)
  Initializer allowing creation of a multi dimensional `MLXArray` from a nested array of `HasDType` values.
- [convenience init<N>(int64: [[N]])](./init%28int64%29-4fpsp.md)
  Initializer allowing creation of a multi dimensional `MLXArray` from a nested array of `Int` as a `DType.int64`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/init(converting:))*