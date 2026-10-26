---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/rfft(_:n:axis:norm:stream:)"
framework: "mlx-swift/MLX"
---

# rfft(_:n:axis:norm:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

One dimensional discrete Fourier Transform on a real input.

## Declaration

```swift
func rfft(_ array: MLXArray, n: Int? = nil, axis: Int = -1, norm: FFTNorm = .backward, stream: StreamOrDevice = .default) -> MLXArray
```

#### Return Value

DFT of the input along the given axis.  The output data type will be complex.

#### Discussion

The output has the same shape as the input except along `axis` in which case it has size `n / 2 + 1`.

##### See Also

- [`MLXFFT`](./mlxfft.md)

## Parameters

- `array`: Input array.  If the array is complex it will be silently cast to a real type
- `n`: Size of the transformed axis.  The corresponding axis in the input is truncated or padded with zeros to match `n`.  If not specified `array.dim(axis)` will be used.
- `axis`: Axis along which to perform the FFT
- `norm`: Normalization mode
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/rfft(_:n:axis:norm:stream:))*