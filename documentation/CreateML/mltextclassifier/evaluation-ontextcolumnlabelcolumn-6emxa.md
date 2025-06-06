# evaluation(on:textColumn:labelColumn:)

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
func evaluation(on labeledTexts: MLDataTable, textColumn: String, labelColumn: String) -> MLClassifierMetrics
```

#### Return Value

A  `MLClassifierMetrics` struct containing the computed metrics or an error message.

## Parameters

- `labeledTexts`: The data table for the data to be evaluated
- `textColumn`: Name of the text column in the provided trainingData
- `labelColumn`: Name of the label column in the provided trainingData

## See Also

- [func evaluation(on: MLTextClassifier.DataSource) -> MLClassifierMetrics](mltextclassifier/evaluation(on:)-8ch4k.md)
  Computes evaluation metrics.
- [func evaluation(on: DataFrame, textColumn: String, labelColumn: String) -> MLClassifierMetrics](mltextclassifier/evaluation(on:textcolumn:labelcolumn:)-2ibj8.md)
  Computes evaluation metrics.
- [func evaluation(on: [String : [String]]) -> MLClassifierMetrics](mltextclassifier/evaluation(on:)-3h6eu.md)
  Computes evaluation metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/evaluation(on:textcolumn:labelcolumn:)-6emxa)*