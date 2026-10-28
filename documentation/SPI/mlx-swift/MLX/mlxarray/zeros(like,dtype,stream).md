---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/zeros(like:dtype:stream:)"
framework: "mlx-swift/MLX"
---

# zeros(like:dtype:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Construct an array of zeros.

## Declaration

```swift
static func zeros(like array: MLXArray, dtype: DType? = nil, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](../converting-python.md)

## Discussion

Example:

```swift
let array = MLXArray(0 ..< 12, [4, 3])
let z = MLXArray.zeros(like: array)
```

### See Also

- [Initialization](../initialization.md)
- [`zeros(_:type:stream:)`](./zeros%28_,type,stream%29.md)
- [`ones(_:type:stream:)`](./ones%28_,type,stream%29.md)

## Parameters

- `array`: Array to copy shape and dtype from
- `dtype`: Optional type to produce the result in, otherwise use array’s dtype
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/zeros(like:dtype:stream:))*