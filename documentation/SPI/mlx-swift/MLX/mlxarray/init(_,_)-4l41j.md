---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/init(_:_:)-4l41j"
framework: "mlx-swift/MLX"
---

# init(_:_:)

**Framework**: mlx-swift/MLX  
**Kind**: init  
**Role**: Initializer

Initializer allowing creation of `MLXArray` from a sequence of `HasDType` values with an optional shape.

## Declaration

```swift
convenience init<S>(_ sequence: S, _ shape: (some Collection<Int>)? = [Int]?.none) where S : Sequence, S.Element : HasDType
```

#### Discussion

```swift
let ramp = MLXArray(0 ..< 64)
let square = MLXArray(0 ..< 64, [8, 8])
```

Note: if the element type is `Int` this will produce an [`DType.int32`](../dtype/int32.md) result. See [`init(int64:_:)`](./init%28int64,_%29-8xap9.md) if an `.int64` is required.

##### See Also

- [Initialization](../initialization.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/init(_:_:)-4l41j)*