# MLHandActionClassifier.ModelParameters

**Framework**: Create ML  
**Kind**: struct  
**Role**: Structure

A set of parameters that affect the training process of a hand action classifier task.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
struct ModelParameters
```

## Topics

### Creating hand action model parameters
- [init(validation: MLHandActionClassifier.ModelParameters.ValidationData, batchSize: Int, maximumIterations: Int, predictionWindowSize: Int, augmentationOptions: MLHandActionClassifier.VideoAugmentationOptions, algorithm: MLHandActionClassifier.ModelParameters.ModelAlgorithmType, targetFrameRate: Double)](./modelparameters-swift.struct/init%28validation,batchsize,maximumiterations,predictionwindowsize,augmentationoptions,algorithm,targetframerate%29.md)
  Creates a set of training session parameters for a hand action classifier task.
### Accessing hand action training parameters
- [var maximumIterations: Int](./modelparameters-swift.struct/maximumiterations.md)
  The largest number of training iterations you allow the training session to use.
- [var batchSize: Int](./modelparameters-swift.struct/batchsize.md)
  The number of videos the model training session uses for each training iteration.
- [var targetFrameRate: Double](./modelparameters-swift.struct/targetframerate.md)
  The number of video frames per second the hand action classifier model expects as its input at runtime.
- [var predictionWindowSize: Int](./modelparameters-swift.struct/predictionwindowsize.md)
  The number of video frames the model training session uses to train a hand action classifier.
- [var algorithm: MLHandActionClassifier.ModelParameters.ModelAlgorithmType](./modelparameters-swift.struct/algorithm.md)
  The algorithm the training session uses to create the hand action classifier.
- [var augmentationOptions: MLHandActionClassifier.VideoAugmentationOptions](./modelparameters-swift.struct/augmentationoptions.md)
  The variations the training session uses to add more variety to its training dataset.
- [var validation: MLHandActionClassifier.ModelParameters.ValidationData](./modelparameters-swift.struct/validation.md)
  A dataset the hand action classifier task uses to evaluate the model that’s distinct from the training dataset.
### Describing hand action model parameters
- [var description: String](./modelparameters-swift.struct/description.md)
  A text representation of the hand action parameters.
- [var debugDescription: String](./modelparameters-swift.struct/debugdescription.md)
  A text representation of the hand action parameters suitable for debugging.
- [var playgroundDescription: Any](./modelparameters-swift.struct/playgrounddescription.md)
  A description of the hand action parameters that’s viewable in a playground.
### Parameter supporting types
- [MLHandActionClassifier.VideoAugmentationOptions](./videoaugmentationoptions.md)
  Options a hand action classification training session can use to generate additional training data from the videos you provide.
- [MLHandActionClassifier.ModelParameters.ValidationData](./modelparameters-swift.struct/validationdata.md)
  A dataset a hand action classifier task uses to validate the model during a training session.
- [MLHandActionClassifier.ModelParameters.ModelAlgorithmType](./modelparameters-swift.struct/modelalgorithmtype.md)
  The hand action classifier training algorithm options.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./modelparameters-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](./modelparameters-swift.struct/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](./modelparameters-swift.struct/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomPlaygroundDisplayConvertible](../../Swift/customplaygrounddisplayconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Escapable](../../Swift/escapable.md)

## See Also

### Supporting types
- [MLHandActionClassifier.DataSource](./datasource.md)
  A hand action classifier dataset that contains annotated videos or hand joint location data.
- [MLHandActionClassifier.VideoAugmentationOptions](./videoaugmentationoptions.md)
  Options a hand action classification training session can use to generate additional training data from the videos you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/modelparameters-swift.struct)*