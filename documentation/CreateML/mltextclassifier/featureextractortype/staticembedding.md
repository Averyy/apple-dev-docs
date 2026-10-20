# MLTextClassifier.FeatureExtractorType.staticEmbedding

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

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

The standard word embeddings are the same as those that [`NLEmbedding`](../../../NaturalLanguage/nlembedding.md) provides with its [`wordEmbedding(for:)`](../../../NaturalLanguage/nlembedding/wordembedding%28for%29.md) method.

## See Also

### Selecting a feature extractor type
- [MLTextClassifier.FeatureExtractorType.customEmbedding(_:)](./customembedding%28_%29.md)
  A feature extractor that uses a custom embedding contained in a CoreML model file.
- [MLTextClassifier.FeatureExtractorType.bertEmbedding](./bertembedding.md)
  A feature extractor that provides BERT contextual word embeddings.
- [MLTextClassifier.FeatureExtractorType.elmoEmbedding](./elmoembedding.md)
  A feature extractor that provides ELMo contextual word embeddings.
- [MLTextClassifier.FeatureExtractorType.dynamicEmbedding](./dynamicembedding.md)
  A feature extractor that provides embeddings for words, based on their in-context use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/featureextractortype/staticembedding)*