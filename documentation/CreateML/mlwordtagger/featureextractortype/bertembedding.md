# MLWordTagger.FeatureExtractorType.bertEmbedding

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

A feature extractor that provides BERT contextual word embeddings.

**Availability**:
- macOS 14.0+

## Declaration

```swift
case bertEmbedding
```

#### Discussion

The embeddings consider the context from left-to-right and right-to-left simultaneously.

BERT embedding requires certain downloadable assets to be present on device at training time. Training will throw an error if the specified language is unavailable at runtime. Asset downloads are managed in the background automatically by the OS when a new language is configured in device settings, such as when adding a new keyboard language or changing the preferred language.

## See Also

### Selecting a feature extractor type
- [MLWordTagger.FeatureExtractorType.elmoEmbedding](./elmoembedding.md)
  A feature extractor that provides ELMo contextual word embeddings.
- [MLWordTagger.FeatureExtractorType.dynamicEmbedding](./dynamicembedding.md)
  A feature extractor that provides embeddings for words, based on their in-context use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/featureextractortype/bertembedding)*