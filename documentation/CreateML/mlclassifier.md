# MLClassifier

**Framework**: Create ML  
**Kind**: enum

A model you train to classify data into discrete categories.

**Availability**:
- macOS 10.14+

## Declaration

```swift
enum MLClassifier
```

## Mentions

- [Improving Your Model’s Accuracy](improving-your-model-s-accuracy.md)

#### Overview

Use an [`MLClassifier`](mlclassifier.md) to train a general-purpose model to recognize categories.

For example, you can create a classifier that predicts whether a sports team is likely to win or lose its next game by training it with these inputs:

- The team’s win-loss ratio
- The team’s game locations

> ❗ **Important**: When working with image or natural language data, don’t use [`MLClassifier`](mlclassifier.md). Instead, use the `MLImageClassifierBuilder` or one of the Natural Language models ([`MLTextClassifier`](mltextclassifier.md) or [`MLWordTagger`](mlwordtagger.md)).

When you create an [`MLClassifier`](mlclassifier.md), Create ML inspects your data and automatically chooses a specific classifier (see ).

## Topics

### Creating and training a classifier
- [init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?) throws](mlclassifier/init(trainingdata:targetcolumn:featurecolumns:)-6ojd1.md)
  Creates a classifier.
- [init(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?) throws](mlclassifier/init(trainingdata:targetcolumn:featurecolumns:)-p3f6.md)
  Creates a classifier from the feature columns in the training data to predict the categories in the target column.
- [var targetColumn: String](mlclassifier/targetcolumn.md)
  The name of the column you selected at initialization to define which categories the classifier predicts.
- [var featureColumns: [String]](mlclassifier/featurecolumns.md)
  The names of the columns you selected at initialization to train the classifier.
### Assessing model accuracy
- [var trainingMetrics: MLClassifierMetrics](mlclassifier/trainingmetrics.md)
  Measurements of the classifier’s performance on the training data set.
- [var validationMetrics: MLClassifierMetrics](mlclassifier/validationmetrics.md)
  Measurements of the classifier’s performance on the validation data set.
### Evaluating a classifier
- [func evaluation(on: DataFrame) -> MLClassifierMetrics](mlclassifier/evaluation(on:)-3xetj.md)
  Evaluates the classifier on the provided labeled data.
- [func evaluation(on: MLDataTable) -> MLClassifierMetrics](mlclassifier/evaluation(on:)-6433y.md)
  Evaluates the classifier on the provided labeled data.
### Testing a classifier
- [func predictions(from: DataFrame) throws -> AnyColumn](mlclassifier/predictions(from:)-7mww4.md)
- [func predictions(from: MLDataTable) throws -> MLUntypedColumn](mlclassifier/predictions(from:)-50jlv.md)
  Classifies the provided data into the target categories.
### Saving a classifier
- [func write(to: URL, metadata: MLModelMetadata?) throws](mlclassifier/write(to:metadata:).md)
  Exports a Core ML model file for use in your app.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](mlclassifier/write(tofile:metadata:).md)
  Exports a Core ML model file for use in your app.
### Describing a model
- [var model: MLModel](mlclassifier/model.md)
  The underlying Core ML model stored in memory.
- [var description: String](mlclassifier/description.md)
  A text representation of the classifier.
- [var debugDescription: String](mlclassifier/debugdescription.md)
  A text representation of the classifier that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlclassifier/playgrounddescription.md)
  A description of the classifier shown in a playground.
### Classifier cases
- [case decisionTree(MLDecisionTreeClassifier)](mlclassifier/decisiontree(_:).md)
  A classifier that predicts the target by creating rules to split the data.
- [case randomForest(MLRandomForestClassifier)](mlclassifier/randomforest(_:).md)
  A classifier based on a collection of decision trees trained on subsets of the data.
- [case boostedTree(MLBoostedTreeClassifier)](mlclassifier/boostedtree(_:).md)
  A classifier based on a collection of decision trees combined with gradient boosting.
- [case logisticRegression(MLLogisticRegressionClassifier)](mlclassifier/logisticregression(_:).md)
  A classifier that predicts a discrete target value as a function of data features.
- [case supportVector(MLSupportVectorClassifier)](mlclassifier/supportvector(_:).md)
  A classifier that predicts a binary target value by maximizing the separation between categories.
### Supporting classifier types
- [struct MLDecisionTreeClassifier](mldecisiontreeclassifier.md)
  A classifier that predicts the target by creating rules to split the data.
- [struct MLRandomForestClassifier](mlrandomforestclassifier.md)
  A classifier based on a collection of decision trees trained on subsets of the data.
- [struct MLBoostedTreeClassifier](mlboostedtreeclassifier.md)
  A classifier based on a collection of decision trees combined with gradient boosting.
- [struct MLLogisticRegressionClassifier](mllogisticregressionclassifier.md)
  A classifier that predicts a discrete target value as a function of data features.
- [struct MLSupportVectorClassifier](mlsupportvectorclassifier.md)
  A classifier that predicts a binary target value by maximizing the separation between categories.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlclassifier/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlclassifier/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlclassifier/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Creating a Model from Tabular Data](creating_a_model_from_tabular_data.md)
  Train a machine learning model by using Core ML to import and manage tabular data.
- [enum MLRegressor](mlregressor.md)
  A model you train to estimate continuous values.
- [struct MLRecommender](mlrecommender.md)
  A model you train to make recommendations based on item similarity, grouping, and, optionally, item ratings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlclassifier)*