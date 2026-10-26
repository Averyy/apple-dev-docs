---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/avgpool3d/init(kernelsize:stride:padding:)"
framework: "mlx-swift/MLXNN"
---

# init(kernelSize:stride:padding:)

**Framework**: mlx-swift/MLXNN  
**Kind**: init  
**Role**: Initializer

Applies 3-dimensional average pooling.

## Declaration

```swift
init(kernelSize: IntOrTriple, stride: IntOrTriple, padding: IntOrTriple = 0)
```

#### Discussion

The input is expected to be `NDHWC`. The output will have the same N/C dimensions with the new D/H/W = floor((D/H/W - kernel)/stride) + 1

The parameters `kernelSize`, `stride`, and `padding` can either be:

- a single `Int` – in which case the same value is used for the depth, height, and width axis
- a tuple of three `Int`s – in which case, the first `Int` is used for the depth axis, the second `Int` for the height axis, and the third `Int` for the width axis

See [AvgPool3d python docs](https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.AvgPool3d.html) for more information.

## Parameters

- `kernelSize`: Size of the pooling window
- `stride`: Stride of the pooling window
- `padding`: How much zero padding to apply to the input. The padding is applied on both sides of the depth, height and width axis. Default: 0


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/avgpool3d/init(kernelsize:stride:padding:))*