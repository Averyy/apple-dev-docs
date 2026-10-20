# init(operation:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a softmax layer with the operation you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init(operation: MLCSoftmaxOperation)
```

```objc
+ (instancetype) layerWithOperation:(MLCSoftmaxOperation) operation;
```

## Parameters

- `operation`: The softmax operation.

## See Also

### Creating Softmax Layers
- [convenience init(operation: MLCSoftmaxOperation, dimension: Int)](./init%28operation,dimension%29.md)
  Creates a softmax layer with the operation and dimension you specify.
- [enum MLCSoftmaxOperation](../mlcsoftmaxoperation.md)
  A softmax operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcsoftmaxlayer/init(operation:))*