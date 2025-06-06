# MLTextClassifier.FeatureExtractorType.dynamicEmbedding

**Framework**: Create ML  
**Kind**: case

A feature extractor that provides embeddings for words, based on their in-context use.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
case dynamicEmbedding
```

#### Discussion

Dynamic embedding requires certain downloadable assets to be present on device at training time. Training will throw an error if the specified language is unavailable at runtime. Asset downloads are managed in the background automatically by the OS when a new language is configured in device settings, such as when adding a new keyboard language or changing the preferred language.

## See Also

- [MLTextClassifier.FeatureExtractorType.customEmbedding(_:)](mltextclassifier/featureextractortype/customembedding(_:).md)
  A feature extractor that uses a custom embedding contained in a CoreML model file.
- [MLTextClassifier.FeatureExtractorType.staticEmbedding](mltextclassifier/featureextractortype/staticembedding.md)
  A feature extractor that uses the standard, built-in word embeddings.
- [MLTextClassifier.FeatureExtractorType.bertEmbedding](mltextclassifier/featureextractortype/bertembedding.md)
  A feature extractor that provides BERT contextual word embeddings.
- [MLTextClassifier.FeatureExtractorType.elmoEmbedding](mltextclassifier/featureextractortype/elmoembedding.md)
  A feature extractor that provides ELMo contextual word embeddings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/featureextractortype/dynamicembedding)*