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
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlwordtagger/featureextractortype/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlwordtagger/featureextractortype/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlwordtagger/featureextractortype/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [MLWordTagger.ModelAlgorithmType](mlwordtagger/modelalgorithmtype.md)
  The algorithm type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/featureextractortype)*