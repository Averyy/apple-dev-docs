# MLBoostedTreeClassifier

**Framework**: Create ML  
**Kind**: struct

A classifier based on a collection of decision trees combined with gradient boosting.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct MLBoostedTreeClassifier
```

#### Overview

A boosted tree classifier combines several [`MLDecisionTreeClassifier`](mldecisiontreeclassifier.md) models (a technique known as ) by training each model to correct the errors of the preceding model.

This model is useful for handling numerical and categorical features, but is less suitable for sparse data such as text.

## Topics

### Creating and training a boosted tree classifier
- [init(checkpoint: MLCheckpoint) throws](mlboostedtreeclassifier/init(checkpoint:).md)
  Creates a boosted tree classifier from a checkpoint.
- [init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLBoostedTreeClassifier.ModelParameters) throws](mlboostedtreeclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:)-11dpb.md)
  Creates a boosted tree classifier.
- [static func makeTrainingSession(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLBoostedTreeClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLBoostedTreeClassifier>](mlboostedtreeclassifier/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-334sj.md)
  Creates or restores a training session.
- [static func makeTrainingSession(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLBoostedTreeClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLBoostedTreeClassifier>](mlboostedtreeclassifier/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-7et81.md)
  Creates or restores a training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLBoostedTreeClassifier>](mlboostedtreeclassifier/restoretrainingsession(sessionparameters:).md)
  Restores an existing training session.
- [static func resume(MLTrainingSession<MLBoostedTreeClassifier>) throws -> MLJob<MLBoostedTreeClassifier>](mlboostedtreeclassifier/resume(_:).md)
  Resumes a training session from the last checkpoint if available.
- [static func train(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLBoostedTreeClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLBoostedTreeClassifier>](mlboostedtreeclassifier/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-79pib.md)
  Trains a boosted tree classifier.
- [static func train(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLBoostedTreeClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLBoostedTreeClassifier>](mlboostedtreeclassifier/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-9sfj7.md)
  Trains a boosted tree classifier.
- [init(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLBoostedTreeClassifier.ModelParameters) throws](mlboostedtreeclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:)-8w2dm.md)
  Creates a Boosted Tree Classifier from the feature columns in the training data to predict the categories in the target column.
- [MLBoostedTreeClassifier.ModelParameters](mlboostedtreeclassifier/modelparameters-swift.struct.md)
  Parameters that affect the process of training a model.
- [let modelParameters: MLBoostedTreeClassifier.ModelParameters](mlboostedtreeclassifier/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
- [var targetColumn: String](mlboostedtreeclassifier/targetcolumn.md)
  The name of the column you selected at initialization to define which categories the classifier predicts.
- [var featureColumns: [String]](mlboostedtreeclassifier/featurecolumns.md)
  The names of the columns you selected at initialization to train the classifier.
### Assessing model accuracy
- [var trainingMetrics: MLClassifierMetrics](mlboostedtreeclassifier/trainingmetrics.md)
  Measurements of the classifier’s performance on the training data set.
- [var validationMetrics: MLClassifierMetrics](mlboostedtreeclassifier/validationmetrics.md)
  Measurements of the classifier’s performance on the validation data set.
### Evaluating the boosted tree classifier
- [func evaluation(on: DataFrame) -> MLClassifierMetrics](mlboostedtreeclassifier/evaluation(on:)-4wlw0.md)
  Evaluates the classifier on the provided labeled data.
- [func evaluation(on: MLDataTable) -> MLClassifierMetrics](mlboostedtreeclassifier/evaluation(on:)-4uhu9.md)
  Evaluates the classifier on the provided labeled data.
### Testing a boosted tree classifier
- [func predictions(from: DataFrame) throws -> AnyColumn](mlboostedtreeclassifier/predictions(from:)-6i6d5.md)
  Predicts a column of labels for the given testing data.
- [func predictions(from: MLDataTable) throws -> MLUntypedColumn](mlboostedtreeclassifier/predictions(from:)-17rgd.md)
  Classifies the provided data into the target categories.
### Saving a boosted tree classifier
- [func write(to: URL, metadata: MLModelMetadata?) throws](mlboostedtreeclassifier/write(to:metadata:).md)
  Exports a Core ML model file for use in your app.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](mlboostedtreeclassifier/write(tofile:metadata:).md)
  Exports a Core ML model file for use in your app.
### Describing a boosted tree classifier
- [var model: MLModel](mlboostedtreeclassifier/model.md)
  The Core ML model.
- [var description: String](mlboostedtreeclassifier/description.md)
  A text representation of the boosted tree classifier.
- [var debugDescription: String](mlboostedtreeclassifier/debugdescription.md)
  A text representation of the boosted tree classifier that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlboostedtreeclassifier/playgrounddescription.md)
  A description of the boosted tree classifier shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlboostedtreeclassifier/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlboostedtreeclassifier/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlboostedtreeclassifier/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct MLDecisionTreeClassifier](mldecisiontreeclassifier.md)
  A classifier that predicts the target by creating rules to split the data.
- [struct MLRandomForestClassifier](mlrandomforestclassifier.md)
  A classifier based on a collection of decision trees trained on subsets of the data.
- [struct MLLogisticRegressionClassifier](mllogisticregressionclassifier.md)
  A classifier that predicts a discrete target value as a function of data features.
- [struct MLSupportVectorClassifier](mlsupportvectorclassifier.md)
  A classifier that predicts a binary target value by maximizing the separation between categories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlboostedtreeclassifier)*