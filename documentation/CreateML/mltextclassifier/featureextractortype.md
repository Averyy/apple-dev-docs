# MLTextClassifier.FeatureExtractorType

**Framework**: Create ML  
**Kind**: enum

The text feature extractor type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
enum FeatureExtractorType
```

## Topics

### Selecting a feature extractor type
- [MLTextClassifier.FeatureExtractorType.customEmbedding(_:)](mltextclassifier/featureextractortype/customembedding(_:).md)
  A feature extractor that uses a custom embedding contained in a CoreML model file.
- [MLTextClassifier.FeatureExtractorType.staticEmbedding](mltextclassifier/featureextractortype/staticembedding.md)
  A feature extractor that uses the standard, built-in word embeddings.
- [MLTextClassifier.FeatureExtractorType.bertEmbedding](mltextclassifier/featureextractortype/bertembedding.md)
  A feature extractor that provides BERT contextual word embeddings.
- [MLTextClassifier.FeatureExtractorType.elmoEmbedding](mltextclassifier/featureextractortype/elmoembedding.md)
  A feature extractor that provides ELMo contextual word embeddings.
- [MLTextClassifier.FeatureExtractorType.dynamicEmbedding](mltextclassifier/featureextractortype/dynamicembedding.md)
  A feature extractor that provides embeddings for words, based on their in-context use.
### Describing a feature extractor type
- [var description: String](mltextclassifier/featureextractortype/description.md)
  A text representation of a feature extractor type.
- [var debugDescription: String](mltextclassifier/featureextractortype/debugdescription.md)
  A text representation of the feature extractor type that’s suitable for output during debugging.
- [var playgroundDescription: Any](mltextclassifier/featureextractortype/playgrounddescription.md)
  A description of the feature extractor type shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mltextclassifier/featureextractortype/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mltextclassifier/featureextractortype/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mltextclassifier/featureextractortype/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [MLTextClassifier.ModelAlgorithmType.crf(revision:)](mltextclassifier/modelalgorithmtype/crf(revision:).md)
  A text classification algorithm that uses a statistical model of transition probabilities between words.
- [MLTextClassifier.ModelAlgorithmType.maxEnt(revision:)](mltextclassifier/modelalgorithmtype/maxent(revision:).md)
  A text classification algorithm that uses multinomial logistic regression based on the frequencies of words, independent of context.
- [case transferLearning(MLTextClassifier.FeatureExtractorType, revision: Int?)](mltextclassifier/modelalgorithmtype/transferlearning(_:revision:).md)
  A text classification algorithm that uses transfer learning by leveraging a feature extractor to generate embeddings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/featureextractortype)*