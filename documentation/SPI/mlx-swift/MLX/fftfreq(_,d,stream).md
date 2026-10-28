---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/fftfreq(_:d:stream:)"
framework: "mlx-swift/MLX"
---

# fftfreq(_:d:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

The sample frequencies of a discrete Fourier Transform.

## Declaration

```swift
func fftfreq(_ n: Int, d: Double = 1.0, stream: StreamOrDevice = .default) -> MLXArray
```

## Return Value

Array of sample frequencies

## Discussion

Returns `n` frequencies in cycles per unit of the sample spacing `d`, ordered to match the output of [`fft(_:n:axis:norm:stream:)`](./fft%28_,n,axis,norm,stream%29.md).

### See Also

- [`MLXFFT`](./mlxfft.md)
- [`rfftfreq(_:d:stream:)`](./rfftfreq%28_,d,stream%29.md)

## Parameters

- `n`: Window length
- `d`: Sample spacing
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/fftfreq(_:d:stream:))*