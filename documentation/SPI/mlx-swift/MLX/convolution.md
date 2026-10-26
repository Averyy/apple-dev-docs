---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/convolution"
framework: "mlx-swift/MLX"
---

# Convolution

**Framework**: mlx-swift/MLX  
**Role**: API Collection

Convolution operations.

## Topics

### Convolution Functions
- [func conv1d(MLXArray, MLXArray, stride: Int, padding: Int, dilation: Int, groups: Int, stream: StreamOrDevice) -> MLXArray](./conv1d%28_,_,stride,padding,dilation,groups,stream%29.md)
  1D convolution over an input with several channels.
- [func conv2d(MLXArray, MLXArray, stride: IntOrPair, padding: IntOrPair, dilation: IntOrPair, groups: Int, stream: StreamOrDevice) -> MLXArray](./conv2d%28_,_,stride,padding,dilation,groups,stream%29.md)
  2D convolution over an input with several channels.
- [func conv3d(MLXArray, MLXArray, stride: IntOrTriple, padding: IntOrTriple, dilation: IntOrTriple, groups: Int, stream: StreamOrDevice) -> MLXArray](./conv3d%28_,_,stride,padding,dilation,groups,stream%29.md)
  3D convolution over an input with several channels.
- [func convGeneral(MLXArray, MLXArray, strides: IntOrArray, padding: IntOrArray, kernelDilation: IntOrArray, inputDilation: IntOrArray, groups: Int, flip: Bool, stream: StreamOrDevice) -> MLXArray](./convgeneral%28_,_,strides,padding,kerneldilation,inputdilation,groups,flip,stream%29-9t1sj.md)
  General convolution over an input with several channels.
- [func convGeneral(MLXArray, MLXArray, strides: IntOrArray, padding: (Int, Int), kernelDilation: IntOrArray, inputDilation: IntOrArray, groups: Int, flip: Bool, stream: StreamOrDevice) -> MLXArray](./convgeneral%28_,_,strides,padding,kerneldilation,inputdilation,groups,flip,stream%29-6j1nr.md)
  General convolution over an input with several channels with a padding pair.
- [func convTransposed1d(MLXArray, MLXArray, stride: Int, padding: Int, dilation: Int, outputPadding: Int, groups: Int, stream: StreamOrDevice) -> MLXArray](./convtransposed1d%28_,_,stride,padding,dilation,outputpadding,groups,stream%29.md)
  1D transposed convolution over an input with several channels.
- [func convTransposed2d(MLXArray, MLXArray, stride: IntOrPair, padding: IntOrPair, dilation: IntOrPair, outputPadding: IntOrPair, groups: Int, stream: StreamOrDevice) -> MLXArray](./convtransposed2d%28_,_,stride,padding,dilation,outputpadding,groups,stream%29.md)
  2D transposed convolution over an input with several channels.
- [func convTransposed3d(MLXArray, MLXArray, stride: IntOrTriple, padding: IntOrTriple, dilation: IntOrTriple, outputPadding: IntOrTriple, groups: Int, stream: StreamOrDevice) -> MLXArray](./convtransposed3d%28_,_,stride,padding,dilation,outputpadding,groups,stream%29.md)
  3D transposed convolution over an input with several channels.
- [func convolve(some ScalarOrArray, some ScalarOrArray, mode: ConvolveMode, stream: StreamOrDevice) -> MLXArray](./convolve%28_,_,mode,stream%29.md)
  The discrete convolution of 1D arrays.

## See Also

### Arithmetic Operators and Functions
- [Arithmetic](./arithmetic.md)
  MLX supports a wide range of binary arithmetic operators.
- [Cumulative Operations](./cumulative.md)
  Operations that produce a cumulative result.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/convolution)*