# evaluation(on:textColumn:labelColumn:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Computes evaluation metrics.

**Availability**:
- iOS 15.0+ - Deprecated in 16.0
- iPadOS 15.0+ - Deprecated in 16.0
- Mac Catalyst 15.0+ - Deprecated in 16.0
- macOS 10.14+ - Deprecated in 13.0
- visionOS 1.0+

> **Deprecated**: Use DataFrame instead of MLDataTable.

## Declaration

```swift
func evaluation(on labeledTexts: MLDataTable, textColumn: String, labelColumn: String) -> MLClassifierMetrics
```

**Other overloads**:

```swift
func evaluation(on dataFrame: DataFrame, textColumn: String, labelColumn: String) -> MLClassifierMetrics
```

## Return Value

A  `MLClassifierMetrics` struct containing the computed metrics or an error message.

## Parameters

- `labeledTexts`: The data table for the data to be evaluated
- `textColumn`: Name of the text column in the provided trainingData
- `labelColumn`: Name of the label column in the provided trainingData


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/evaluation(on:textcolumn:labelcolumn:)-6emxa)*