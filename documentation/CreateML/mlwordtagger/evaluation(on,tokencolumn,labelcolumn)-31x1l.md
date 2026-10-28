# evaluation(on:tokenColumn:labelColumn:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Computes evaluation metrics.

**Availability**:
- macOS 10.14+ - Deprecated in 13.0

## Declaration

```swift
func evaluation(on labeledTokens: MLDataTable, tokenColumn: String, labelColumn: String) -> MLWordTaggerMetrics
```

**Other overloads**:

```swift
func evaluation(on labeledTokens: DataFrame, tokenColumn: String, labelColumn: String) -> MLWordTaggerMetrics
```

## Mentions

- [Creating a word tagger model](../creating-a-word-tagger-model.md)

## Return Value

Word tagger metrics.

## Parameters

- `labeledTokens`: A table containing tokens and labels.
- `tokenColumn`: The name of the token column in the data frame.
- `labelColumn`: The name of the label column in the data frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/evaluation(on:tokencolumn:labelcolumn:)-31x1l)*