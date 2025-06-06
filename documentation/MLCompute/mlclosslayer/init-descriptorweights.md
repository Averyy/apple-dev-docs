# init(descriptor:weights:)

**Framework**: ML Compute  
**Kind**: init

Creates a loss layer with the descriptor and weights you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init(descriptor lossDescriptor: MLCLossDescriptor, weights: MLCTensor)
```

## Parameters

- `lossDescriptor`: An object you use to configure the loss layer.
- `weights`: The loss label weights tensor.

## See Also

- [convenience init(descriptor: MLCLossDescriptor)](mlclosslayer/init(descriptor:).md)
  Creates a loss layer with the descriptor you specify.
- [class MLCLossDescriptor](mlclossdescriptor.md)
  A configuration object you use to create a loss layer.
- [enum MLCLossType](mlclosstype.md)
  A loss function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclosslayer/init(descriptor:weights:))*