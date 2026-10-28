---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/upsample/init(scalefactor:mode:)"
framework: "mlx-swift/MLXNN"
---

# init(scaleFactor:mode:)

**Framework**: mlx-swift/MLXNN  
**Kind**: init  
**Role**: Initializer

Upsample the input signal spatially.

## Declaration

```swift
init(scaleFactor: FloatOrArray, mode: Upsample.Mode = .nearest)
```

## Discussion

The spatial dimensions are by convention dimensions `1` to `x.ndim - 2`. The first is the batch dimension and the last is the feature dimension.

For example, an audio signal would be 3D with 1 spatial dimension, an image 4D with 2 and so on and so forth.

There are three upsampling algorithms implemented:

- [`Upsample.Mode.nearest`](./mode-swift.enum/nearest.md)
- [`Upsample.Mode.linear(alignCorners:)`](./mode-swift.enum/linear%28aligncorners%29.md)
- [`Upsample.Mode.cubic(alignCorners:)`](./mode-swift.enum/cubic%28aligncorners%29.md)

All can be applied to any number of spatial dimensions and the linear interpolation will be bilinear, trilinear etc when applied to more than one spatial dimension.

## Parameters

- `scaleFactor`: The multiplier for the spatial size. If a `float` is provided, it is the multiplier for all spatial dimensions. Otherwise, the number of scale factors provided must match the number of spatial dimensions.
- `mode`: The upsampling algorithm


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/upsample/init(scalefactor:mode:))*