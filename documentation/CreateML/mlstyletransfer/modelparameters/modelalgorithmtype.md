# MLStyleTransfer.ModelParameters.ModelAlgorithmType

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

The style transfer training algorithm options.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum ModelAlgorithmType
```

#### Overview

This object uses a convolutional neural network for training the style transfer model, giving more detailed style. It’s ideal for cases where latency is not the main concern, such as single images.

## Topics

### Selecting an algorithm type
- [MLStyleTransfer.ModelParameters.ModelAlgorithmType.cnn](./modelalgorithmtype/cnn.md)
  A style-transfer training algorithm that generates a model that prioritizes image quality over speed.
- [MLStyleTransfer.ModelParameters.ModelAlgorithmType.cnnLite](./modelalgorithmtype/cnnlite.md)
  A style-transfer training algorithm that generates a model that prioritizes speed over image quality.
### Describing an algorithm type
- [var description: String](./modelalgorithmtype/description.md)
  A text representation of the model parameters.
- [var debugDescription: String](./modelalgorithmtype/debugdescription.md)
  A text representation of the model parameters that’s suitable for output during debugging.
- [var playgroundDescription: Any](./modelalgorithmtype/playgrounddescription.md)
  A description of the model parameters shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./modelalgorithmtype/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](./modelalgorithmtype/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](./modelalgorithmtype/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../../Swift/customdebugstringconvertible.md)
- [CustomPlaygroundDisplayConvertible](../../../Swift/customplaygrounddisplayconvertible.md)
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Equatable](../../../Swift/equatable.md)
- [Escapable](../../../Swift/escapable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Describing parameters
- [MLStyleTransfer.ModelParameters.ValidationData](./validationdata.md)
  The source of a validation dataset for a style transfer model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlstyletransfer/modelparameters/modelalgorithmtype)*