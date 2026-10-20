# MLCSoftmaxOperation

**Framework**: ML Compute  
**Kind**: enum  
**Role**: Enumeration

A softmax operation.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
enum MLCSoftmaxOperation
```

```c
enum MLCSoftmaxOperation : int32_t;
```

## Topics

### Enumeration Cases
- [MLCSoftmaxOperation.softmax](./mlcsoftmaxoperation/softmax.md)
- [MLCSoftmaxOperation.logSoftmax](./mlcsoftmaxoperation/logsoftmax.md)
- [var debugDescription: String](./mlcsoftmaxoperation/debugdescription.md)
  A textual description of the softmax operation, suitable for debugging.
### Initializers
- [init?(rawValue: Int32)](./mlcsoftmaxoperation/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating Softmax Layers
- [convenience init(operation: MLCSoftmaxOperation)](./mlcsoftmaxlayer/init%28operation%29.md)
  Creates a softmax layer with the operation you specify.
- [convenience init(operation: MLCSoftmaxOperation, dimension: Int)](./mlcsoftmaxlayer/init%28operation,dimension%29.md)
  Creates a softmax layer with the operation and dimension you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcsoftmaxoperation)*