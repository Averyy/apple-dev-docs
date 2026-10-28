# MLTextClassifier.ModelAlgorithmType

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

The type of algorithm that a text classifier uses.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
enum ModelAlgorithmType
```

## Mentions

- [Creating a text classifier model](../creating-a-text-classifier-model.md)
- [Improving Your Model’s Accuracy](../improving-your-model-s-accuracy.md)

## Overview

Typically, `maxEnt` is the fastest training algorithm. If the text classifier’s performance isn’t good enough, consider the `transferLearning` algorithm.

## Topics

### Selecting an algorithm type
- [MLTextClassifier.ModelAlgorithmType.crf(revision:)](./modelalgorithmtype/crf%28revision%29.md)
  A text classification algorithm that uses a statistical model of transition probabilities between words.
- [MLTextClassifier.ModelAlgorithmType.maxEnt(revision:)](./modelalgorithmtype/maxent%28revision%29.md)
  A text classification algorithm that uses multinomial logistic regression based on the frequencies of words, independent of context.
- [case transferLearning(MLTextClassifier.FeatureExtractorType, revision: Int?)](./modelalgorithmtype/transferlearning%28_,revision%29.md)
  A text classification algorithm that uses transfer learning by leveraging a feature extractor to generate embeddings.
- [MLTextClassifier.FeatureExtractorType](./featureextractortype.md)
  The text feature extractor type.
### Describing an algorithm type
- [var description: String](./modelalgorithmtype/description.md)
  A text representation of the algorithm type.
- [var debugDescription: String](./modelalgorithmtype/debugdescription.md)
  A text representation of the algorithm type that’s suitable for output during debugging.
- [var playgroundDescription: Any](./modelalgorithmtype/playgrounddescription.md)
  A description of the algorithm type shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./modelalgorithmtype/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](./modelalgorithmtype/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](./modelalgorithmtype/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomPlaygroundDisplayConvertible](../../Swift/customplaygrounddisplayconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [MLTextClassifier.FeatureExtractorType](./featureextractortype.md)
  The text feature extractor type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/modelalgorithmtype)*