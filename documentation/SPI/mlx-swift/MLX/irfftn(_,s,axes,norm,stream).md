---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/irfftn(_:s:axes:norm:stream:)"
framework: "mlx-swift/MLX"
---

# irfftn(_:s:axes:norm:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

Inverse n-dimensional discrete Fourier Transform on a real input.

## Declaration

```swift
func irfftn(_ array: MLXArray, s: (some Collection<Int>)? = [Int]?.none, axes: (some Collection<Int>)? = [Int]?.none, norm: FFTNorm = .backward, stream: StreamOrDevice = .default) -> MLXArray
```

#### Return Value

Inverse of [`rfftn(_:s:axes:norm:stream:)`](./rfftn%28_,s,axes,norm,stream%29.md)

#### Discussion

Note the input is generally complex. The dimensions of the input specified in `axes` are padded or truncated to match the sizes from `s`. The last axis in `axes` is treated as the real axis and will have size `s[s.lastIndex] / 2 + 1`.

##### See Also

- [`MLXFFT`](./mlxfft.md)

## Parameters

- `array`: Input array
- `s`: Sizes of the transformed axis.  The corresponding axes in the input are truncated or padded with zeros to match `s`.  If not specified `array.dim(axes)` will be used.
- `axes`: Axes along which to perform the FFT
- `norm`: Normalization mode
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/irfftn(_:s:axes:norm:stream:))*