---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/init(_:_:type:)-3fuk4"
framework: "mlx-swift/MLX"
---

# init(_:_:type:)

**Framework**: mlx-swift/MLX  
**Kind**: init  
**Role**: Initializer

Initializer allowing creation of `MLXArray` from a `Data` filled with bytes of `HasDType` values with an optional shape.

## Declaration

```swift
convenience init(_ data: Data, _ shape: (some Collection<Int>)? = [Int]?.none, type: (some HasDType).Type)
```

## Discussion

```swift
let data: Data
let array = MLXArray(data, [2, 3], type: Int32.self)
```

### See Also

- [Initialization](../initialization.md)

## See Also

### MLXArray Array Initializers
- [convenience init<T>([T], (some Collection<Int>)?)](./init%28_,_%29-7autl.md)
  Initializer allowing creation of `MLXArray` from an array of `HasDType` values with an optional shape.
- [class MLXArray](../mlxarray.md)
  An N dimensional array.  The main type in `mlx`.
- [convenience init([Int], (some Collection<Int>)?)](./init%28_,_%29-97hqf.md)
  Initializer allowing creation of scalar (0-dimension) `MLXArray` from an `[Int]` as a `Dtype.int32`.
- [convenience init(converting: [Double], (some Collection<Int>)?)](./init%28converting,_%29.md)
  Initializer allowing creation of `MLXArray` from an array of `Double` values with an optional shape.
- [convenience init(UnsafeRawBufferPointer, (some Collection<Int>)?, type: (some HasDType).Type)](./init%28_,_,type%29-7ktbj.md)
  Initializer allowing creation of `MLXArray` from a `UnsafeRawBufferPointer` filled with bytes of `HasDType` values with an optional shape.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/init(_:_:type:)-3fuk4)*