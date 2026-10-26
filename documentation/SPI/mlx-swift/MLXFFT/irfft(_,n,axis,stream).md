---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxfft/irfft(_:n:axis:stream:)"
framework: "mlx-swift/MLXFFT"
---

# irfft(_:n:axis:stream:)

**Framework**: mlx-swift/MLXFFT  
**Kind**: func  
**Role**: Function

Inverse one dimensional discrete Fourier Transform on a real input.

## Declaration

```swift
func irfft(_ array: MLXArray, n: Int? = nil, axis: Int = -1, stream: StreamOrDevice = .default) -> MLXArray
```

#### Return Value

Inverse of [`rfft(_:n:axis:stream:)`](./rfft%28_,n,axis,stream%29.md)

#### Discussion

The output has the same shape as the input except along `axis` in which case it has size `n`.

##### See Also

- [MLXFFT](./MLXFFT.md)

## Parameters

- `array`: Input array.  If the array is complex it will be silently cast to a real type
- `n`: Size of the transformed axis.  The corresponding axis in the input is truncated or padded with zeros to match `n / 2 + 1`.  If not specified `array.dim(axis) / 2 + 1` will be used.
- `axis`: Axis along which to perform the FFT
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxfft/irfft(_:n:axis:stream:))*