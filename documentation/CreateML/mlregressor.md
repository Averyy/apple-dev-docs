# MLRegressor

**Framework**: Create ML  
**Kind**: enum

A model you train to estimate continuous values.

**Availability**:
- macOS 10.14+

## Declaration

```swift
enum MLRegressor
```

## Mentions

- [Improving Your Model’s Accuracy](improving-your-model-s-accuracy.md)

#### Overview

Use an [`MLRegressor`](mlregressor.md) to estimate continuous values like price, time, or temperature.

A regressor differs from a classifier because it can predict output values not seen during the training process. By contrast, a classifier can only classify input into the categories you provide in the training data.

For example, when estimating housing prices on Mars, a regressor can interpolate between the examples to estimate prices not seen during training. The figure below shows a linear regressor for Mars real-estate prices similar to the [`Integrating a Core ML Model into Your App`](https://developer.apple.com/documentation/CoreML/integrating-a-core-ml-model-into-your-app) sample.

![A graph showing housing prices for mars with a linear regressor used to create a continuous estimation between](https://docs-assets.developer.apple.com/published/03ef437b3bfd8a33d85264d85eeb2de4/MLRegressor-1%402x.png)

In this case, there are no data points with three solar panels, but the regressor can make an informed prediction about the housing price.

When you create an [`MLRegressor`](mlregressor.md), Create ML inspects your data and automatically chooses a specific regressor (see ).

## Topics

### Creating and training a regressor
- [init(trainingData:targetColumn:featureColumns:)](mlregressor/init(trainingdata:targetcolumn:featurecolumns:).md)
  Creates a regressor.
- [var targetColumn: String](mlregressor/targetcolumn.md)
  The name of the column you selected at initialization to define which feature the regressor predicts.
- [var featureColumns: [String]](mlregressor/featurecolumns.md)
  The names of the columns you selected at initialization to train the regressor.
### Evaluating a regressor
- [func evaluation(on:)](mlregressor/evaluation(on:).md)
  Evaluates the classifier on the provided labeled data.
- [var trainingMetrics: MLRegressorMetrics](mlregressor/trainingmetrics.md)
  Measurements of the regressor’s performance on the training data set.
- [var validationMetrics: MLRegressorMetrics](mlregressor/validationmetrics.md)
  Measurements of the regressor’s performance on the validation data set.
### Testing a regressor
- [func predictions(from:)](mlregressor/predictions(from:).md)
### Saving a regressor
- [func write(to: URL, metadata: MLModelMetadata?) throws](mlregressor/write(to:metadata:).md)
  Exports a Core ML model file for use in your app.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](mlregressor/write(tofile:metadata:).md)
  Exports a Core ML model file for use in your app.
### Describing a regressor
- [var model: MLModel](mlregressor/model.md)
  The underlying Core ML model stored in memory.
- [var description: String](mlregressor/description.md)
  A text representation of the regressor.
- [var debugDescription: String](mlregressor/debugdescription.md)
  A text representation of the regressor that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlregressor/playgrounddescription.md)
  A description of the regressor shown in a playground.
### Regressor cases
- [case linear(MLLinearRegressor)](mlregressor/linear(_:).md)
  A regressor that estimates the target as a linear function of the features.
- [case decisionTree(MLDecisionTreeRegressor)](mlregressor/decisiontree(_:).md)
  A regressor that estimates the target by learning rules to split the data.
- [case boostedTree(MLBoostedTreeRegressor)](mlregressor/boostedtree(_:).md)
  A regressor based on a collection of decision trees combined with gradient boosting.
- [case randomForest(MLRandomForestRegressor)](mlregressor/randomforest(_:).md)
  A regressor based on a collection of decision trees trained on subsets of the data.
### Supporting regressor types
- [struct MLLinearRegressor](mllinearregressor.md)
  A regressor that estimates the target as a linear function of the features.
- [struct MLDecisionTreeRegressor](mldecisiontreeregressor.md)
  A regressor that estimates the target by learning rules to split the data.
- [struct MLRandomForestRegressor](mlrandomforestregressor.md)
  A regressor based on a collection of decision trees trained on subsets of the data.
- [struct MLBoostedTreeRegressor](mlboostedtreeregressor.md)
  A regressor based on a collection of decision trees combined with gradient boosting.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlregressor/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlregressor/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlregressor/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Creating a model from tabular data](creating-a-model-from-tabular-data.md)
  Train a machine learning model by using Core ML to import and manage tabular data.
- [enum MLClassifier](mlclassifier.md)
  A model you train to classify data into discrete categories.
- [struct MLRecommender](mlrecommender.md)
  A model you train to make recommendations based on item similarity, grouping, and, optionally, item ratings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlregressor)*