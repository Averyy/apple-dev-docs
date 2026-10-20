# MLWordTagger.FeatureExtractorType

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

The feature extractors that are available to train a word tagger using with the transfer-learning algorithm option.

**Availability**:
- macOS 11.0+

## Declaration

```swift
enum FeatureExtractorType
```

## Topics

### Selecting a feature extractor type
- [MLWordTagger.FeatureExtractorType.bertEmbedding](./featureextractortype/bertembedding.md)
  A feature extractor that provides BERT contextual word embeddings.
- [MLWordTagger.FeatureExtractorType.elmoEmbedding](./featureextractortype/elmoembedding.md)
  A feature extractor that provides ELMo contextual word embeddings.
- [MLWordTagger.FeatureExtractorType.dynamicEmbedding](./featureextractortype/dynamicembedding.md)
  A feature extractor that provides embeddings for words, based on their in-context use.
### Describing a feature extractor type
- [var description: String](./featureextractortype/description.md)
  A text representation of a feature extractor type.
- [var debugDescription: String](./featureextractortype/debugdescription.md)
  A text representation of the feature extractor that’s suitable for output during debugging.
- [var playgroundDescription: Any](./featureextractortype/playgrounddescription.md)
  A description of the feature extractor in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./featureextractortype/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](./featureextractortype/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](./featureextractortype/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomPlaygroundDisplayConvertible](../../Swift/customplaygrounddisplayconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [MLWordTagger.ModelAlgorithmType](./modelalgorithmtype.md)
  The algorithm type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/featureextractortype)*