# trainingMetrics

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

Measurements of the tagger’s performance on the training data set.

**Availability**:
- macOS 10.14+

## Declaration

```swift
let trainingMetrics: MLWordTaggerMetrics
```

## Mentions

- [Creating a word tagger model](../creating-a-word-tagger-model.md)

## See Also

### Evaluating a word tagger
- [func evaluation(on:tokenColumn:labelColumn:)](./evaluation%28on,tokencolumn,labelcolumn%29.md)
  Computes evaluation metrics.
- [func evaluation(on: [(tokens: [MLWordTagger.Token], labels: [String])]) -> MLWordTaggerMetrics](./evaluation%28on%29.md)
  Computes evaluation metrics.
- [let validationMetrics: MLWordTaggerMetrics](./validationmetrics.md)
  Measurements of the tagger’s performance on the validation data set.
- [struct MLWordTaggerMetrics](../mlwordtaggermetrics.md)
  Metrics you use to evaluate a word tagger’s performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/trainingmetrics)*