# MLClassifierMetrics

**Framework**: Createml  
**Kind**: struct

Metrics you use to evaluate a classifier’s performance.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct MLClassifierMetrics
```

## Mentions

- [Creating a text classifier model](creating-a-text-classifier-model.md)
- [Creating a Text Classifier Model](creating-a-classification-model-for-natural-language.md)
- [Creating an Image Classifier Model](creating-an-image-classifier-model.md)
- [Improving Your Model’s Accuracy](improving-your-model-s-accuracy.md)

#### Overview

Use [`MLClassifierMetrics`](mlclassifiermetrics.md) to evaluate your model’s ability to distinguish between different categories when it’s classifying data.

You can determine the model’s accuracy using the [`classificationError`](mlclassifiermetrics/classificationerror.md) metric. For information about how your model is mislabeling or missing a certain category, use the [`precisionRecall`](mlclassifiermetrics/precisionrecall.md) metric. To determine specific cases where your model is mistaking one label for another, use the [`confusion`](mlclassifiermetrics/confusion.md) property.

Accuracy can be a misleading metric if you use unbalanced data, which means the number of examples for some categories are much larger than others. Instead, use [`precisionRecall`](mlclassifiermetrics/precisionrecall.md) or [`confusion`](mlclassifiermetrics/confusion.md).

> **Note**: Each trained model contains different metrics for its various data sets (training, validation, and testing). [`Improving Your Model’s Accuracy`](improving-your-model-s-accuracy.md) compares these metrics between different data sets.

## Topics

### Understanding the model
- [var classificationError: Double](mlclassifiermetrics/classificationerror.md)
  The fraction of incorrectly labeled examples.
- [var precisionRecall: MLDataTable](mlclassifiermetrics/precisionrecall.md)
  A data table listing the precision and recall percentages for each class.
- [var confusion: MLDataTable](mlclassifiermetrics/confusion.md)
  A table comparing the actual and predicted labels for each classification category.
- [var confusionDataFrame: DataFrame](mlclassifiermetrics/confusiondataframe.md)
  A data frame comparing the actual and predicted labels for each class.
- [var precisionRecallDataFrame: DataFrame](mlclassifiermetrics/precisionrecalldataframe.md)
  A data frame listing the precision and recall percentages for each class.
### Handling errors
- [var isValid: Bool](mlclassifiermetrics/isvalid.md)
  A Boolean value indicating whether the classifier model was able to calculate metrics.
- [var error: (any Error)?](mlclassifiermetrics/error.md)
  The underlying error present when the metrics are invalid.
### Creating metrics
- [init(classificationError: Double, confusion: MLDataTable, precisionRecall: MLDataTable)](mlclassifiermetrics/init(classificationerror:confusion:precisionrecall:).md)
  Creates empty classifier metrics.
### Describing metrics
- [var description: String](mlclassifiermetrics/description.md)
  A text representation of the classifier metrics.
- [var debugDescription: String](mlclassifiermetrics/debugdescription.md)
  A text representation of the classifier metrics that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlclassifiermetrics/playgrounddescription.md)
  A description of the classifier metrics shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlclassifiermetrics/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlclassifiermetrics/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlclassifiermetrics/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [Improving Your Model’s Accuracy](improving-your-model-s-accuracy.md)
  Use metrics to tune the performance of your machine learning model.
- [struct MLRegressorMetrics](mlregressormetrics.md)
  Metrics you use to evaluate a regressor’s performance.
- [struct MLWordTaggerMetrics](mlwordtaggermetrics.md)
  Metrics you use to evaluate a word tagger’s performance.
- [struct MLRecommenderMetrics](mlrecommendermetrics.md)
  Metrics you use to evaluate a recommender’s performance.
- [struct MLObjectDetectorMetrics](mlobjectdetectormetrics.md)
  Metrics you use to evaluate an object detector’s performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CreateML/mlclassifiermetrics)*