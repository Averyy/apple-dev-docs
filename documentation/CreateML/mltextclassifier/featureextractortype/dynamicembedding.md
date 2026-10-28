# MLTextClassifier.FeatureExtractorType.dynamicEmbedding

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

A feature extractor that provides embeddings for words, based on their in-context use.

**Availability**:
- iOS 15.0+ - Deprecated in 17.0 (renamed: elmoEmbedding)
- iPadOS 15.0+ - Deprecated in 17.0 (renamed: elmoEmbedding)
- Mac Catalyst 15.0+ - Deprecated in 17.0 (renamed: elmoEmbedding)
- macOS 10.15+ - Deprecated in 14.0 (renamed: elmoEmbedding)
- visionOS 1.0+

## Declaration

```swift
case dynamicEmbedding
```

## Discussion

Dynamic embedding requires certain downloadable assets to be present on device at training time. Training will throw an error if the specified language is unavailable at runtime. Asset downloads are managed in the background automatically by the OS when a new language is configured in device settings, such as when adding a new keyboard language or changing the preferred language.

## See Also

### Selecting a feature extractor type
- [MLTextClassifier.FeatureExtractorType.customEmbedding(_:)](./customembedding%28_%29.md)
  A feature extractor that uses a custom embedding contained in a CoreML model file.
- [MLTextClassifier.FeatureExtractorType.staticEmbedding](./staticembedding.md)
  A feature extractor that uses the standard, built-in word embeddings.
- [MLTextClassifier.FeatureExtractorType.bertEmbedding](./bertembedding.md)
  A feature extractor that provides BERT contextual word embeddings.
- [MLTextClassifier.FeatureExtractorType.elmoEmbedding](./elmoembedding.md)
  A feature extractor that provides ELMo contextual word embeddings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/featureextractortype/dynamicembedding)*