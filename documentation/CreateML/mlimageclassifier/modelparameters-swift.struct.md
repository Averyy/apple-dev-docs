# MLImageClassifier.ModelParameters

**Framework**: Create ML  
**Kind**: struct  
**Role**: Structure

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
- Provide your own validation dataset. See [`MLImageClassifier.ModelParameters.ValidationData`](./modelparameters-swift.struct/validationdata-swift.enum.md).
- Enable specific image augmentations. See [`MLImageClassifier.ImageAugmentationOptions`](./imageaugmentationoptions.md).
- Designate a custom feature extractor. See [`MLImageClassifier.FeatureExtractorType.custom(_:)`](./featureextractortype/custom%28_%29.md).

Once you configure an [`MLImageClassifier.ModelParameters`](./modelparameters-swift.struct.md) instance, use it to configure a training session with one of the applicable [`MLImageClassifier`](../mlimageclassifier.md) asynchronous type methods or synchronous initializers.

## Topics

### Creating parameters
- [init(validation: MLImageClassifier.ModelParameters.ValidationData, maxIterations: Int, augmentation: MLImageClassifier.ImageAugmentationOptions, algorithm: MLImageClassifier.ModelParameters.ModelAlgorithmType)](./modelparameters-swift.struct/init%28validation,maxiterations,augmentation,algorithm%29.md)
  Creates model training parameters.
- [init(featureExtractor: MLImageClassifier.FeatureExtractorType, validation: MLImageClassifier.ModelParameters.ValidationData, maxIterations: Int, augmentationOptions: MLImageClassifier.ImageAugmentationOptions)](./modelparameters-swift.struct/init%28featureextractor,validation,maxiterations,augmentationoptions%29.md)
  Creates a new set of training parameters for an image classifier with a validation dataset.
- [init(featureExtractor:validationData:maxIterations:augmentationOptions:)](./modelparameters-swift.struct/init%28featureextractor,validationdata,maxiterations,augmentationoptions%29.md)
  Creates a new set of image classifier parameters with validation data represented by a data source.
- [MLImageClassifier.ModelParameters.ClassifierType](./modelparameters-swift.struct/classifiertype.md)
  Type of classifier to be used.
- [MLImageClassifier.ModelParameters.ModelAlgorithmType](./modelparameters-swift.struct/modelalgorithmtype.md)
  The model algorithm to use for training an image classifier.
### Accessing the training parameters
- [var algorithm: MLImageClassifier.ModelParameters.ModelAlgorithmType](./modelparameters-swift.struct/algorithm.md)
  Model algorithm to be used
- [var featureExtractor: MLImageClassifier.FeatureExtractorType](./modelparameters-swift.struct/featureextractor.md)
  The underlying base model the training session uses to extract image features as it trains an image classifier.
- [var validation: MLImageClassifier.ModelParameters.ValidationData](./modelparameters-swift.struct/validation.md)
  The image classifier’s validation dataset.
- [var maxIterations: Int](./modelparameters-swift.struct/maxiterations.md)
  The maximum number of iterations the training session can use.
- [var augmentationOptions: MLImageClassifier.ImageAugmentationOptions](./modelparameters-swift.struct/augmentationoptions.md)
  The variations the training session uses to generate more variety in the training dataset.
- [var validationData: [String : [URL]]?](./modelparameters-swift.struct/validationdata-swift.property.md)
  A set of images that the training process uses for validation.
### Describing parameters
- [var description: String](./modelparameters-swift.struct/description.md)
  A text representation of the model parameters.
- [var debugDescription: String](./modelparameters-swift.struct/debugdescription.md)
  A text representation of the model parameters that’s suitable for output during debugging.
- [var playgroundDescription: Any](./modelparameters-swift.struct/playgrounddescription.md)
  A description of the model parameters shown in a playground.
### Supporting types
- [MLImageClassifier.FeatureExtractorType](./featureextractortype.md)
  The underlying base model that extracts image features for image classifier training session.
- [MLImageClassifier.ModelParameters.ValidationData](./modelparameters-swift.struct/validationdata-swift.enum.md)
  The source of a validation dataset for an image classifier.
- [MLImageClassifier.ImageAugmentationOptions](./imageaugmentationoptions.md)
  The variations that the training process can use to generate more training data from the training data you provide.
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
- [MLImageClassifier.DataSource](./datasource.md)
  A data source for an image classifier.
- [MLImageClassifier.FeatureExtractorType](./featureextractortype.md)
  The underlying base model that extracts image features for image classifier training session.
- [MLImageClassifier.CustomFeatureExtractor](./customfeatureextractor.md)
  A custom feature extractor a training session uses to train an image classifier.
- [MLImageClassifier.ImageAugmentationOptions](./imageaugmentationoptions.md)
  The variations that the training process can use to generate more training data from the training data you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/modelparameters-swift.struct)*