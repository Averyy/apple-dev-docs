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
func evaluation(on labeledTexts: [String : [String]]) -> MLClassifierMetrics
```

#### Return Value

Classifier metrics.

## Parameters

- `labeledTexts`: A dictionary of labeled texts to evaluate.

## See Also

- [func evaluation(on: MLTextClassifier.DataSource) -> MLClassifierMetrics](mltextclassifier/evaluation(on:)-8ch4k.md)
  Computes evaluation metrics.
- [func evaluation(on: DataFrame, textColumn: String, labelColumn: String) -> MLClassifierMetrics](mltextclassifier/evaluation(on:textcolumn:labelcolumn:)-2ibj8.md)
  Computes evaluation metrics.
- [func evaluation(on: MLDataTable, textColumn: String, labelColumn: String) -> MLClassifierMetrics](mltextclassifier/evaluation(on:textcolumn:labelcolumn:)-6emxa.md)
  Computes evaluation metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/evaluation(on:)-3h6eu)*