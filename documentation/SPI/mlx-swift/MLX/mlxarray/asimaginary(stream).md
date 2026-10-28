---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/asimaginary(stream:)"
framework: "mlx-swift/MLX"
---

# asImaginary(stream:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Instance Method

Convert the real array into a [`DType.complex64`](../dtype/complex64.md) imaginary part.

## Declaration

```swift
func asImaginary(stream: StreamOrDevice = .default) -> MLXArray
```

## Discussion

This is equivalent to the following in python:

```python
result = 1j * array
```

### See Also

- [`init(real:imaginary:)`](./init%28real,imaginary%29.md)
- [`realPart(stream:)`](./realpart%28stream%29.md)
- [`imaginaryPart(stream:)`](./imaginarypart%28stream%29.md)
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
- [func imaginaryPart(stream: StreamOrDevice) -> MLXArray](./imaginarypart%28stream%29.md)
  Extract the imaginary part of a [`DType.complex64`](../dtype/complex64.md) array.
- [func realPart(stream: StreamOrDevice) -> MLXArray](./realpart%28stream%29.md)
  Extract the real part of a [`DType.complex64`](../dtype/complex64.md) array.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxarray/asimaginary(stream:))*