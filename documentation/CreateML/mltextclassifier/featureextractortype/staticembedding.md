# MLTextClassifier.FeatureExtractorType.staticEmbedding

**Framework**: Create ML  
**Kind**: case

A feature extractor that uses the standard, built-in word embeddings.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
case staticEmbedding
```

#### Discussion

The standard word embeddings are the same as those that [`NLEmbedding`](https://developer.apple.com/documentation/NaturalLanguage/NLEmbedding) provides with its [`wordEmbedding(for:)`](https://developer.apple.com/documentation/NaturalLanguage/NLEmbedding/wordEmbedding(for:)) method.

## See Also

- [MLTextClassifier.FeatureExtractorType.customEmbedding(_:)](mltextclassifier/featureextractortype/customembedding(_:).md)
  A feature extractor that uses a custom embedding contained in a CoreML model file.
- [MLTextClassifier.FeatureExtractorType.bertEmbedding](mltextclassifier/featureextractortype/bertembedding.md)
  A feature extractor that provides BERT contextual word embeddings.
- [MLTextClassifier.FeatureExtractorType.elmoEmbedding](mltextclassifier/featureextractortype/elmoembedding.md)
  A feature extractor that provides ELMo contextual word embeddings.
- [MLTextClassifier.FeatureExtractorType.dynamicEmbedding](mltextclassifier/featureextractortype/dynamicembedding.md)
  A feature extractor that provides embeddings for words, based on their in-context use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/featureextractortype/staticembedding)*