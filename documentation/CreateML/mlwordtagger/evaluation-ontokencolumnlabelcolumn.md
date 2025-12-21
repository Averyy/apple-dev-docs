# evaluation(on:tokenColumn:labelColumn:)

**Framework**: Create ML  
**Kind**: method

Computes evaluation metrics.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func evaluation(on labeledTokens: DataFrame, tokenColumn: String, labelColumn: String) -> MLWordTaggerMetrics
```

#### Return Value

Word tagger metrics.

## Parameters

- `labeledTokens`: An data frame containing tokens and labels.
- `tokenColumn`: The name of the token column in the data frame.
- `labelColumn`: The name of the label column in the data frame.

## See Also

- [func evaluation(on: [(tokens: [MLWordTagger.Token], labels: [String])]) -> MLWordTaggerMetrics](mlwordtagger/evaluation(on:).md)
  Computes evaluation metrics.
- [let trainingMetrics: MLWordTaggerMetrics](mlwordtagger/trainingmetrics.md)
  Measurements of the tagger’s performance on the training data set.
- [let validationMetrics: MLWordTaggerMetrics](mlwordtagger/validationmetrics.md)
  Measurements of the tagger’s performance on the validation data set.
- [struct MLWordTaggerMetrics](mlwordtaggermetrics.md)
  Metrics you use to evaluate a word tagger’s performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/evaluation(on:tokencolumn:labelcolumn:))*