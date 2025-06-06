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

- [func evaluation(on: MLDataTable, tokenColumn: String, labelColumn: String) -> MLWordTaggerMetrics](mlwordtagger/evaluation(on:tokencolumn:labelcolumn:)-31x1l.md)
  Computes evaluation metrics.
- [func evaluation(on: DataFrame, tokenColumn: String, labelColumn: String) -> MLWordTaggerMetrics](mlwordtagger/evaluation(on:tokencolumn:labelcolumn:)-7jhx7.md)
  Computes evaluation metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/evaluation(on:))*