---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/init(int64:_:)-8xap9"
framework: "mlx-swift/MLX"
---

# init(int64:_:)

**Framework**: mlx-swift/MLX  
**Kind**: init  
**Role**: Initializer

Initializer allowing creation of scalar (0-dimension) `MLXArray` from an `[Int]` as a `Dtype.int64`.

## Declaration

```swift
convenience init(int64 sequence: some Sequence<Int>, _ shape: (some Collection<Int>)? = [Int]?.none)
```

#### Discussion

```swift
let a = MLXArray(int64: [1, 2, 3])
```

Note [`init(int64:_:)`](./init%28int64,_%29-8xap9.md) (producing an `int32` scalar is preferred).

##### See Also

- [Initialization](../initialization.md)

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
- [convenience init<N>(int64: [[N]])](./init%28int64%29-4fpsp.md)
  Initializer allowing creation of a multi dimensional `MLXArray` from a nested array of `Int` as a `DType.int64`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/init(int64:_:)-8xap9)*