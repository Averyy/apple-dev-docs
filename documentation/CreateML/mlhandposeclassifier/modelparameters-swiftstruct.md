# MLHandPoseClassifier.ModelParameters

**Framework**: Create ML  
**Kind**: struct

A set of parameters that affect the training process of a hand pose classifier task.

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

### Creating hand pose model parameters
- [init(validation: MLHandPoseClassifier.ModelParameters.ValidationData, batchSize: Int, maximumIterations: Int, augmentationOptions: MLHandPoseClassifier.ImageAugmentationOptions, algorithm: MLHandPoseClassifier.ModelParameters.ModelAlgorithmType)](mlhandposeclassifier/modelparameters-swift.struct/init(validation:batchsize:maximumiterations:augmentationoptions:algorithm:).md)
  Creates a set of training session parameters for a hand pose classifier task.
### Accessing hand pose training parameters
- [var maximumIterations: Int](mlhandposeclassifier/modelparameters-swift.struct/maximumiterations.md)
  The largest number of training iterations you allow the training session to use.
- [var batchSize: Int](mlhandposeclassifier/modelparameters-swift.struct/batchsize.md)
  The number of images the model training session uses for each training iteration.
- [var algorithm: MLHandPoseClassifier.ModelParameters.ModelAlgorithmType](mlhandposeclassifier/modelparameters-swift.struct/algorithm.md)
  The algorithm the training session uses to create the hand pose classifier.
- [var augmentationOptions: MLHandPoseClassifier.ImageAugmentationOptions](mlhandposeclassifier/modelparameters-swift.struct/augmentationoptions.md)
  The variations the training session uses to add more variety to its training dataset.
- [var validation: MLHandPoseClassifier.ModelParameters.ValidationData](mlhandposeclassifier/modelparameters-swift.struct/validation.md)
  A dataset the hand pose classifier task uses to evaluate the model that’s distinct from the training dataset.
### Describing hand pose model parameters
- [var description: String](mlhandposeclassifier/modelparameters-swift.struct/description.md)
  A text representation of the hand pose parameters.
- [var debugDescription: String](mlhandposeclassifier/modelparameters-swift.struct/debugdescription.md)
  A text representation of the hand pose parameters suitable for debugging.
- [var playgroundDescription: Any](mlhandposeclassifier/modelparameters-swift.struct/playgrounddescription.md)
  A description of the hand pose parameters that’s viewable in a playground.
### Parameter supporting types
- [MLHandPoseClassifier.ImageAugmentationOptions](mlhandposeclassifier/imageaugmentationoptions.md)
  Options a hand pose classification training session can use to generate additional training data from the images you provide.
- [MLHandPoseClassifier.ModelParameters.ValidationData](mlhandposeclassifier/modelparameters-swift.struct/validationdata.md)
  A dataset a hand pose classifier task uses to validate the model during a training session.
- [MLHandPoseClassifier.ModelParameters.ModelAlgorithmType](mlhandposeclassifier/modelparameters-swift.struct/modelalgorithmtype.md)
  The hand pose classifier training algorithm options.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlhandposeclassifier/modelparameters-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlhandposeclassifier/modelparameters-swift.struct/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlhandposeclassifier/modelparameters-swift.struct/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [MLHandPoseClassifier.DataSource](mlhandposeclassifier/datasource.md)
  A hand pose classifier dataset that contains annotated images or hand joint location data.
- [MLHandPoseClassifier.ImageAugmentationOptions](mlhandposeclassifier/imageaugmentationoptions.md)
  Options a hand pose classification training session can use to generate additional training data from the images you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/modelparameters-swift.struct)*