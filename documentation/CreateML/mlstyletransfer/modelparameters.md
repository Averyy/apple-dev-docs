# MLStyleTransfer.ModelParameters

**Framework**: Create ML  
**Kind**: struct

Parameters that affect the training process of a style transfer model.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct ModelParameters
```

## Topics

### Creating parameters
- [init(algorithm: MLStyleTransfer.ModelParameters.ModelAlgorithmType, validation: MLStyleTransfer.ModelParameters.ValidationData, maxIterations: Int, textelDensity: Int, styleStrength: Int)](mlstyletransfer/modelparameters/init(algorithm:validation:maxiterations:texteldensity:stylestrength:).md)
  Creates a new set of training parameters for a style transfer model.
### Setting style transfer parameters
- [var algorithm: MLStyleTransfer.ModelParameters.ModelAlgorithmType](mlstyletransfer/modelparameters/algorithm.md)
  The style transfer task’s training algorithm that prioritizes either speed or quality.
- [var debugDescription: String](mlstyletransfer/modelparameters/debugdescription.md)
  A text representation of the style transfer model parameters that’s suitable for output during debugging.
- [var description: String](mlstyletransfer/modelparameters/description.md)
  A text representation of the style transfer model parameters.
- [var maxIterations: Int](mlstyletransfer/modelparameters/maxiterations.md)
  The largest number of iterations the style transfer model can use during training.
- [var playgroundDescription: Any](mlstyletransfer/modelparameters/playgrounddescription.md)
  A description of the style transfer model parameters shown in a playground.
- [var styleStrength: Int](mlstyletransfer/modelparameters/stylestrength.md)
  The amount of influence the input style image has in the stylized image output.
- [var textelDensity: Int](mlstyletransfer/modelparameters/texteldensity.md)
  The amount of detail the task applies from the input style image to the stylized image output.
- [var validation: MLStyleTransfer.ModelParameters.ValidationData](mlstyletransfer/modelparameters/validation.md)
  The style transfer model’s validation dataset.
### Describing parameters
- [MLStyleTransfer.ModelParameters.ModelAlgorithmType](mlstyletransfer/modelparameters/modelalgorithmtype.md)
  The style transfer training algorithm options.
- [MLStyleTransfer.ModelParameters.ValidationData](mlstyletransfer/modelparameters/validationdata.md)
  The source of a validation dataset for a style transfer model.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlstyletransfer/modelparameters/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlstyletransfer/modelparameters/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlstyletransfer/modelparameters/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [MLStyleTransfer.DataSource](mlstyletransfer/datasource.md)
  A data source for a style transfer model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlstyletransfer/modelparameters)*