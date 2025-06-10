# MLRegressorMetrics

**Framework**: Create ML  
**Kind**: struct

Metrics you use to evaluate a regressor’s performance.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct MLRegressorMetrics
```

## Mentions

- [Improving Your Model’s Accuracy](improving-your-model-s-accuracy.md)

#### Overview

To understand what performance you can expect from the regressor, you start by looking at its [`maximumError`](mlregressormetrics/maximumerror.md). This high-level metric indicates your model’s worst-case performance. To get a sense for how your model performs on average, look at the [`rootMeanSquaredError`](mlregressormetrics/rootmeansquarederror.md). In both cases, you want to minimize the value and therefore the error.

> **Note**: Each trained model contains different metrics for its various data sets (training, validation, and testing). [`Improving Your Model’s Accuracy`](improving-your-model-s-accuracy.md) compares these metrics among different data sets.

## Topics

### Understanding the model
- [var maximumError: Double](mlregressormetrics/maximumerror.md)
  The largest absolute difference between the expected values and the model’s predicted values during testing or training.
- [var rootMeanSquaredError: Double](mlregressormetrics/rootmeansquarederror.md)
  A common metric used to determine the deviation between correct and predicted values.
### Handling errors
- [var isValid: Bool](mlregressormetrics/isvalid.md)
  A Boolean value indicating whether the regressor model was able to calculate metrics.
- [var error: (any Error)?](mlregressormetrics/error.md)
  The underlying error present when the metrics are invalid.
### Creating metrics
- [init(maximumError: Double, rootMeanSquaredError: Double)](mlregressormetrics/init(maximumerror:rootmeansquarederror:).md)
  Creates regressor metrics describing the quality of your model.
### Describing metrics
- [var description: String](mlregressormetrics/description.md)
  A text representation of the regressor metrics.
- [var debugDescription: String](mlregressormetrics/debugdescription.md)
  A text representation of the regressor metrics that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlregressormetrics/playgrounddescription.md)
  A description of the regressor metrics shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlregressormetrics/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlregressormetrics/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlregressormetrics/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Improving Your Model’s Accuracy](improving-your-model-s-accuracy.md)
  Use metrics to tune the performance of your machine learning model.
- [struct MLClassifierMetrics](mlclassifiermetrics.md)
  Metrics you use to evaluate a classifier’s performance.
- [struct MLWordTaggerMetrics](mlwordtaggermetrics.md)
  Metrics you use to evaluate a word tagger’s performance.
- [struct MLRecommenderMetrics](mlrecommendermetrics.md)
  Metrics you use to evaluate a recommender’s performance.
- [struct MLObjectDetectorMetrics](mlobjectdetectormetrics.md)
  Metrics you use to evaluate an object detector’s performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlregressormetrics)*