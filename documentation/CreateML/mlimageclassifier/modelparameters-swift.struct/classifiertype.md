# MLImageClassifier.ModelParameters.ClassifierType

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

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
- [MLImageClassifier.ModelParameters.ClassifierType.logisticRegressor](./classifiertype/logisticregressor.md)
  Logistic regression is a statistical model that classifies input feature vector into different categories.
- [MLImageClassifier.ModelParameters.ClassifierType.multilayerPerceptron(layerSizes:)](./classifiertype/multilayerperceptron%28layersizes%29.md)
  Multilayer perceptron, layerSizes holds a list of positive integers that represent the number of hidden units in each layer. An additional fully connected layer with a Softmax activation output will be added that maps to probabilities of sound categories.

## Relationships

### Conforms To
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Creating parameters
- [init(validation: MLImageClassifier.ModelParameters.ValidationData, maxIterations: Int, augmentation: MLImageClassifier.ImageAugmentationOptions, algorithm: MLImageClassifier.ModelParameters.ModelAlgorithmType)](./init%28validation,maxiterations,augmentation,algorithm%29.md)
  Creates model training parameters.
- [init(featureExtractor: MLImageClassifier.FeatureExtractorType, validation: MLImageClassifier.ModelParameters.ValidationData, maxIterations: Int, augmentationOptions: MLImageClassifier.ImageAugmentationOptions)](./init%28featureextractor,validation,maxiterations,augmentationoptions%29.md)
  Creates a new set of training parameters for an image classifier with a validation dataset.
- [init(featureExtractor:validationData:maxIterations:augmentationOptions:)](./init%28featureextractor,validationdata,maxiterations,augmentationoptions%29.md)
  Creates a new set of image classifier parameters with validation data represented by a data source.
- [MLImageClassifier.ModelParameters.ModelAlgorithmType](./modelalgorithmtype.md)
  The model algorithm to use for training an image classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/modelparameters-swift.struct/classifiertype)*