---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxfft/rfftfreq(_:d:stream:)"
framework: "mlx-swift/MLX"
---

# rfftfreq(_:d:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

The sample frequencies of a discrete Fourier Transform on a real input.

## Declaration

```swift
static func rfftfreq(_ n: Int, d: Double = 1.0, stream: StreamOrDevice = .default) -> MLXArray
```

## Return Value

Array of non-negative sample frequencies

## Discussion

Like [`fftfreq(_:d:stream:)`](./fftfreq%28_,d,stream%29.md) but returns only the `n / 2 + 1` non-negative frequencies, matching the output of [`rfft(_:n:axis:norm:stream:)`](./rfft%28_,n,axis,norm,stream%29.md).

### See Also

- [`MLXFFT`](../mlxfft.md)
- [`fftfreq(_:d:stream:)`](./fftfreq%28_,d,stream%29.md)

## Parameters

- `n`: Window length
- `d`: Sample spacing
- `stream`: Stream or device to evaluate on


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxfft/rfftfreq(_:d:stream:))*