---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/lossreduction"
framework: "mlx-swift/MLXNN"
---

# LossReduction

**Framework**: mlx-swift/MLXNN  
**Kind**: enum  
**Role**: Enumeration

Different types of loss reductions

## Declaration

```swift
enum LossReduction
```

## Topics

### Enumeration Cases
- [LossReduction.mean](./lossreduction/mean.md)
  take the `mean` of the loss. This produces a a scalar array
- [LossReduction.none](./lossreduction/none.md)
  take the loss as-is.  This produces an array the same shape as the input.
- [LossReduction.sum](./lossreduction/sum.md)
  take the `sum` of the loss.  This produces a a scalar array.
### Initializers
- [init?(rawValue: String)](./lossreduction/init%28rawvalue%29.md)
### Instance Methods
- [func reduce(loss: MLXArray) -> MLXArray](./lossreduction/reduce%28loss%29.md)
### Default Implementations
- [Equatable Implementations](./lossreduction/equatable-implementations.md)
- [RawRepresentable Implementations](./lossreduction/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.RawRepresentable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/lossreduction)*