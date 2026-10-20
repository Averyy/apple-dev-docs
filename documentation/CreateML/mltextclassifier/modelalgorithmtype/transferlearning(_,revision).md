# MLTextClassifier.ModelAlgorithmType.transferLearning(_:revision:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

A text classification algorithm that uses transfer learning by leveraging a feature extractor to generate embeddings.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
case transferLearning(MLTextClassifier.FeatureExtractorType, revision: Int?)
```

## Mentions

- [Creating a text classifier model](../../creating-a-text-classifier-model.md)

## Parameters

- `_`: Feature extractor to be used by the transfer learning algorithm.
- `revision`: The algorithm version. The only supported version is 1. If `nil` defaults to the latest version.

## See Also

### Selecting an algorithm type
- [MLTextClassifier.ModelAlgorithmType.crf(revision:)](./crf%28revision%29.md)
  A text classification algorithm that uses a statistical model of transition probabilities between words.
- [MLTextClassifier.ModelAlgorithmType.maxEnt(revision:)](./maxent%28revision%29.md)
  A text classification algorithm that uses multinomial logistic regression based on the frequencies of words, independent of context.
- [MLTextClassifier.FeatureExtractorType](../featureextractortype.md)
  The text feature extractor type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/modelalgorithmtype/transferlearning(_:revision:))*