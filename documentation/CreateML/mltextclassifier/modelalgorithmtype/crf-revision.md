# MLTextClassifier.ModelAlgorithmType.crf(revision:)

**Framework**: Create ML  
**Kind**: case

A text classification algorithm that uses a statistical model of transition probabilities between words.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
case crf(revision: Int?)
```

## Mentions

- [Creating a text classifier model](creating-a-text-classifier-model.md)

## Parameters

- `revision`: The algorithm version. The only supported version is 1. If   defaults to the latest version.

## See Also

- [MLTextClassifier.ModelAlgorithmType.maxEnt(revision:)](mltextclassifier/modelalgorithmtype/maxent(revision:).md)
  A text classification algorithm that uses multinomial logistic regression based on the frequencies of words, independent of context.
- [case transferLearning(MLTextClassifier.FeatureExtractorType, revision: Int?)](mltextclassifier/modelalgorithmtype/transferlearning(_:revision:).md)
  A text classification algorithm that uses transfer learning by leveraging a feature extractor to generate embeddings.
- [MLTextClassifier.FeatureExtractorType](mltextclassifier/featureextractortype.md)
  The text feature extractor type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/modelalgorithmtype/crf(revision:))*