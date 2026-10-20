# evaluation(on:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

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

**Other overloads**:

```swift
func evaluation(on labeledTexts: [String : [String]]) -> MLClassifierMetrics
```

#### Return Value

Classifier metrics.

## Parameters

- `labeledTexts`: A data source of labeled texts to evaluate.

## See Also

### Evaluating a text classifier
- [func evaluation(on:textColumn:labelColumn:)](./evaluation%28on,textcolumn,labelcolumn%29.md)
  Computes evaluation metrics.
- [let trainingMetrics: MLClassifierMetrics](./trainingmetrics.md)
  Measurements of the classifier’s performance on the training data set.
- [let validationMetrics: MLClassifierMetrics](./validationmetrics.md)
  Measurements of the classifier’s performance on the validation data set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/evaluation(on:))*