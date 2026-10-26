---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/linspace(_:_:count:dtype:stream:)-3fx01"
framework: "mlx-swift/MLX"
---

# linspace(_:_:count:dtype:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Generate `count` evenly spaced numbers over interval `[start, stop]` for `BinaryInteger`.

## Declaration

```swift
static func linspace<T>(_ start: T, _ stop: T, count: Int = 50, dtype: DType? = nil, stream: StreamOrDevice = .default) -> MLXArray where T : HasDType, T : BinaryInteger
```

#### Discussion

The result is floating point (`float32` by default) even for integer bounds – see [`linspace(_:_:count:endpoint:dtype:stream:)`](../linspace%28_,_,count,endpoint,dtype,stream%29-2b6eu.md).

```swift
// [0, 0.5, 1] as float32
let r = MLXArray.linspace(0, 1, count: 3)
```

##### See Also

- [Initialization](../initialization.md)
- [`linspace(_:_:count:dtype:stream:)`](./linspace%28_,_,count,dtype,stream%29-3fx01.md)

## Parameters

- `start`: Start value
- `stop`: Stop value
- `count`: Number of samples
- `dtype`: Dtype of the result, `float32` if not specified
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/linspace(_:_:count:dtype:stream:)-3fx01)*