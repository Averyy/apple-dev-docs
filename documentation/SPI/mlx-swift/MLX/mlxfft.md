---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxfft"
framework: "mlx-swift/MLX"
---

# MLXFFT

**Framework**: mlx-swift/MLX  
**Kind**: enum  
**Role**: Enumeration

## Declaration

```swift
enum MLXFFT
```

## Topics

### Type Methods
- [static func fft(MLXArray, n: Int?, axis: Int, norm: FFTNorm, stream: StreamOrDevice) -> MLXArray](./mlxfft/fft%28_,n,axis,norm,stream%29.md)
  One dimensional discrete Fourier Transform.
- [static func fft2(MLXArray, s: (some Collection<Int>)?, axes: (some Collection<Int>)?, norm: FFTNorm, stream: StreamOrDevice) -> MLXArray](./mlxfft/fft2%28_,s,axes,norm,stream%29.md)
  Two dimensional discrete Fourier Transform.
- [static func fftfreq(Int, d: Double, stream: StreamOrDevice) -> MLXArray](./mlxfft/fftfreq%28_,d,stream%29.md)
  The sample frequencies of a discrete Fourier Transform.
- [static func fftn(MLXArray, s: (some Collection<Int>)?, axes: (some Collection<Int>)?, norm: FFTNorm, stream: StreamOrDevice) -> MLXArray](./mlxfft/fftn%28_,s,axes,norm,stream%29.md)
  n-dimensional discrete Fourier Transform.
- [static func fftshift(MLXArray, axes: [Int]?, stream: StreamOrDevice) -> MLXArray](./mlxfft/fftshift%28_,axes,stream%29.md)
  Shift the zero-frequency component to the center of the spectrum.
- [static func ifft(MLXArray, n: Int?, axis: Int, norm: FFTNorm, stream: StreamOrDevice) -> MLXArray](./mlxfft/ifft%28_,n,axis,norm,stream%29.md)
  One dimensional inverse discrete Fourier Transform.
- [static func ifft2(MLXArray, s: (some Collection<Int>)?, axes: (some Collection<Int>)?, norm: FFTNorm, stream: StreamOrDevice) -> MLXArray](./mlxfft/ifft2%28_,s,axes,norm,stream%29.md)
  Two dimensional inverse discrete Fourier Transform.
- [static func ifftn(MLXArray, s: (some Collection<Int>)?, axes: (some Collection<Int>)?, norm: FFTNorm, stream: StreamOrDevice) -> MLXArray](./mlxfft/ifftn%28_,s,axes,norm,stream%29.md)
  n-dimensional inverse discrete Fourier Transform.
- [static func ifftshift(MLXArray, axes: [Int]?, stream: StreamOrDevice) -> MLXArray](./mlxfft/ifftshift%28_,axes,stream%29.md)
  The inverse of [`fftshift(_:axes:stream:)`](./mlxfft/fftshift%28_,axes,stream%29.md).
- [static func irfft(MLXArray, n: Int?, axis: Int, norm: FFTNorm, stream: StreamOrDevice) -> MLXArray](./mlxfft/irfft%28_,n,axis,norm,stream%29.md)
  Inverse one dimensional discrete Fourier Transform on a real input.
- [static func irfft2(MLXArray, s: (some Collection<Int>)?, axes: (some Collection<Int>)?, norm: FFTNorm, stream: StreamOrDevice) -> MLXArray](./mlxfft/irfft2%28_,s,axes,norm,stream%29.md)
  Inverse two dimensional discrete Fourier Transform on a real input.
- [static func irfftn(MLXArray, s: (some Collection<Int>)?, axes: (some Collection<Int>)?, norm: FFTNorm, stream: StreamOrDevice) -> MLXArray](./mlxfft/irfftn%28_,s,axes,norm,stream%29.md)
  Inverse n-dimensional discrete Fourier Transform on a real input.
- [static func rfft(MLXArray, n: Int?, axis: Int, norm: FFTNorm, stream: StreamOrDevice) -> MLXArray](./mlxfft/rfft%28_,n,axis,norm,stream%29.md)
  One dimensional discrete Fourier Transform on a real input.
- [static func rfft2(MLXArray, s: (some Collection<Int>)?, axes: (some Collection<Int>)?, norm: FFTNorm, stream: StreamOrDevice) -> MLXArray](./mlxfft/rfft2%28_,s,axes,norm,stream%29.md)
  Two dimensional real discrete Fourier Transform.
- [static func rfftfreq(Int, d: Double, stream: StreamOrDevice) -> MLXArray](./mlxfft/rfftfreq%28_,d,stream%29.md)
  The sample frequencies of a discrete Fourier Transform on a real input.
- [static func rfftn(MLXArray, s: (some Collection<Int>)?, axes: (some Collection<Int>)?, norm: FFTNorm, stream: StreamOrDevice) -> MLXArray](./mlxfft/rfftn%28_,s,axes,norm,stream%29.md)
  n-dimensional real discrete Fourier Transform.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxfft)*