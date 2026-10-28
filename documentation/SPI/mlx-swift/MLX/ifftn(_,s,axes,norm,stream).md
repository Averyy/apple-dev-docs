---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/ifftn(_:s:axes:norm:stream:)"
framework: "mlx-swift/MLX"
---

# ifftn(_:s:axes:norm:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

n-dimensional inverse discrete Fourier Transform.

## Declaration

```swift
func ifftn(_ array: MLXArray, s: (some Collection<Int>)? = [Int]?.none, axes: (some Collection<Int>)? = [Int]?.none, norm: FFTNorm = .backward, stream: StreamOrDevice = .default) -> MLXArray
```

## Return Value

Inverse DFT of the input along the given axes

### See Also

- [`MLXFFT`](./mlxfft.md)

## Parameters

- `array`: Input array
- `s`: Sizes of the transformed axis.  The corresponding axes in the input are truncated or padded with zeros to match `s`.  If not specified `array.dim(axes)` will be used.
- `axes`: Axes along which to perform the FFT
- `norm`: Normalization mode
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/ifftn(_:s:axes:norm:stream:))*