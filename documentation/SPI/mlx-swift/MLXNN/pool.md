---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/pool"
framework: "mlx-swift/MLXNN"
---

# Pool

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

Abstract pooling layer.

## Declaration

```swift
class Pool
```

### See Also

- [`MaxPool1d`](./maxpool1d.md)
- [`MaxPool2d`](./maxpool2d.md)
- [`MaxPool3d`](./maxpool3d.md)
- [`AvgPool1d`](./avgpool1d.md)
- [`AvgPool2d`](./avgpool2d.md)
- [`AvgPool3d`](./avgpool3d.md)

## Topics

### Instance Properties
- [let axes: [Int]](./pool/axes.md)
- [let kernelSize: [Int]](./pool/kernelsize.md)
- [let padding: [Int]](./pool/padding.md)
- [let paddingValue: Float](./pool/paddingvalue.md)
- [let poolingOp: (MLXArray, [Int]) -> MLXArray](./pool/poolingop.md)
- [let stride: [Int]](./pool/stride.md)
### Instance Methods
- [func callAsFunction(MLXArray) -> MLXArray](./pool/callasfunction%28_%29.md)

## Relationships

### Inherits From
- [Module](./module.md)
### Inherited By
- [AvgPool1d](./avgpool1d.md)
- [AvgPool2d](./avgpool2d.md)
- [AvgPool3d](./avgpool3d.md)
- [MaxPool1d](./maxpool1d.md)
- [MaxPool2d](./maxpool2d.md)
- [MaxPool3d](./maxpool3d.md)
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- Swift.CustomStringConvertible
- [UnaryLayer](./unarylayer.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/pool)*