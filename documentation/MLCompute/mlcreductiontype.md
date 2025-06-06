# MLCReductionType

**Framework**: ML Compute  
**Kind**: enum

Constants that describe a reduction operation type.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
enum MLCReductionType
```

## Topics

### Enumeration Cases
- [MLCReductionType.all](mlcreductiontype/all.md)
  A reduction operation that applies to all dimensions.
- [MLCReductionType.any](mlcreductiontype/any.md)
  A reduction operation that applies to any dimension.
- [MLCReductionType.argMax](mlcreductiontype/argmax.md)
  A reduction operation that applies to the maximum dimension you specify.
- [MLCReductionType.argMin](mlcreductiontype/argmin.md)
  A reduction operation that applies to the minimum dimension you specify.
- [MLCReductionType.max](mlcreductiontype/max.md)
  A reduction operation that applies to the maximum dimension.
- [MLCReductionType.mean](mlcreductiontype/mean.md)
  A reduction operation that applies to the mean of the dimensions.
- [MLCReductionType.min](mlcreductiontype/min.md)
  A reduction operation that applies to the minimum dimension.
- [MLCReductionType.none](mlcreductiontype/none.md)
  A reduction operation that applies no reduction.
- [MLCReductionType.sum](mlcreductiontype/sum.md)
  A reduction operation that applies to the sum of the dimensions.
- [MLCReductionType.l1Norm](mlcreductiontype/l1norm.md)
  A reduction operation that applies a lasso regularization penalty.
- [var debugDescription: String](mlcreductiontype/debugdescription.md)
  A textual description of the reduction operation you use for debugging.
### Initializers
- [init?(rawValue: Int32)](mlcreductiontype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [convenience init?(reductionType: MLCReductionType, dimension: Int)](mlcreductionlayer/init(reductiontype:dimension:).md)
  Creates a reduction layer using the reduction type and dimension you specify.
- [convenience init?(reductionType: MLCReductionType, dimensions: [Int])](mlcreductionlayer/init(reductiontype:dimensions:).md)
  Creates a reduction layer using the reduction type and dimensions you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcreductiontype)*