---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/convgeneral(_:_:strides:padding:kerneldilation:inputdilation:groups:flip:stream:)-6j1nr"
framework: "mlx-swift/MLX"
---

# convGeneral(_:_:strides:padding:kernelDilation:inputDilation:groups:flip:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

General convolution over an input with several channels with a padding pair.

## Declaration

```swift
func convGeneral(_ array: MLXArray, _ weight: MLXArray, strides: IntOrArray = 1, padding: (Int, Int), kernelDilation: IntOrArray = 1, inputDilation: IntOrArray = 1, groups: Int = 1, flip: Bool = false, stream: StreamOrDevice = .default) -> MLXArray
```

#### Discussion

> **Note**: Only 1d and 2d convolutions are supported at the moment

> **Note**: The default `groups: 1` is currently supported

##### See Also

- [Convolution](./convolution.md)
- [`IntOrArray`](./intorarray.md)
- [`conv2d(_:_:stride:padding:dilation:groups:stream:)`](./conv2d%28_,_,stride,padding,dilation,groups,stream%29.md)
- [`convGeneral(_:_:strides:padding:kernelDilation:inputDilation:groups:flip:stream:)`](./convgeneral%28_,_,strides,padding,kerneldilation,inputdilation,groups,flip,stream%29-6j1nr.md)

## Parameters

- `array`: Input array of shape `(N, ..., C_in)`
- `weight`: Weight array of shape `(C_out, ..., C_in)`
- `strides`: `Int` or `some Collection<Int>` with kernel strides.  All dimensions get the same stride if only one number is specified.
- `padding`: Pair of padding values to apply to all dimensions
- `kernelDilation`: `Int` or `some Collection<Int>` with kernel dilation.  All dimensions get the same dilation if only one number is specified.
- `inputDilation`: `Int` or `some Collection<Int>` with input dilation.  All dimensions get the same dilation if only one number is specified.
- `groups`: Input feature groups
- `flip`: Flip the order in which the spatial dimensions of the weights are processed. Performs the cross-correlation operator when `flip` is `false` and the convolution operator otherwise.
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
- [func convTransposed1d(MLXArray, MLXArray, stride: Int, padding: Int, dilation: Int, outputPadding: Int, groups: Int, stream: StreamOrDevice) -> MLXArray](./convtransposed1d%28_,_,stride,padding,dilation,outputpadding,groups,stream%29.md)
  1D transposed convolution over an input with several channels.
- [func convTransposed2d(MLXArray, MLXArray, stride: IntOrPair, padding: IntOrPair, dilation: IntOrPair, outputPadding: IntOrPair, groups: Int, stream: StreamOrDevice) -> MLXArray](./convtransposed2d%28_,_,stride,padding,dilation,outputpadding,groups,stream%29.md)
  2D transposed convolution over an input with several channels.
- [func convTransposed3d(MLXArray, MLXArray, stride: IntOrTriple, padding: IntOrTriple, dilation: IntOrTriple, outputPadding: IntOrTriple, groups: Int, stream: StreamOrDevice) -> MLXArray](./convtransposed3d%28_,_,stride,padding,dilation,outputpadding,groups,stream%29.md)
  3D transposed convolution over an input with several channels.
- [func convolve(some ScalarOrArray, some ScalarOrArray, mode: ConvolveMode, stream: StreamOrDevice) -> MLXArray](./convolve%28_,_,mode,stream%29.md)
  The discrete convolution of 1D arrays.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/convgeneral(_:_:strides:padding:kerneldilation:inputdilation:groups:flip:stream:)-6j1nr)*