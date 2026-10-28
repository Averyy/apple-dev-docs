---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/ones(like:dtype:stream:)"
framework: "mlx-swift/MLX"
---

# ones(like:dtype:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Construct an array of ones.

## Declaration

```swift
static func ones(like array: MLXArray, dtype: DType? = nil, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](../converting-python.md)

## Discussion

Example:

```swift
let array = MLXArray(0 ..< 12, [4, 3])
let r = MLXArray.ones(like: array)
```

### See Also

- [Initialization](../initialization.md)
- [`ones(_:type:stream:)`](./ones%28_,type,stream%29.md)
- [`zeros(_:type:stream:)`](./zeros%28_,type,stream%29.md)

## Parameters

- `array`: Array to copy shape and dtype from
- `dtype`: Optional type to produce the result in, otherwise use array’s dtype
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/ones(like:dtype:stream:))*