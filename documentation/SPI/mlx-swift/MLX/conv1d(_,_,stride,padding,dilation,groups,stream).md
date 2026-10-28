---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/conv1d(_:_:stride:padding:dilation:groups:stream:)"
framework: "mlx-swift/MLX"
---

# conv1d(_:_:stride:padding:dilation:groups:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

1D convolution over an input with several channels.

## Declaration

```swift
func conv1d(_ array: MLXArray, _ weight: MLXArray, stride: Int = 1, padding: Int = 0, dilation: Int = 1, groups: Int = 1, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](./converting-python.md)

## Discussion

> **Note**: Only the default `groups=1` is currently supported.

### See Also

- [Convolution](./convolution.md)
- [`conv2d(_:_:stride:padding:dilation:groups:stream:)`](./conv2d%28_,_,stride,padding,dilation,groups,stream%29.md)
- [`conv3d(_:_:stride:padding:dilation:groups:stream:)`](./conv3d%28_,_,stride,padding,dilation,groups,stream%29.md)
- [`convolve(_:_:mode:stream:)`](./convolve%28_,_,mode,stream%29.md)

## Parameters

- `array`: Input array of shape `[N, H, C_in]`
- `weight`: Weight array of shape `[C_out, H, C_in]`
- `stride`: Kernel stride
- `padding`: Input padding
- `dilation`: Kernel dilation
- `groups`: Input feature groups
- `stream`: Stream or device to evaluate on

## See Also

### Convolution
- [func conv2d(MLXArray, MLXArray, stride: IntOrPair, padding: IntOrPair, dilation: IntOrPair, groups: Int, stream: StreamOrDevice) -> MLXArray](./conv2d%28_,_,stride,padding,dilation,groups,stream%29.md)
  2D convolution over an input with several channels.
- [func convolve(some ScalarOrArray, some ScalarOrArray, mode: ConvolveMode, stream: StreamOrDevice) -> MLXArray](./convolve%28_,_,mode,stream%29.md)
  The discrete convolution of 1D arrays.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/conv1d(_:_:stride:padding:dilation:groups:stream:))*