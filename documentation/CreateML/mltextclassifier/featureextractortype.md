# MLTextClassifier.FeatureExtractorType

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

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

## Mentions

- [Creating a text classifier model](../creating-a-text-classifier-model.md)

## Topics

### Selecting a feature extractor type
- [MLTextClassifier.FeatureExtractorType.customEmbedding(_:)](./featureextractortype/customembedding%28_%29.md)
  A feature extractor that uses a custom embedding contained in a CoreML model file.
- [MLTextClassifier.FeatureExtractorType.staticEmbedding](./featureextractortype/staticembedding.md)
  A feature extractor that uses the standard, built-in word embeddings.
- [MLTextClassifier.FeatureExtractorType.bertEmbedding](./featureextractortype/bertembedding.md)
  A feature extractor that provides BERT contextual word embeddings.
- [MLTextClassifier.FeatureExtractorType.elmoEmbedding](./featureextractortype/elmoembedding.md)
  A feature extractor that provides ELMo contextual word embeddings.
- [MLTextClassifier.FeatureExtractorType.dynamicEmbedding](./featureextractortype/dynamicembedding.md)
  A feature extractor that provides embeddings for words, based on their in-context use.
### Describing a feature extractor type
- [var description: String](./featureextractortype/description.md)
  A text representation of a feature extractor type.
- [var debugDescription: String](./featureextractortype/debugdescription.md)
  A text representation of the feature extractor type that’s suitable for output during debugging.
- [var playgroundDescription: Any](./featureextractortype/playgrounddescription.md)
  A description of the feature extractor type shown in a playground.
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
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [MLTextClassifier.ModelAlgorithmType](./modelalgorithmtype.md)
  The type of algorithm that a text classifier uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/featureextractortype)*