# MLWordTagger.FeatureExtractorType

**Framework**: Create ML  
**Kind**: enum

The feature extractors that are available to train a word tagger using with the transfer-learning algorithm option.

**Availability**:
- macOS 11.0+

## Declaration

```swift
enum FeatureExtractorType
```

## Topics

### Selecting a feature extractor type
- [MLWordTagger.FeatureExtractorType.bertEmbedding](mlwordtagger/featureextractortype/bertembedding.md)
  A feature extractor that provides BERT contextual word embeddings.
- [MLWordTagger.FeatureExtractorType.elmoEmbedding](mlwordtagger/featureextractortype/elmoembedding.md)
  A feature extractor that provides ELMo contextual word embeddings.
- [MLWordTagger.FeatureExtractorType.dynamicEmbedding](mlwordtagger/featureextractortype/dynamicembedding.md)
  A feature extractor that provides embeddings for words, based on their in-context use.
### Describing a feature extractor type
- [var description: String](mlwordtagger/featureextractortype/description.md)
  A text representation of a feature extractor type.
- [var debugDescription: String](mlwordtagger/featureextractortype/debugdescription.md)
  A text representation of the feature extractor that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlwordtagger/featureextractortype/playgrounddescription.md)
  A description of the feature extractor in a playground.
### Comparing feature extractors
- [static func == (MLWordTagger.FeatureExtractorType, MLWordTagger.FeatureExtractorType) -> Bool](mlwordtagger/featureextractortype/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](mlwordtagger/featureextractortype/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Accessing the hash value
- [func hash(into: inout Hasher)](mlwordtagger/featureextractortype/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](mlwordtagger/featureextractortype/hashvalue.md)
  The hash value.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlwordtagger/featureextractortype/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlwordtagger/featureextractortype/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlwordtagger/featureextractortype/customstringconvertible-implementations.md)
- [Equatable Implementations](mlwordtagger/featureextractortype/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [MLWordTagger.ModelAlgorithmType.crf(revision:)](mlwordtagger/modelalgorithmtype/crf(revision:).md)
  A conditional random field algorithm.
- [case transferLearning(MLWordTagger.FeatureExtractorType, revision: Int)](mlwordtagger/modelalgorithmtype/transferlearning(_:revision:).md)
  A transfer-learning algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/featureextractortype)*