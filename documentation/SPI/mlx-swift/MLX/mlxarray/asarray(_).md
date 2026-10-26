---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/asarray(_:)"
framework: "mlx-swift/MLX"
---

# asArray(_:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Return the contents as a single contiguous 1d `Swift.Array`.

## Declaration

```swift
func asArray<T>(_ type: T.Type) -> [T] where T : HasDType
```

## Mentions

- [Converting From Python](../converting-python.md)

#### Discussion

Note: because the number of dimensions is dynamic, this cannot produce a multi-dimensional array.

##### See Also

- [Conversion](../conversion.md)
- [`asData(access:)`](./asdata%28access%29.md)
- [`asData(noCopy:disambiguate:)`](./asdata%28nocopy,disambiguate%29.md)
- [`asMTLBuffer(device:noCopy:)`](./asmtlbuffer%28device,nocopy%29.md)

## See Also

### Conversion Functions
- [class MLXArray](../mlxarray.md)
  An N dimensional array.  The main type in `mlx`.
- [func asType(DType, stream: StreamOrDevice) -> MLXArray](./astype%28_,stream%29-6d44y.md)
  Create a new `MLXArray` with the contents converted to the given [`DType`](../dtype.md).
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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/asarray(_:))*