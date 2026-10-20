# MLStyleTransfer.ModelParameters

**Framework**: Create ML  
**Kind**: struct  
**Role**: Structure

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
- [init(algorithm: MLStyleTransfer.ModelParameters.ModelAlgorithmType, validation: MLStyleTransfer.ModelParameters.ValidationData, maxIterations: Int, textelDensity: Int, styleStrength: Int)](./modelparameters/init%28algorithm,validation,maxiterations,texteldensity,stylestrength%29.md)
  Creates a new set of training parameters for a style transfer model.
### Setting style transfer parameters
- [var algorithm: MLStyleTransfer.ModelParameters.ModelAlgorithmType](./modelparameters/algorithm.md)
  The style transfer task’s training algorithm that prioritizes either speed or quality.
- [var debugDescription: String](./modelparameters/debugdescription.md)
  A text representation of the style transfer model parameters that’s suitable for output during debugging.
- [var description: String](./modelparameters/description.md)
  A text representation of the style transfer model parameters.
- [var maxIterations: Int](./modelparameters/maxiterations.md)
  The largest number of iterations the style transfer model can use during training.
- [var playgroundDescription: Any](./modelparameters/playgrounddescription.md)
  A description of the style transfer model parameters shown in a playground.
- [var styleStrength: Int](./modelparameters/stylestrength.md)
  The amount of influence the input style image has in the stylized image output.
- [var textelDensity: Int](./modelparameters/texteldensity.md)
  The amount of detail the task applies from the input style image to the stylized image output.
- [var validation: MLStyleTransfer.ModelParameters.ValidationData](./modelparameters/validation.md)
  The style transfer model’s validation dataset.
### Describing parameters
- [MLStyleTransfer.ModelParameters.ModelAlgorithmType](./modelparameters/modelalgorithmtype.md)
  The style transfer training algorithm options.
- [MLStyleTransfer.ModelParameters.ValidationData](./modelparameters/validationdata.md)
  The source of a validation dataset for a style transfer model.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./modelparameters/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](./modelparameters/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](./modelparameters/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomPlaygroundDisplayConvertible](../../Swift/customplaygrounddisplayconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [MLStyleTransfer.DataSource](./datasource.md)
  A data source for a style transfer model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlstyletransfer/modelparameters)*