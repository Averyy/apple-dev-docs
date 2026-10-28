---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/avgpool2d/init(kernelsize:stride:padding:)"
framework: "mlx-swift/MLXNN"
---

# init(kernelSize:stride:padding:)

**Framework**: mlx-swift/MLXNN  
**Kind**: init  
**Role**: Initializer

Applies 2-dimensional average pooling.

## Declaration

```swift
init(kernelSize: IntOrPair, stride: IntOrPair, padding: IntOrPair = 0)
```

## Discussion

The input is expected to be `NHWC`. The output will have the same N/C dimensions with the new H/W = floor((H/W - kernel)/stride) + 1

See [AvgPool2d python docs](https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.AvgPool2d.html) for more information.

## Parameters

- `kernelSize`: Size of the pooling window
- `stride`: Stride of the pooling window
- `padding`: How much zero padding to apply to the input. The padding is applied on both sides of the height and width axis. Default: 0


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/avgpool2d/init(kernelsize:stride:padding:))*