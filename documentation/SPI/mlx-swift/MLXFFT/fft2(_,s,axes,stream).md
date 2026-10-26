---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxfft/fft2(_:s:axes:stream:)"
framework: "mlx-swift/MLXFFT"
---

# fft2(_:s:axes:stream:)

**Framework**: mlx-swift/MLXFFT  
**Kind**: func  
**Role**: Function

Two dimensional discrete Fourier Transform.

> **Deprecated**: fft2 is now available in the main MLX module.

## Declaration

```swift
func fft2(_ array: MLXArray, s: [Int]? = nil, axes: [Int]? = [-2, -1], stream: StreamOrDevice = .default) -> MLXArray
```

#### Return Value

DFT of the input along the given axes

##### See Also

- [MLXFFT](./MLXFFT.md)

## Parameters

- `array`: Input array
- `s`: Sizes of the transformed axis.  The corresponding axes in the input are truncated or padded with zeros to match `s`.  If not specified `array.dim(axis)` will be used.
- `axes`: Axes along which to perform the FFT
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxfft/fft2(_:s:axes:stream:))*