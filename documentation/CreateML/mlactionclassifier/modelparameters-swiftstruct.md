# MLActionClassifier.ModelParameters

**Framework**: Create ML  
**Kind**: struct

Parameters that affect the training process of an action classifier.

**Availability**:
- macOS 11.0+

## Declaration

```swift
struct ModelParameters
```

## Topics

### Creating action classifier parameters
- [init(validation: MLActionClassifier.ModelParameters.ValidationData, batchSize: Int, maximumIterations: Int, predictionWindowSize: Int, augmentationOptions: MLActionClassifier.VideoAugmentationOptions, algorithm: MLActionClassifier.ModelParameters.ModelAlgorithmType, targetFrameRate: Double)](mlactionclassifier/modelparameters-swift.struct/init(validation:batchsize:maximumiterations:predictionwindowsize:augmentationoptions:algorithm:targetframerate:).md)
  Creates a new set of training parameters for an action classifier with the validation dataset.
### Accessing the training parameters
- [var maximumIterations: Int](mlactionclassifier/modelparameters-swift.struct/maximumiterations.md)
  The largest number of training iterations the training session can use.
- [var batchSize: Int](mlactionclassifier/modelparameters-swift.struct/batchsize.md)
  The number of videos the training session uses for each of its training iterations.
- [var targetFrameRate: Double](mlactionclassifier/modelparameters-swift.struct/targetframerate.md)
  The number of frames the training session uses per second of video to train an action classifier.
- [var predictionWindowSize: Int](mlactionclassifier/modelparameters-swift.struct/predictionwindowsize.md)
  The number of frames the training session uses to train an action classifier.
- [var algorithm: MLActionClassifier.ModelParameters.ModelAlgorithmType](mlactionclassifier/modelparameters-swift.struct/algorithm.md)
  The algorithm the training session uses to train the action classifier.
- [var augmentationOptions: MLActionClassifier.VideoAugmentationOptions](mlactionclassifier/modelparameters-swift.struct/augmentationoptions.md)
  The variations the training session uses to generate more variety in the training dataset.
- [var validation: MLActionClassifier.ModelParameters.ValidationData](mlactionclassifier/modelparameters-swift.struct/validation.md)
  The action classifier’s validation dataset.
### Describing the model parameters
- [var description: String](mlactionclassifier/modelparameters-swift.struct/description.md)
  A text representation of the model parameters.
- [var debugDescription: String](mlactionclassifier/modelparameters-swift.struct/debugdescription.md)
  A text representation of the model parameters that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlactionclassifier/modelparameters-swift.struct/playgrounddescription.md)
  A description of the model parameters shown in a playground.
### Supporting types
- [MLActionClassifier.ModelParameters.ValidationData](mlactionclassifier/modelparameters-swift.struct/validationdata.md)
  The source of a validation dataset for an action classifier.
- [MLActionClassifier.VideoAugmentationOptions](mlactionclassifier/videoaugmentationoptions.md)
  The video augmentations for an action classifier training session.
- [MLActionClassifier.ModelParameters.ModelAlgorithmType](mlactionclassifier/modelparameters-swift.struct/modelalgorithmtype.md)
  The action classifier training algorithm options.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlactionclassifier/modelparameters-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlactionclassifier/modelparameters-swift.struct/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlactionclassifier/modelparameters-swift.struct/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [MLActionClassifier.DataSource](mlactionclassifier/datasource.md)
  A data source for an action classifier.
- [MLActionClassifier.VideoAugmentationOptions](mlactionclassifier/videoaugmentationoptions.md)
  The video augmentations for an action classifier training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/modelparameters-swift.struct)*