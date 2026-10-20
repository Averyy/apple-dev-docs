# init(operation:dimension:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a softmax layer with the operation and dimension you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init(operation: MLCSoftmaxOperation, dimension: Int)
```

```objc
+ (instancetype) layerWithOperation:(MLCSoftmaxOperation) operation dimension:(NSUInteger) dimension;
```

## Parameters

- `operation`: The softmax operation.
- `dimension`: The dimension over which you perform the softmax operation.

## See Also

### Creating Softmax Layers
- [convenience init(operation: MLCSoftmaxOperation)](./init%28operation%29.md)
  Creates a softmax layer with the operation you specify.
- [enum MLCSoftmaxOperation](../mlcsoftmaxoperation.md)
  A softmax operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcsoftmaxlayer/init(operation:dimension:))*