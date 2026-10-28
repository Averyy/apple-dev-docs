---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/maxpool1d/init(kernelsize:stride:padding:)"
framework: "mlx-swift/MLXNN"
---

# init(kernelSize:stride:padding:)

**Framework**: mlx-swift/MLXNN  
**Kind**: init  
**Role**: Initializer

Applies 1-dimensional max pooling.

## Declaration

```swift
init(kernelSize: Int, stride: Int, padding: Int = 0)
```

## Discussion

The input is expected to be `NLC`. The output will have the same N/C dimensions with the new L = floor((L - kernel)/stride) + 1

See [MaxPool1d python docs](https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.MaxPool1d.html) for more information.

## Parameters

- `kernelSize`: Size of the pooling window
- `stride`: Stride of the pooling window
- `padding`: How much negative infinity padding to apply to the input. The padding is applied to both sides of the spatial axis. Default: 0


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/maxpool1d/init(kernelsize:stride:padding:))*