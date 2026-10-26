---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/view(dtype:stream:)"
framework: "mlx-swift/MLX"
---

# view(dtype:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

View the array as a different type.

## Declaration

```swift
func view(dtype: DType, stream: StreamOrDevice = .default) -> MLXArray
```

#### Return Value

Array with the new type

#### Discussion

The output array will change along the last axis if the input array’s type and the output array’s type do not have the same size.

Note: the view op does not imply that the input and output arrays share their underlying data. The view only gaurantees that the binary representation of each element (or group of elements) is the same.

## Parameters

- `dtype`: Type to change to
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/view(dtype:stream:))*