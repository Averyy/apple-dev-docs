# evaluation(on:)

**Framework**: Create ML  
**Kind**: method

Computes evaluation metrics.

**Availability**:
- macOS 10.14+

## Declaration

```swift
func evaluation(on labeledTokens: [(tokens: [MLWordTagger.Token], labels: [String])]) -> MLWordTaggerMetrics
```

#### Return Value

Word tagger metrics.

## Parameters

- `labeledTokens`: An array of token and label pairs.

## See Also

- [func evaluation(on:tokenColumn:labelColumn:)](mlwordtagger/evaluation(on:tokencolumn:labelcolumn:).md)
  Computes evaluation metrics.
- [let trainingMetrics: MLWordTaggerMetrics](mlwordtagger/trainingmetrics.md)
  Measurements of the tagger’s performance on the training data set.
- [let validationMetrics: MLWordTaggerMetrics](mlwordtagger/validationmetrics.md)
  Measurements of the tagger’s performance on the validation data set.
- [struct MLWordTaggerMetrics](mlwordtaggermetrics.md)
  Metrics you use to evaluate a word tagger’s performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/evaluation(on:))*