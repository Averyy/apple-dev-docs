---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxfft/fftshift(_:axes:stream:)"
framework: "mlx-swift/MLX"
---

# fftshift(_:axes:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Shift the zero-frequency component to the center of the spectrum.

## Declaration

```swift
static func fftshift(_ array: MLXArray, axes: [Int]? = nil, stream: StreamOrDevice = .default) -> MLXArray
```

#### Return Value

The shifted array

##### See Also

- [`MLXFFT`](../mlxfft.md)

## Parameters

- `array`: Input array
- `axes`: Axes over which to shift.  If `nil`, all axes are shifted.
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxfft/fftshift(_:axes:stream:))*