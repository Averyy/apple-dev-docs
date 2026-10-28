---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxfft/fft(_:n:axis:stream:)"
framework: "mlx-swift/MLXFFT"
---

# fft(_:n:axis:stream:)

**Framework**: mlx-swift/MLXFFT  
**Kind**: func  
**Role**: Function

One dimensional discrete Fourier Transform.

> **Deprecated**: fft is now available in the main MLX module.

## Declaration

```swift
func fft(_ array: MLXArray, n: Int? = nil, axis: Int = -1, stream: StreamOrDevice = .default) -> MLXArray
```

## Return Value

DFT of the input along the given axis

### See Also

- [MLXFFT](./MLXFFT.md)

## Parameters

- `array`: Input array
- `n`: Size of the transformed axis.  The corresponding axis in the input is truncated or padded with zeros to match `n`.  If not specified `array.dim(axis)` will be used.
- `axis`: Axis along which to perform the FFT
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxfft/fft(_:n:axis:stream:))*