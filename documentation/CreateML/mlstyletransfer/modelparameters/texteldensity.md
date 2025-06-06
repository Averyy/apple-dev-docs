# textelDensity

**Framework**: Create ML  
**Kind**: property

The amount of detail the task applies from the input style image to the stylized image output.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var textelDensity: Int
```

#### Discussion

The value must be a multiple of `4` in the range `[64, 1024]`. The style transfer task converts all other values to the nearest multiple of `4` less than the value.

## See Also

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
- [var validation: MLStyleTransfer.ModelParameters.ValidationData](mlstyletransfer/modelparameters/validation.md)
  The style transfer model’s validation dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlstyletransfer/modelparameters/texteldensity)*