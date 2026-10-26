---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/conv2d(_:_:stride:padding:dilation:groups:stream:)"
framework: "mlx-swift/MLX"
---

# conv2d(_:_:stride:padding:dilation:groups:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

2D convolution over an input with several channels.

## Declaration

```swift
func conv2d(_ array: MLXArray, _ weight: MLXArray, stride: IntOrPair = 1, padding: IntOrPair = 0, dilation: IntOrPair = 1, groups: Int = 1, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](./converting-python.md)

#### Discussion

> **Note**: Only the default `groups=1` is currently supported.

The numeric parameters may be given as single values:

```swift
padding: 1
```

This will produce a padding of `(1, 1)`.  You can also give an array:

```swift
padding: [2, 3]
```

See [`IntOrPair`](./intorpair.md) for more information.

##### See Also

- [Convolution](./convolution.md)
- [`IntOrPair`](./intorpair.md)
- [`conv1d(_:_:stride:padding:dilation:groups:stream:)`](./conv1d%28_,_,stride,padding,dilation,groups,stream%29.md)
- [`conv3d(_:_:stride:padding:dilation:groups:stream:)`](./conv3d%28_,_,stride,padding,dilation,groups,stream%29.md)
- [`convolve(_:_:mode:stream:)`](./convolve%28_,_,mode,stream%29.md)
- [`convGeneral(_:_:strides:padding:kernelDilation:inputDilation:groups:flip:stream:)`](./convgeneral%28_,_,strides,padding,kerneldilation,inputdilation,groups,flip,stream%29-9t1sj.md)

## Parameters

- `array`: Input array of shape `[N, H, W, C_in]`
- `weight`: Weight array of shape `[C_out, H, W, C_in]`
- `stride`: Kernel stride
- `padding`: Input padding
- `dilation`: Kernel dilation
- `groups`: Input feature groups
- `stream`: Stream or device to evaluate on

## See Also

### Convolution
- [func conv1d(MLXArray, MLXArray, stride: Int, padding: Int, dilation: Int, groups: Int, stream: StreamOrDevice) -> MLXArray](./conv1d%28_,_,stride,padding,dilation,groups,stream%29.md)
  1D convolution over an input with several channels.
- [func convolve(some ScalarOrArray, some ScalarOrArray, mode: ConvolveMode, stream: StreamOrDevice) -> MLXArray](./convolve%28_,_,mode,stream%29.md)
  The discrete convolution of 1D arrays.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/conv2d(_:_:stride:padding:dilation:groups:stream:))*