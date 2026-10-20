# evaluation(on:tokenColumn:labelColumn:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Computes evaluation metrics.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func evaluation(on labeledTokens: DataFrame, tokenColumn: String, labelColumn: String) -> MLWordTaggerMetrics
```

**Other overloads**:

```swift
func evaluation(on labeledTokens: MLDataTable, tokenColumn: String, labelColumn: String) -> MLWordTaggerMetrics
```

#### Return Value

Word tagger metrics.

## Parameters

- `labeledTokens`: An data frame containing tokens and labels.
- `tokenColumn`: The name of the token column in the data frame.
- `labelColumn`: The name of the label column in the data frame.

## See Also

### Evaluating a word tagger
- [func evaluation(on: [(tokens: [MLWordTagger.Token], labels: [String])]) -> MLWordTaggerMetrics](./evaluation%28on%29.md)
  Computes evaluation metrics.
- [let trainingMetrics: MLWordTaggerMetrics](./trainingmetrics.md)
  Measurements of the tagger’s performance on the training data set.
- [let validationMetrics: MLWordTaggerMetrics](./validationmetrics.md)
  Measurements of the tagger’s performance on the validation data set.
- [struct MLWordTaggerMetrics](../mlwordtaggermetrics.md)
  Metrics you use to evaluate a word tagger’s performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/evaluation(on:tokencolumn:labelcolumn:))*