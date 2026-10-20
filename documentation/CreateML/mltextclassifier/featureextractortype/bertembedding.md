# MLTextClassifier.FeatureExtractorType.bertEmbedding

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

A feature extractor that provides BERT contextual word embeddings.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
case bertEmbedding
```

## Mentions

- [Creating a text classifier model](../../creating-a-text-classifier-model.md)

#### Discussion

The embeddings consider the context from left-to-right and right-to-left simultaneously.

BERT embedding requires certain downloadable assets to be present on device at training time. Training will throw an error if the specified language is unavailable at runtime. Asset downloads are managed in the background automatically by the OS when a new language is configured in device settings, such as when adding a new keyboard language or changing the preferred language.

## See Also

### Selecting a feature extractor type
- [MLTextClassifier.FeatureExtractorType.customEmbedding(_:)](./customembedding%28_%29.md)
  A feature extractor that uses a custom embedding contained in a CoreML model file.
- [MLTextClassifier.FeatureExtractorType.staticEmbedding](./staticembedding.md)
  A feature extractor that uses the standard, built-in word embeddings.
- [MLTextClassifier.FeatureExtractorType.elmoEmbedding](./elmoembedding.md)
  A feature extractor that provides ELMo contextual word embeddings.
- [MLTextClassifier.FeatureExtractorType.dynamicEmbedding](./dynamicembedding.md)
  A feature extractor that provides embeddings for words, based on their in-context use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/featureextractortype/bertembedding)*