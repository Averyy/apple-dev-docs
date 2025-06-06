# algorithm

**Framework**: Create ML  
**Kind**: property

The style transfer task’s training algorithm that prioritizes either speed or quality.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var algorithm: MLStyleTransfer.ModelParameters.ModelAlgorithmType
```

#### Discussion

You choose the task’s training algorithm based on your intended use for this model.

Use [`MLStyleTransfer.ModelParameters.ModelAlgorithmType.cnnLite`](mlstyletransfer/modelparameters/modelalgorithmtype/cnnlite.md) to train a model that prioritizes speed to stylize images with low latency, typically for frames of a video stream. Otherwise, select [`MLStyleTransfer.ModelParameters.ModelAlgorithmType.cnn`](mlstyletransfer/modelparameters/modelalgorithmtype/cnn.md) to train a model that applies a higher-quality stylization, typically for a still image.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlstyletransfer/modelparameters/algorithm)*