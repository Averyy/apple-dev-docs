# MLCLossType

**Framework**: ML Compute  
**Kind**: enum

A loss function.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
enum MLCLossType
```

## Topics

### Enumeration Cases
- [MLCLossType.categoricalCrossEntropy](mlclosstype/categoricalcrossentropy.md)
- [MLCLossType.cosineDistance](mlclosstype/cosinedistance.md)
- [MLCLossType.hinge](mlclosstype/hinge.md)
- [MLCLossType.huber](mlclosstype/huber.md)
- [MLCLossType.log](mlclosstype/log.md)
- [MLCLossType.meanAbsoluteError](mlclosstype/meanabsoluteerror.md)
- [MLCLossType.meanSquaredError](mlclosstype/meansquarederror.md)
- [MLCLossType.sigmoidCrossEntropy](mlclosstype/sigmoidcrossentropy.md)
- [MLCLossType.softmaxCrossEntropy](mlclosstype/softmaxcrossentropy.md)
- [var debugDescription: String](mlclosstype/debugdescription.md)
  A textual description of the loss type, suitable for debugging.
### Initializers
- [init?(rawValue: Int32)](mlclosstype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [convenience init(descriptor: MLCLossDescriptor)](mlclosslayer/init(descriptor:).md)
  Creates a loss layer with the descriptor you specify.
- [convenience init(descriptor: MLCLossDescriptor, weights: MLCTensor)](mlclosslayer/init(descriptor:weights:).md)
  Creates a loss layer with the descriptor and weights you specify.
- [class MLCLossDescriptor](mlclossdescriptor.md)
  A configuration object you use to create a loss layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclosstype)*