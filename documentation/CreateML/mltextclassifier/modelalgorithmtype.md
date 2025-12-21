# MLTextClassifier.ModelAlgorithmType

**Framework**: Create ML  
**Kind**: enum

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

- [Creating a text classifier model](creating-a-text-classifier-model.md)
- [Improving Your Model’s Accuracy](improving-your-model-s-accuracy.md)

#### Overview

Typically, `maxEnt` is the fastest training algorithm. If the text classifier’s performance isn’t good enough, consider the `transferLearning` algorithm.

## Topics

### Selecting an algorithm type
- [MLTextClassifier.ModelAlgorithmType.crf(revision:)](mltextclassifier/modelalgorithmtype/crf(revision:).md)
  A text classification algorithm that uses a statistical model of transition probabilities between words.
- [MLTextClassifier.ModelAlgorithmType.maxEnt(revision:)](mltextclassifier/modelalgorithmtype/maxent(revision:).md)
  A text classification algorithm that uses multinomial logistic regression based on the frequencies of words, independent of context.
- [case transferLearning(MLTextClassifier.FeatureExtractorType, revision: Int?)](mltextclassifier/modelalgorithmtype/transferlearning(_:revision:).md)
  A text classification algorithm that uses transfer learning by leveraging a feature extractor to generate embeddings.
- [MLTextClassifier.FeatureExtractorType](mltextclassifier/featureextractortype.md)
  The text feature extractor type.
### Describing an algorithm type
- [var description: String](mltextclassifier/modelalgorithmtype/description.md)
  A text representation of the algorithm type.
- [var debugDescription: String](mltextclassifier/modelalgorithmtype/debugdescription.md)
  A text representation of the algorithm type that’s suitable for output during debugging.
- [var playgroundDescription: Any](mltextclassifier/modelalgorithmtype/playgrounddescription.md)
  A description of the algorithm type shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mltextclassifier/modelalgorithmtype/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mltextclassifier/modelalgorithmtype/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mltextclassifier/modelalgorithmtype/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [MLTextClassifier.FeatureExtractorType](mltextclassifier/featureextractortype.md)
  The text feature extractor type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/modelalgorithmtype)*