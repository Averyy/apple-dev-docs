---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxfft/irfftn(_:s:axes:stream:)"
framework: "mlx-swift/MLXFFT"
---

# irfftn(_:s:axes:stream:)

**Framework**: mlx-swift/MLXFFT  
**Kind**: func  
**Role**: Function

Inverse n-dimensional discrete Fourier Transform on a real input.

> **Deprecated**: irfftn is now available in the main MLX module.

## Declaration

```swift
func irfftn(_ array: MLXArray, s: [Int]? = nil, axes: [Int]? = nil, stream: StreamOrDevice = .default) -> MLXArray
```

#### Return Value

Inverse of [`rfftn(_:s:axes:stream:)`](./rfftn%28_,s,axes,stream%29.md)

#### Discussion

Note the input is generally complex. The dimensions of the input specified in `axes` are padded or truncated to match the sizes from `s`. The last axis in `axes` is treated as the real axis and will have size `s[s.lastIndex] / 2 + 1`.

##### See Also

- [MLXFFT](./MLXFFT.md)

## Parameters

- `array`: Input array
- `s`: Sizes of the transformed axes.  The corresponding axes in the input are truncated or padded with zeros to match the sizes from `s`.  If not specified the sizes of `axes` in the input will be used.
- `axes`: Axes along which to perform the FFT
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxfft/irfftn(_:s:axes:stream:))*