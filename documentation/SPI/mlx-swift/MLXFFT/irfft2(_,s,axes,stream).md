---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxfft/irfft2(_:s:axes:stream:)"
framework: "mlx-swift/MLXFFT"
---

# irfft2(_:s:axes:stream:)

**Framework**: mlx-swift/MLXFFT  
**Kind**: func  
**Role**: Function

Inverse two dimensional discrete Fourier Transform on a real input.

> **Deprecated**: irfft2 is now available in the main MLX module.

## Declaration

```swift
func irfft2(_ array: MLXArray, s: [Int]? = nil, axes: [Int]? = [-2, -1], stream: StreamOrDevice = .default) -> MLXArray
```

## Return Value

Inverse of [`rfft2(_:s:axes:stream:)`](./rfft2%28_,s,axes,stream%29.md)

## Discussion

Note the input is generally complex. The dimensions of the input specified in `axes` are padded or truncated to match the sizes from `s`. The last axis in `axes` is treated as the real axis and will have size `s[s.lastIndex] / 2 + 1`.

### See Also

- [MLXFFT](./MLXFFT.md)

## Parameters

- `array`: Input array
- `s`: Sizes of the transformed axes.  The corresponding axes in the input are truncated or padded with zeros to match the sizes from `s`.  If not specified the sizes of `axes` in the input will be used.
- `axes`: Axes along which to perform the FFT
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxfft/irfft2(_:s:axes:stream:))*