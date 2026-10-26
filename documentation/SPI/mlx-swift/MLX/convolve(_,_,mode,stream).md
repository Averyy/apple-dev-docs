---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/convolve(_:_:mode:stream:)"
framework: "mlx-swift/MLX"
---

# convolve(_:_:mode:stream:)

**Framework**: mlx-swift/MLX  
**Kind**: func  
**Role**: Function

The discrete convolution of 1D arrays.

## Declaration

```swift
func convolve(_ a: some ScalarOrArray, _ b: some ScalarOrArray, mode: ConvolveMode = .full, stream: StreamOrDevice = .default) -> MLXArray
```

## Mentions

- [Converting From Python](./converting-python.md)

##### See Also

- [Convolution](./convolution.md)
- [`conv1d(_:_:stride:padding:dilation:groups:stream:)`](./conv1d%28_,_,stride,padding,dilation,groups,stream%29.md)
- [`conv2d(_:_:stride:padding:dilation:groups:stream:)`](./conv2d%28_,_,stride,padding,dilation,groups,stream%29.md)

## Parameters

- `a`: 1D input array
- `b`: 1D input array
- `mode`: Padding mode
- `stream`: Stream or device to evaluate on

## See Also

### Convolution
- [func conv1d(MLXArray, MLXArray, stride: Int, padding: Int, dilation: Int, groups: Int, stream: StreamOrDevice) -> MLXArray](./conv1d%28_,_,stride,padding,dilation,groups,stream%29.md)
  1D convolution over an input with several channels.
- [func conv2d(MLXArray, MLXArray, stride: IntOrPair, padding: IntOrPair, dilation: IntOrPair, groups: Int, stream: StreamOrDevice) -> MLXArray](./conv2d%28_,_,stride,padding,dilation,groups,stream%29.md)
  2D convolution over an input with several channels.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/convolve(_:_:mode:stream:))*