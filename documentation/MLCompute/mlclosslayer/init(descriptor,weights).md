# init(descriptor:weights:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a loss layer with the descriptor and weights you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init(descriptor lossDescriptor: MLCLossDescriptor, weights: MLCTensor)
```

```objc
+ (instancetype) layerWithDescriptor:(MLCLossDescriptor *) lossDescriptor weights:(MLCTensor *) weights;
```

## Parameters

- `lossDescriptor`: An object you use to configure the loss layer.
- `weights`: The loss label weights tensor.

## See Also

### Creating Loss Layers with Descriptors
- [convenience init(descriptor: MLCLossDescriptor)](./init%28descriptor%29.md)
  Creates a loss layer with the descriptor you specify.
- [class MLCLossDescriptor](../mlclossdescriptor.md)
  A configuration object you use to create a loss layer.
- [enum MLCLossType](../mlclosstype.md)
  A loss function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclosslayer/init(descriptor:weights:))*