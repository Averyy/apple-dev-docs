---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/linspace(_:_:count:dtype:stream:)-9yqai"
framework: "mlx-swift/MLX"
---

# linspace(_:_:count:dtype:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Generate `count` evenly spaced numbers over interval `[start, stop]` for `BinaryFloatingPoint`.

## Declaration

```swift
static func linspace<T>(_ start: T, _ stop: T, count: Int = 50, dtype: DType? = nil, stream: StreamOrDevice = .default) -> MLXArray where T : HasDType, T : BinaryFloatingPoint
```

## Discussion

Example:

```swift
// Create a 50 element 1-D array with values from 0 to 1
let r = MLXArray.linspace(0.0, 1.0)
```

### See Also

- [Initialization](../initialization.md)
- [`linspace(_:_:count:dtype:stream:)`](./linspace%28_,_,count,dtype,stream%29-9yqai.md)

## Parameters

- `start`: Start value
- `stop`: Stop value
- `count`: Number of samples
- `dtype`: Dtype of the result, derived from `T` if not specified
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/linspace(_:_:count:dtype:stream:)-9yqai)*