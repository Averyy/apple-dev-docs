---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/blackman(_:stream:)"
framework: "mlx-swift/MLX"
---

# blackman(_:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Return the Blackman window.

## Declaration

```swift
func blackman(_ m: Int, stream: StreamOrDevice = .default) -> MLXArray
```

## Return Value

The window, with the maximum value normalized to one (the value one appears only if the number of samples is odd).

## Discussion

The Blackman window is a taper formed by using the first three terms of a summation of cosines.

## Parameters

- `m`: Number of points in the output window
- `stream`: Stream to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/blackman(_:stream:))*