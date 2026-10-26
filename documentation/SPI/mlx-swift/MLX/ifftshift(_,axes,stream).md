---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/ifftshift(_:axes:stream:)"
framework: "mlx-swift/MLX"
---

# ifftshift(_:axes:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

The inverse of [`fftshift(_:axes:stream:)`](./fftshift%28_,axes,stream%29.md).

## Declaration

```swift
func ifftshift(_ array: MLXArray, axes: [Int]? = nil, stream: StreamOrDevice = .default) -> MLXArray
```

#### Return Value

The shifted array

#### Discussion

While identical to [`fftshift(_:axes:stream:)`](./fftshift%28_,axes,stream%29.md) for even-length axes, the behavior differs for odd-length axes.

##### See Also

- [`MLXFFT`](./mlxfft.md)

## Parameters

- `array`: Input array
- `axes`: Axes over which to shift.  If `nil`, all axes are shifted.
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/ifftshift(_:axes:stream:))*