# MLImageClassifier.ModelParameters

**Framework**: Create ML  
**Kind**: struct

Parameters that affect the process of training an image classifier model.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
struct ModelParameters
```

#### Overview

Use this structure to configure the model training session. With it you can:

- Set a limit to the number of training iterations the session can use
- Provide your own validation dataset. See [`MLImageClassifier.ModelParameters.ValidationData`](mlimageclassifier/modelparameters-swift.struct/validationdata-swift.enum.md).
- Enable specific image augmentations. See [`MLImageClassifier.ImageAugmentationOptions`](mlimageclassifier/imageaugmentationoptions.md).
- Designate a custom feature extractor. See [`MLImageClassifier.FeatureExtractorType.custom(_:)`](mlimageclassifier/featureextractortype/custom(_:).md).

Once you configure an [`MLImageClassifier.ModelParameters`](mlimageclassifier/modelparameters-swift.struct.md) instance, use it to configure a training session with one of the applicable [`MLImageClassifier`](mlimageclassifier.md) asynchronous type methods or synchronous initializers.

## Topics

### Creating parameters
- [init(validation: MLImageClassifier.ModelParameters.ValidationData, maxIterations: Int, augmentation: MLImageClassifier.ImageAugmentationOptions, algorithm: MLImageClassifier.ModelParameters.ModelAlgorithmType)](mlimageclassifier/modelparameters-swift.struct/init(validation:maxiterations:augmentation:algorithm:).md)
  Creates model training parameters.
- [init(featureExtractor: MLImageClassifier.FeatureExtractorType, validation: MLImageClassifier.ModelParameters.ValidationData, maxIterations: Int, augmentationOptions: MLImageClassifier.ImageAugmentationOptions)](mlimageclassifier/modelparameters-swift.struct/init(featureextractor:validation:maxiterations:augmentationoptions:).md)
  Creates a new set of training parameters for an image classifier with a validation dataset.
- [init(featureExtractor: MLImageClassifier.FeatureExtractorType, validationData: MLImageClassifier.DataSource, maxIterations: Int, augmentationOptions: MLImageClassifier.ImageAugmentationOptions)](mlimageclassifier/modelparameters-swift.struct/init(featureextractor:validationdata:maxiterations:augmentationoptions:)-42gf1.md)
  Creates a new set of image classifier parameters with validation data represented by a data source.
- [init(featureExtractor: MLImageClassifier.FeatureExtractorType, validationData: [String : [URL]]?, maxIterations: Int, augmentationOptions: MLImageClassifier.ImageAugmentationOptions)](mlimageclassifier/modelparameters-swift.struct/init(featureextractor:validationdata:maxiterations:augmentationoptions:)-5we70.md)
  Creates a new set of image classifier parameters with validation data represented by a dictionary.
- [MLImageClassifier.ModelParameters.ClassifierType](mlimageclassifier/modelparameters-swift.struct/classifiertype.md)
  Type of classifier to be used.
- [MLImageClassifier.ModelParameters.ModelAlgorithmType](mlimageclassifier/modelparameters-swift.struct/modelalgorithmtype.md)
  The model algorithm to use for training an image classifier.
### Accessing the training parameters
- [var algorithm: MLImageClassifier.ModelParameters.ModelAlgorithmType](mlimageclassifier/modelparameters-swift.struct/algorithm.md)
  Model algorithm to be used
- [var featureExtractor: MLImageClassifier.FeatureExtractorType](mlimageclassifier/modelparameters-swift.struct/featureextractor.md)
  The underlying base model the training session uses to extract image features as it trains an image classifier.
- [var validation: MLImageClassifier.ModelParameters.ValidationData](mlimageclassifier/modelparameters-swift.struct/validation.md)
  The image classifier’s validation dataset.
- [var maxIterations: Int](mlimageclassifier/modelparameters-swift.struct/maxiterations.md)
  The maximum number of iterations the training session can use.
- [var augmentationOptions: MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/modelparameters-swift.struct/augmentationoptions.md)
  The variations the training session uses to generate more variety in the training dataset.
- [var validationData: [String : [URL]]?](mlimageclassifier/modelparameters-swift.struct/validationdata-swift.property.md)
  A set of images that the training process uses for validation.
### Describing parameters
- [var description: String](mlimageclassifier/modelparameters-swift.struct/description.md)
  A text representation of the model parameters.
- [var debugDescription: String](mlimageclassifier/modelparameters-swift.struct/debugdescription.md)
  A text representation of the model parameters that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlimageclassifier/modelparameters-swift.struct/playgrounddescription.md)
  A description of the model parameters shown in a playground.
### Supporting types
- [MLImageClassifier.FeatureExtractorType](mlimageclassifier/featureextractortype.md)
  The underlying base model that extracts image features for image classifier training session.
- [MLImageClassifier.ModelParameters.ValidationData](mlimageclassifier/modelparameters-swift.struct/validationdata-swift.enum.md)
  The source of a validation dataset for an image classifier.
- [MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions.md)
  The variations that the training process can use to generate more training data from the training data you provide.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlimageclassifier/modelparameters-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlimageclassifier/modelparameters-swift.struct/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlimageclassifier/modelparameters-swift.struct/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [static func train(trainingData: MLActionClassifier.DataSource, parameters: MLActionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLActionClassifier>](mlactionclassifier/train(trainingdata:parameters:sessionparameters:).md)
  Begins an asynchronous action classifier training session.
- [init(trainingData: MLImageClassifier.DataSource, parameters: MLImageClassifier.ModelParameters) throws](mlimageclassifier/init(trainingdata:parameters:)-4r6hr.md)
  Creates an image classifier with a training dataset represented by a data source.
- [init(trainingData: [String : [URL]], parameters: MLImageClassifier.ModelParameters) throws](mlimageclassifier/init(trainingdata:parameters:)-7j4w6.md)
  Creates an image classifier with a training dataset represented by a dictionary.
- [MLImageClassifier.DataSource](mlimageclassifier/datasource.md)
  A data source for an image classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/modelparameters-swift.struct)*