---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxfft/rfftn(_:s:axes:stream:)"
framework: "mlx-swift/MLXFFT"
---

# rfftn(_:s:axes:stream:)

**Framework**: mlx-swift/MLXFFT  
**Kind**: func  
**Role**: Function

n-dimensional real discrete Fourier Transform.

> **Deprecated**: rfftn is now available in the main MLX module.

## Declaration

```swift
func rfftn(_ array: MLXArray, s: [Int]? = nil, axes: [Int]? = nil, stream: StreamOrDevice = .default) -> MLXArray
```

#### Return Value

DFT of the input along the given axes.  The output data type will be complex.

#### Discussion

The output has the same shape as the input except along the dimensions in `axes` in which case it has sizes from `s`. The last axis in `axes` is treated as the real axis and will have size `s[s.lastIndex] / 2 + 1`.

##### See Also

- [MLXFFT](./MLXFFT.md)

## Parameters

- `array`: Input array
- `s`: Sizes of the transformed axis.  The corresponding axes in the input are truncated or padded with zeros to match `s`.  If not specified `array.dim(axes)` will be used.
- `axes`: Axes along which to perform the FFT
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxfft/rfftn(_:s:axes:stream:))*