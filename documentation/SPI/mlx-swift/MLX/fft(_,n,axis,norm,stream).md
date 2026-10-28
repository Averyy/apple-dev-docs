---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/fft(_:n:axis:norm:stream:)"
framework: "mlx-swift/MLX"
---

# fft(_:n:axis:norm:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

One dimensional discrete Fourier Transform.

## Declaration

```swift
func fft(_ array: MLXArray, n: Int? = nil, axis: Int = -1, norm: FFTNorm = .backward, stream: StreamOrDevice = .default) -> MLXArray
```

## Return Value

DFT of the input along the given axis

### See Also

- [`MLXFFT`](./mlxfft.md)

## Parameters

- `array`: Input array
- `n`: Size of the transformed axis.  The corresponding axis in the input is truncated or padded with zeros to match `n`.  If not specified `array.dim(axis)` will be used.
- `axis`: Axis along which to perform the FFT
- `norm`: Normalization mode
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/fft(_:n:axis:norm:stream:))*