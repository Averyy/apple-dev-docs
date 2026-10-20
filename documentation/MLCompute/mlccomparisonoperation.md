# MLCComparisonOperation

**Framework**: ML Compute  
**Kind**: enum  
**Role**: Enumeration

A comparison operation.

**Availability**:
- iOS 14.5+ - Deprecated in 17.4
- iPadOS 14.5+ - Deprecated in 17.4
- Mac Catalyst 14.5+ - Deprecated in 17.4
- macOS 11.3+ - Deprecated in 14.3
- tvOS 14.5+ - Deprecated in 17.4

## Declaration

```swift
enum MLCComparisonOperation
```

```c
enum MLCComparisonOperation : int32_t;
```

## Topics

### Enumeration Cases
- [MLCComparisonOperation.equal](./mlccomparisonoperation/equal.md)
- [MLCComparisonOperation.greater](./mlccomparisonoperation/greater.md)
- [MLCComparisonOperation.greaterOrEqual](./mlccomparisonoperation/greaterorequal.md)
- [MLCComparisonOperation.less](./mlccomparisonoperation/less.md)
- [MLCComparisonOperation.lessOrEqual](./mlccomparisonoperation/lessorequal.md)
- [MLCComparisonOperation.logicalAND](./mlccomparisonoperation/logicaland.md)
- [MLCComparisonOperation.logicalNAND](./mlccomparisonoperation/logicalnand.md)
- [MLCComparisonOperation.logicalNOR](./mlccomparisonoperation/logicalnor.md)
- [MLCComparisonOperation.logicalNOT](./mlccomparisonoperation/logicalnot.md)
- [MLCComparisonOperation.logicalOR](./mlccomparisonoperation/logicalor.md)
- [MLCComparisonOperation.logicalXOR](./mlccomparisonoperation/logicalxor.md)
- [MLCComparisonOperation.notEqual](./mlccomparisonoperation/notequal.md)
- [var debugDescription: String](./mlccomparisonoperation/debugdescription.md)
  A textual description of the comparison operation, suitable for debugging.
### Initializers
- [init?(rawValue: Int32)](./mlccomparisonoperation/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating Comparison Layers
- [convenience init(operation: MLCComparisonOperation)](./mlccomparisonlayer/init%28operation%29.md)
  Creates a comparison layer with the operation you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlccomparisonoperation)*