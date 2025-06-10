# MLSoundClassifier.ModelParameters.ClassifierType

**Framework**: Create ML  
**Kind**: enum

The classifier options for a sound classifier training algorithm.

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
- [MLSoundClassifier.ModelParameters.ClassifierType.logisticRegressor](mlsoundclassifier/modelparameters-swift.struct/classifiertype/logisticregressor.md)
  A statistical model that uses logistic regression to classify an input vector into a category.
- [MLSoundClassifier.ModelParameters.ClassifierType.multilayerPerceptron(layerSizes:)](mlsoundclassifier/modelparameters-swift.struct/classifiertype/multilayerperceptron(layersizes:).md)
  A neural network model that uses three or more layers to classify an input into a category.
### Describing a classifier type
- [var description: String](mlsoundclassifier/modelparameters-swift.struct/classifiertype/description.md)
  A text representation of the classifier type.
### Comparing a classifier type
- [static func == (MLSoundClassifier.ModelParameters.ClassifierType, MLSoundClassifier.ModelParameters.ClassifierType) -> Bool](mlsoundclassifier/modelparameters-swift.struct/classifiertype/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](mlsoundclassifier/modelparameters-swift.struct/classifiertype/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Instance Properties
- [var hashValue: Int](mlsoundclassifier/modelparameters-swift.struct/classifiertype/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](mlsoundclassifier/modelparameters-swift.struct/classifiertype/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](mlsoundclassifier/modelparameters-swift.struct/classifiertype/equatable-implementations.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case transferLearning(featureExtractor: MLSoundClassifier.ModelParameters.FeatureExtractorType, classifier: MLSoundClassifier.ModelParameters.ClassifierType)](mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype/transferlearning(featureextractor:classifier:).md)
  An algorithm that leverages the knowledge of a general-purpose model built into the operating system.
- [MLSoundClassifier.ModelParameters.FeatureExtractorType](mlsoundclassifier/modelparameters-swift.struct/featureextractortype.md)
  The feature-extractor options for a sound-classifier training algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/classifiertype)*