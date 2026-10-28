---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/init(_:)-1ocp6"
framework: "mlx-swift/MLX"
---

# init(_:)

**Framework**: mlx-swift/MLX  
**Kind**: init  
**Role**: Initializer

Initializer allowing creation of a multi dimensional `MLXArray` from a nested array of `HasDType` values.

## Declaration

```swift
convenience init<N>(_ value: [[N]]) where N : NestedArrayElement
```

## Discussion

The shape is inferred directly from the provided array. Note that the nesting must be rectangular (all arrays of a given level must have the same count). Failing to meet this constraint will hit a precondition failure.

```swift
// shape [2, 3]
let twoByThree = MLXArray([[1, 2, 3],
                           [4, 5, 6]])

// shape [2, 2, 2] -- any depth of nesting works
let cube = MLXArray([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
```

Note: as with the one dimensional initializers, `Int` values produce a [`DType.int32`](../dtype/int32.md) result and the precondition will fail if a value is out of bounds.  See [`init(int64:)`](./init%28int64%29-4fpsp.md) if `.int64` is required.

### See Also

- [Initialization](../initialization.md)
- [`init(int64:)`](./init%28int64%29-4fpsp.md)

## See Also

### MLXArray Int Overrides
- [convenience init(Int)](./init%28_%29-6nnka.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from an `Int` as a `Dtype.int32`.
- [convenience init([Int], (some Collection<Int>)?)](./init%28_,_%29-97hqf.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from an `[Int]` as a `Dtype.int32`.
- [convenience init(int64: Int)](./init%28int64%29-750va.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from an `Int` as a `Dtype.int64`.
- [convenience init(int64: [Int], (some Collection<Int>)?)](./init%28int64,_%29-3hkzx.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from an `[Int]` as a `Dtype.int64`.
- [convenience init(int64: some Sequence<Int>, (some Collection<Int>)?)](./init%28int64,_%29-8xap9.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from an `[Int]` as a `Dtype.int64`.
- [convenience init<N>(int64: [[N]])](./init%28int64%29-4fpsp.md)
  Initializer allowing creation of a multi dimensional `MLXArray` from a nested array of `Int` as a `DType.int64`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/init(_:)-1ocp6)*