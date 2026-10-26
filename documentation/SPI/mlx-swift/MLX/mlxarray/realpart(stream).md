---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/realpart(stream:)"
framework: "mlx-swift/MLX"
---

# realPart(stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Extract the real part of a [`DType.complex64`](../dtype/complex64.md) array.

## Declaration

```swift
func realPart(stream: StreamOrDevice = .default) -> MLXArray
```

##### See Also

- [Conversion](../conversion.md)

## See Also

### Conversion Functions
- [class MLXArray](../mlxarray.md)
  An N dimensional array.  The main type in `mlx`.
- [func asType(DType, stream: StreamOrDevice) -> MLXArray](./astype%28_,stream%29-6d44y.md)
  Create a new `MLXArray` with the contents converted to the given [`DType`](../dtype.md).
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


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/realpart(stream:))*