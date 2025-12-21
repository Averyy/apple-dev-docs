# MLWordTaggerMetrics

**Framework**: Create ML  
**Kind**: struct

Metrics you use to evaluate a word tagger’s performance.

**Availability**:
- macOS 10.14+

## Declaration

```swift
struct MLWordTaggerMetrics
```

## Mentions

- [Creating a word tagger model](creating-a-word-tagger-model.md)

## Topics

### Analyzing the tagger’s performance
- [var taggingError: Double](mlwordtaggermetrics/taggingerror.md)
  The fraction of incorrectly tagged examples.
- [var precisionRecall: MLDataTable](mlwordtaggermetrics/precisionrecall.md)
  A data table listing the precision and recall percentages for each category.
- [var confusion: MLDataTable](mlwordtaggermetrics/confusion.md)
  A table comparing the actual and predicted labels for each tagging category.
### Handling errors
- [var isValid: Bool](mlwordtaggermetrics/isvalid.md)
  A Boolean value indicating whether the metrics were calculated.
- [var error: (any Error)?](mlwordtaggermetrics/error.md)
  The underlying error present when the metrics are invalid.
### Describing metrics
- [var description: String](mlwordtaggermetrics/description.md)
  A text representation of the word tagger metrics.
- [var debugDescription: String](mlwordtaggermetrics/debugdescription.md)
  A text representation of the word tagger metrics that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlwordtaggermetrics/playgrounddescription.md)
  A description of the word tagger metrics shown in a playground.
- [var confusionDataFrame: DataFrame](mlwordtaggermetrics/confusiondataframe.md)
  A data frame comparing the actual and predicted labels for each class.
- [var precisionRecallDataFrame: DataFrame](mlwordtaggermetrics/precisionrecalldataframe.md)
  A data frame listing the precision and recall percentages for each class.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlwordtaggermetrics/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlwordtaggermetrics/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlwordtaggermetrics/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [Improving Your Model’s Accuracy](improving-your-model-s-accuracy.md)
  Use metrics to tune the performance of your machine learning model.
- [struct MLClassifierMetrics](mlclassifiermetrics.md)
  Metrics you use to evaluate a classifier’s performance.
- [struct MLRegressorMetrics](mlregressormetrics.md)
  Metrics you use to evaluate a regressor’s performance.
- [struct MLRecommenderMetrics](mlrecommendermetrics.md)
  Metrics you use to evaluate a recommender’s performance.
- [struct MLObjectDetectorMetrics](mlobjectdetectormetrics.md)
  Metrics you use to evaluate an object detector’s performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtaggermetrics)*