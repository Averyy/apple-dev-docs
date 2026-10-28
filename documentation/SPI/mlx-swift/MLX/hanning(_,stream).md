---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/hanning(_:stream:)"
framework: "mlx-swift/MLX"
---

# hanning(_:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Return the Hanning window.

## Declaration

```swift
func hanning(_ m: Int, stream: StreamOrDevice = .default) -> MLXArray
```

## Return Value

The window, with the maximum value normalized to one (the value one appears only if the number of samples is odd).

## Discussion

The Hanning window is a taper formed by using a weighted cosine.

## Parameters

- `m`: Number of points in the output window
- `stream`: Stream to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/hanning(_:stream:))*