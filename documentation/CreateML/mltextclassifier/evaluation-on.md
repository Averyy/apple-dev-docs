# evaluation(on:)

**Framework**: Create ML  
**Kind**: method

Computes evaluation metrics.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
func evaluation(on labeledTexts: MLTextClassifier.DataSource) -> MLClassifierMetrics
```

#### Return Value

Classifier metrics.

## Parameters

- `labeledTexts`: A data source of labeled texts to evaluate.

## See Also

- [func evaluation(on:textColumn:labelColumn:)](mltextclassifier/evaluation(on:textcolumn:labelcolumn:).md)
  Computes evaluation metrics.
- [let trainingMetrics: MLClassifierMetrics](mltextclassifier/trainingmetrics.md)
  Measurements of the classifier’s performance on the training data set.
- [let validationMetrics: MLClassifierMetrics](mltextclassifier/validationmetrics.md)
  Measurements of the classifier’s performance on the validation data set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/evaluation(on:))*