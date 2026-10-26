# MLCLossType

**Framework**: ML Compute  
**Kind**: enum  
**Role**: Enumeration

A loss function.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
enum MLCLossType
```

```c
enum MLCLossType : int32_t;
```

## Topics

### Enumeration Cases
- [MLCLossType.categoricalCrossEntropy](./mlclosstype/categoricalcrossentropy.md)
- [MLCLossType.cosineDistance](./mlclosstype/cosinedistance.md)
- [MLCLossType.hinge](./mlclosstype/hinge.md)
- [MLCLossType.huber](./mlclosstype/huber.md)
- [MLCLossType.log](./mlclosstype/log.md)
- [MLCLossType.meanAbsoluteError](./mlclosstype/meanabsoluteerror.md)
- [MLCLossType.meanSquaredError](./mlclosstype/meansquarederror.md)
- [MLCLossType.sigmoidCrossEntropy](./mlclosstype/sigmoidcrossentropy.md)
- [MLCLossType.softmaxCrossEntropy](./mlclosstype/softmaxcrossentropy.md)
- [var debugDescription: String](./mlclosstype/debugdescription.md)
  A textual description of the loss type, suitable for debugging.
- [MLCLossTypeCount](./mlclosstype/mlclosstypecount.md)
### Initializers
- [init?(rawValue: Int32)](./mlclosstype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating Loss Layers with Descriptors
- [convenience init(descriptor: MLCLossDescriptor)](./mlclosslayer/init%28descriptor%29.md)
  Creates a loss layer with the descriptor you specify.
- [convenience init(descriptor: MLCLossDescriptor, weights: MLCTensor)](./mlclosslayer/init%28descriptor,weights%29.md)
  Creates a loss layer with the descriptor and weights you specify.
- [class MLCLossDescriptor](./mlclossdescriptor.md)
  A configuration object you use to create a loss layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclosstype)*