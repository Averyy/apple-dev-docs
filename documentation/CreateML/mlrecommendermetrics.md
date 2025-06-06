# MLRecommenderMetrics

**Framework**: Create ML  
**Kind**: struct

Metrics you use to evaluate a recommender’s performance.

**Availability**:
- macOS 10.15+

## Declaration

```swift
struct MLRecommenderMetrics
```

## Topics

### Assessing the model
- [let excludingObserved: Bool](mlrecommendermetrics/excludingobserved.md)
  A Boolean value that indicates whether the recommender omitted training data from the recommendations.
- [var precisionRecall: MLDataTable](mlrecommendermetrics/precisionrecall.md)
  A data table with the recall and precision for each item.
- [var precisionRecallDataFrame: DataFrame](mlrecommendermetrics/precisionrecalldataframe.md)
  A data table with the recall and precision for each item.
### Handling errors
- [var isValid: Bool](mlrecommendermetrics/isvalid.md)
  A Boolean value indicating whether the recommender model was able to calculate metrics.
- [let error: (any Error)?](mlrecommendermetrics/error.md)
  The underlying error present when the metrics are invalid.
### Creating metrics
- [init(precisionRecall: MLDataTable, excludingObserved: Bool)](mlrecommendermetrics/init(precisionrecall:excludingobserved:).md)
  Creates metrics for a recommender, given a data table with precision and recall metric columns, and whether the recommender omitted training data.

## See Also

- [Improving Your Model’s Accuracy](improving-your-model-s-accuracy.md)
  Use metrics to tune the performance of your machine learning model.
- [struct MLClassifierMetrics](mlclassifiermetrics.md)
  Metrics you use to evaluate a classifier’s performance.
- [struct MLRegressorMetrics](mlregressormetrics.md)
  Metrics you use to evaluate a regressor’s performance.
- [struct MLWordTaggerMetrics](mlwordtaggermetrics.md)
  Metrics you use to evaluate a word tagger’s performance.
- [struct MLObjectDetectorMetrics](mlobjectdetectormetrics.md)
  Metrics you use to evaluate an object detector’s performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrecommendermetrics)*