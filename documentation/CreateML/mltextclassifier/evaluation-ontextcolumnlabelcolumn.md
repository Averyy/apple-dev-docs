# evaluation(on:textColumn:labelColumn:)

**Framework**: Create ML  
**Kind**: method

Computes evaluation metrics.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func evaluation(on dataFrame: DataFrame, textColumn: String, labelColumn: String) -> MLClassifierMetrics
```

#### Return Value

The computed metrics or an error message.

## Parameters

- `dataFrame`: A data frame containing labeled examples.
- `textColumn`: The name of the text column.
- `labelColumn`: The name of the label column.

## See Also

- [func evaluation(on:)](mltextclassifier/evaluation(on:).md)
  Computes evaluation metrics.
- [let trainingMetrics: MLClassifierMetrics](mltextclassifier/trainingmetrics.md)
  Measurements of the classifier’s performance on the training data set.
- [let validationMetrics: MLClassifierMetrics](mltextclassifier/validationmetrics.md)
  Measurements of the classifier’s performance on the validation data set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/evaluation(on:textcolumn:labelcolumn:))*