# MLCSoftmaxOperation

**Framework**: ML Compute  
**Kind**: enum

A softmax operation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
enum MLCSoftmaxOperation
```

## Topics

### Enumeration Cases
- [MLCSoftmaxOperation.softmax](mlcsoftmaxoperation/softmax.md)
- [MLCSoftmaxOperation.logSoftmax](mlcsoftmaxoperation/logsoftmax.md)
- [var debugDescription: String](mlcsoftmaxoperation/debugdescription.md)
  A textual description of the softmax operation, suitable for debugging.
### Initializers
- [init?(rawValue: Int32)](mlcsoftmaxoperation/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [convenience init(operation: MLCSoftmaxOperation)](mlcsoftmaxlayer/init(operation:).md)
  Creates a softmax layer with the operation you specify.
- [convenience init(operation: MLCSoftmaxOperation, dimension: Int)](mlcsoftmaxlayer/init(operation:dimension:).md)
  Creates a softmax layer with the operation and dimension you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcsoftmaxoperation)*