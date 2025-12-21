# MLImageClassifier.ModelParameters.ClassifierType

**Framework**: Create ML  
**Kind**: enum

Type of classifier to be used.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum ClassifierType
```

## Topics

### Designating an algorithm’s classifier
- [MLImageClassifier.ModelParameters.ClassifierType.logisticRegressor](mlimageclassifier/modelparameters-swift.struct/classifiertype/logisticregressor.md)
  Logistic regression is a statistical model that classifies input feature vector into different categories.
- [MLImageClassifier.ModelParameters.ClassifierType.multilayerPerceptron(layerSizes:)](mlimageclassifier/modelparameters-swift.struct/classifiertype/multilayerperceptron(layersizes:).md)
  Multilayer perceptron, layerSizes holds a list of positive integers that represent the number of hidden units in each layer. An additional fully connected layer with a Softmax activation output will be added that maps to probabilities of sound categories.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(validation: MLImageClassifier.ModelParameters.ValidationData, maxIterations: Int, augmentation: MLImageClassifier.ImageAugmentationOptions, algorithm: MLImageClassifier.ModelParameters.ModelAlgorithmType)](mlimageclassifier/modelparameters-swift.struct/init(validation:maxiterations:augmentation:algorithm:).md)
  Creates model training parameters.
- [init(featureExtractor: MLImageClassifier.FeatureExtractorType, validation: MLImageClassifier.ModelParameters.ValidationData, maxIterations: Int, augmentationOptions: MLImageClassifier.ImageAugmentationOptions)](mlimageclassifier/modelparameters-swift.struct/init(featureextractor:validation:maxiterations:augmentationoptions:).md)
  Creates a new set of training parameters for an image classifier with a validation dataset.
- [init(featureExtractor:validationData:maxIterations:augmentationOptions:)](mlimageclassifier/modelparameters-swift.struct/init(featureextractor:validationdata:maxiterations:augmentationoptions:).md)
  Creates a new set of image classifier parameters with validation data represented by a data source.
- [MLImageClassifier.ModelParameters.ModelAlgorithmType](mlimageclassifier/modelparameters-swift.struct/modelalgorithmtype.md)
  The model algorithm to use for training an image classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/modelparameters-swift.struct/classifiertype)*