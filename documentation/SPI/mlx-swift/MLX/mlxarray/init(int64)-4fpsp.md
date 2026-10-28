---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/init(int64:)-4fpsp"
framework: "mlx-swift/MLX"
---

# init(int64:)

**Framework**: mlx-swift/MLX  
**Kind**: init  
**Role**: Initializer

Initializer allowing creation of a multi dimensional `MLXArray` from a nested array of `Int` as a `DType.int64`.

## Declaration

```swift
convenience init<N>(int64 value: [[N]]) where N : NestedArrayElement, N.Scalar == Int
```

## Discussion

```swift
let a = MLXArray(int64: [[1, 2, 3], [4, 5, 6]])
```

Note [`init(_:)`](./init%28_%29-1ocp6.md) (producing an `int32` result) is preferred.

### See Also

- [Initialization](../initialization.md)
- [`init(_:)`](./init%28_%29-1ocp6.md)

## See Also

### MLXArray Int Overrides
- [convenience init(Int)](./init%28_%29-6nnka.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from an `Int` as a `Dtype.int32`.
- [convenience init([Int], (some Collection<Int>)?)](./init%28_,_%29-97hqf.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from an `[Int]` as a `Dtype.int32`.
- [convenience init<N>([[N]])](./init%28_%29-1ocp6.md)
  Initializer allowing creation of a multi dimensional `MLXArray` from a nested array of `HasDType` values.
- [convenience init(int64: Int)](./init%28int64%29-750va.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from an `Int` as a `Dtype.int64`.
- [convenience init(int64: [Int], (some Collection<Int>)?)](./init%28int64,_%29-3hkzx.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from an `[Int]` as a `Dtype.int64`.
- [convenience init(int64: some Sequence<Int>, (some Collection<Int>)?)](./init%28int64,_%29-8xap9.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from an `[Int]` as a `Dtype.int64`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/init(int64:)-4fpsp)*