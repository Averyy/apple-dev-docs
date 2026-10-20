# MLCReductionType

**Framework**: ML Compute  
**Kind**: enum  
**Role**: Enumeration

Constants that describe a reduction operation type.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
enum MLCReductionType
```

```c
enum MLCReductionType : int32_t;
```

## Topics

### Enumeration Cases
- [MLCReductionType.all](./mlcreductiontype/all.md)
  A reduction operation that applies to all dimensions.
- [MLCReductionType.any](./mlcreductiontype/any.md)
  A reduction operation that applies to any dimension.
- [MLCReductionType.argMax](./mlcreductiontype/argmax.md)
  A reduction operation that applies to the maximum dimension you specify.
- [MLCReductionType.argMin](./mlcreductiontype/argmin.md)
  A reduction operation that applies to the minimum dimension you specify.
- [MLCReductionType.max](./mlcreductiontype/max.md)
  A reduction operation that applies to the maximum dimension.
- [MLCReductionType.mean](./mlcreductiontype/mean.md)
  A reduction operation that applies to the mean of the dimensions.
- [MLCReductionType.min](./mlcreductiontype/min.md)
  A reduction operation that applies to the minimum dimension.
- [MLCReductionType.none](./mlcreductiontype/none.md)
  A reduction operation that applies no reduction.
- [MLCReductionType.sum](./mlcreductiontype/sum.md)
  A reduction operation that applies to the sum of the dimensions.
- [MLCReductionType.l1Norm](./mlcreductiontype/l1norm.md)
  A reduction operation that applies a lasso regularization penalty.
- [var debugDescription: String](./mlcreductiontype/debugdescription.md)
  A textual description of the reduction operation you use for debugging.
### Initializers
- [init?(rawValue: Int32)](./mlcreductiontype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating Reduction Layers
- [convenience init?(reductionType: MLCReductionType, dimension: Int)](./mlcreductionlayer/init%28reductiontype,dimension%29.md)
  Creates a reduction layer using the reduction type and dimension you specify.
- [convenience init?(reductionType: MLCReductionType, dimensions: [Int])](./mlcreductionlayer/init%28reductiontype,dimensions%29.md)
  Creates a reduction layer using the reduction type and dimensions you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcreductiontype)*