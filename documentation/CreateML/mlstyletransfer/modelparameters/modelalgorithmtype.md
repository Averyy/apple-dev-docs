# MLStyleTransfer.ModelParameters.ModelAlgorithmType

**Framework**: Create ML  
**Kind**: enum

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
- [MLStyleTransfer.ModelParameters.ModelAlgorithmType.cnn](mlstyletransfer/modelparameters/modelalgorithmtype/cnn.md)
  A style-transfer training algorithm that generates a model that prioritizes image quality over speed.
- [MLStyleTransfer.ModelParameters.ModelAlgorithmType.cnnLite](mlstyletransfer/modelparameters/modelalgorithmtype/cnnlite.md)
  A style-transfer training algorithm that generates a model that prioritizes speed over image quality.
### Describing an algorithm type
- [var description: String](mlstyletransfer/modelparameters/modelalgorithmtype/description.md)
  A text representation of the model parameters.
- [var debugDescription: String](mlstyletransfer/modelparameters/modelalgorithmtype/debugdescription.md)
  A text representation of the model parameters that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlstyletransfer/modelparameters/modelalgorithmtype/playgrounddescription.md)
  A description of the model parameters shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlstyletransfer/modelparameters/modelalgorithmtype/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlstyletransfer/modelparameters/modelalgorithmtype/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlstyletransfer/modelparameters/modelalgorithmtype/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [MLStyleTransfer.ModelParameters.ValidationData](mlstyletransfer/modelparameters/validationdata.md)
  The source of a validation dataset for a style transfer model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlstyletransfer/modelparameters/modelalgorithmtype)*