# init(precisionRecall:excludingObserved:)

**Framework**: Create ML  
**Kind**: init

Creates metrics for a recommender, given a data table with precision and recall metric columns, and whether the recommender omitted training data.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(precisionRecall: MLDataTable, excludingObserved: Bool)
```

#### Discussion

Do not use this initializer. [`MLRecommender`](mlrecommender.md) generates metrics for you when you call its [`evaluation(on:userColumn:itemColumn:ratingColumn:cutoffs:excludingObserved:)`](mlrecommender/evaluation(on:usercolumn:itemcolumn:ratingcolumn:cutoffs:excludingobserved:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrecommendermetrics/init(precisionrecall:excludingobserved:))*