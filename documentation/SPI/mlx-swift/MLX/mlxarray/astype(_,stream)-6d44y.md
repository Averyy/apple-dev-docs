---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/astype(_:stream:)-6d44y"
framework: "mlx-swift/MLX"
---

# asType(_:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Create a new `MLXArray` with the contents converted to the given [`DType`](../dtype.md).

## Declaration

```swift
func asType(_ type: DType, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](../converting-python.md)

### See Also

- [Conversion](../conversion.md)

## Parameters

- `type`: Type to convert to
- `stream`: Stream or device to evaluate on

## See Also

### Conversion Functions
- [class MLXArray](../mlxarray.md)
  An N dimensional array.  The main type in `mlx`.
- [func asArray<T>(T.Type) -> [T]](./asarray%28_%29.md)
  Return the contents as a single contiguous 1d `Swift.Array`.
- [class MLXArray](../mlxarray.md)
  An N dimensional array.  The main type in `mlx`.
- [func asMTLBuffer(device: some MTLDevice, noCopy: Bool) -> (any MTLBuffer)?](./asmtlbuffer%28device,nocopy%29.md)
  Return the contents as a Metal buffer in the native [`dtype`](./dtype.md).
- [func asImaginary(stream: StreamOrDevice) -> MLXArray](./asimaginary%28stream%29.md)
  Convert the real array into a [`DType.complex64`](../dtype/complex64.md) imaginary part.
- [func imaginaryPart(stream: StreamOrDevice) -> MLXArray](./imaginarypart%28stream%29.md)
  Extract the imaginary part of a [`DType.complex64`](../dtype/complex64.md) array.
- [func realPart(stream: StreamOrDevice) -> MLXArray](./realpart%28stream%29.md)
  Extract the real part of a [`DType.complex64`](../dtype/complex64.md) array.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/astype(_:stream:)-6d44y)*