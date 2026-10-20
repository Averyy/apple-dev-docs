# styleStrength

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

The amount of influence the input style image has in the stylized image output.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var styleStrength: Int
```

#### Discussion

This parameter’s value must be in the range `[1, 10]`. Higher numbers apply more of the style image than the content image.

## See Also

### Setting style transfer parameters
- [var algorithm: MLStyleTransfer.ModelParameters.ModelAlgorithmType](./algorithm.md)
  The style transfer task’s training algorithm that prioritizes either speed or quality.
- [var debugDescription: String](./debugdescription.md)
  A text representation of the style transfer model parameters that’s suitable for output during debugging.
- [var description: String](./description.md)
  A text representation of the style transfer model parameters.
- [var maxIterations: Int](./maxiterations.md)
  The largest number of iterations the style transfer model can use during training.
- [var playgroundDescription: Any](./playgrounddescription.md)
  A description of the style transfer model parameters shown in a playground.
- [var textelDensity: Int](./texteldensity.md)
  The amount of detail the task applies from the input style image to the stylized image output.
- [var validation: MLStyleTransfer.ModelParameters.ValidationData](./validation.md)
  The style transfer model’s validation dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlstyletransfer/modelparameters/stylestrength)*