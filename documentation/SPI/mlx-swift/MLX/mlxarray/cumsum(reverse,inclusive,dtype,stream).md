---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/cumsum(reverse:inclusive:dtype:stream:)"
framework: "mlx-swift/MLX"
---

# cumsum(reverse:inclusive:dtype:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Return the cumulative sum of the elements over the flattened array.

## Declaration

```swift
func cumsum(reverse: Bool = false, inclusive: Bool = true, dtype: DType? = nil, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

```swift
let array = MLXArray([5, 8, 4, 9], [2, 2])

// result is [5, 13, 17, 26]
let result = array.cumsum()
```

##### See Also

- [Cumulative Operations](../cumulative.md)
- [`cumsum(axis:reverse:inclusive:dtype:stream:)`](./cumsum%28axis,reverse,inclusive,dtype,stream%29.md)
- [`cumsum(_:axis:reverse:inclusive:dtype:stream:)`](../cumsum%28_,axis,reverse,inclusive,dtype,stream%29.md)

## Parameters

- `reverse`: Reverse the reduction
- `inclusive`: Include the initial value
- `dtype`: If specified, convert the input to this type
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/cumsum(reverse:inclusive:dtype:stream:))*