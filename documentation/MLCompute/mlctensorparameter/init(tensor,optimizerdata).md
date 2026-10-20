# init(tensor:optimizerData:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a tensor parameter with the tensor and optimizer data you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init(tensor: MLCTensor, optimizerData: [MLCTensorData]?)
```

```objc
+ (instancetype) parameterWithTensor:(MLCTensor *) tensor optimizerData:(NSArray<MLCTensorData *> *) optimizerData;
```

## Parameters

- `tensor`: The underlying tensor.
- `optimizerData`: The optimizer data.

## See Also

### Creating Tensor Parameters
- [convenience init(tensor: MLCTensor)](./init%28tensor%29.md)
  Creates a tensor parameter with the tensor you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensorparameter/init(tensor:optimizerdata:))*