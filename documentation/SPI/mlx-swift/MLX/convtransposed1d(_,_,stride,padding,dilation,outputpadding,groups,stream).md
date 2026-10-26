---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/convtransposed1d(_:_:stride:padding:dilation:outputpadding:groups:stream:)"
framework: "mlx-swift/MLX"
---

# convTransposed1d(_:_:stride:padding:dilation:outputPadding:groups:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

1D transposed convolution over an input with several channels.

## Declaration

```swift
func convTransposed1d(_ array: MLXArray, _ weight: MLXArray, stride: Int = 1, padding: Int = 0, dilation: Int = 1, outputPadding: Int = 0, groups: Int = 1, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

> **Note**: Only the default `groups=1` is currently supported.

##### See Also

- [Convolution](./convolution.md)
- [`conv1d(_:_:stride:padding:dilation:groups:stream:)`](./conv1d%28_,_,stride,padding,dilation,groups,stream%29.md)
- [`convTransposed2d(_:_:stride:padding:dilation:outputPadding:groups:stream:)`](./convtransposed2d%28_,_,stride,padding,dilation,outputpadding,groups,stream%29.md)
- [`convTransposed3d(_:_:stride:padding:dilation:outputPadding:groups:stream:)`](./convtransposed3d%28_,_,stride,padding,dilation,outputpadding,groups,stream%29.md)
- [`convolve(_:_:mode:stream:)`](./convolve%28_,_,mode,stream%29.md)

## Parameters

- `array`: Input array of shape `[N, H, C_in]`
- `weight`: Weight array of shape `[C_out, H, C_in]`
- `stride`: Kernel stride
- `padding`: Input padding
- `dilation`: Kernel dilation
- `outputPadding`: Output padding
- `groups`: Input feature groups
- `stream`: Stream or device to evaluate on

## See Also

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
- [func convTransposed2d(MLXArray, MLXArray, stride: IntOrPair, padding: IntOrPair, dilation: IntOrPair, outputPadding: IntOrPair, groups: Int, stream: StreamOrDevice) -> MLXArray](./convtransposed2d%28_,_,stride,padding,dilation,outputpadding,groups,stream%29.md)
  2D transposed convolution over an input with several channels.
- [func convTransposed3d(MLXArray, MLXArray, stride: IntOrTriple, padding: IntOrTriple, dilation: IntOrTriple, outputPadding: IntOrTriple, groups: Int, stream: StreamOrDevice) -> MLXArray](./convtransposed3d%28_,_,stride,padding,dilation,outputpadding,groups,stream%29.md)
  3D transposed convolution over an input with several channels.
- [func convolve(some ScalarOrArray, some ScalarOrArray, mode: ConvolveMode, stream: StreamOrDevice) -> MLXArray](./convolve%28_,_,mode,stream%29.md)
  The discrete convolution of 1D arrays.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/convtransposed1d(_:_:stride:padding:dilation:outputpadding:groups:stream:))*