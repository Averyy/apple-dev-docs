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

### Training a boosted tree classifier asynchronously
- [static train(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)](mlboostedtreeclassifier/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:).md)
  Trains a boosted tree classifier.
- [static makeTrainingSession(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)](mlboostedtreeclassifier/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:).md)
  Creates or restores a training session.
- [static func resume(MLTrainingSession<MLBoostedTreeClassifier>) throws -> MLJob<MLBoostedTreeClassifier>](mlboostedtreeclassifier/resume(_:).md)
  Resumes a training session from the last checkpoint if available.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLBoostedTreeClassifier>](mlboostedtreeclassifier/restoretrainingsession(sessionparameters:).md)
  Restores an existing training session.
### Creating a boosted tree classifier from a checkpoint
- [init(checkpoint: MLCheckpoint) throws](mlboostedtreeclassifier/init(checkpoint:).md)
  Creates a boosted tree classifier from a checkpoint.
### Training a boosted tree classifier synchronously
- [init(trainingData:targetColumn:featureColumns:parameters:)](mlboostedtreeclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:).md)
  Creates a boosted tree classifier.
- [var targetColumn: String](mlboostedtreeclassifier/targetcolumn.md)
  The name of the column you selected at initialization to define which categories the classifier predicts.
- [var featureColumns: [String]](mlboostedtreeclassifier/featurecolumns.md)
  The names of the columns you selected at initialization to train the classifier.
### Evaluating a boosted tree classifier
- [func evaluation(on:)](mlboostedtreeclassifier/evaluation(on:).md)
  Evaluates the classifier on the provided labeled data.
- [var trainingMetrics: MLClassifierMetrics](mlboostedtreeclassifier/trainingmetrics.md)
  Measurements of the classifier’s performance on the training data set.
- [var validationMetrics: MLClassifierMetrics](mlboostedtreeclassifier/validationmetrics.md)
  Measurements of the classifier’s performance on the validation data set.
### Testing a boosted tree classifier
- [func predictions(from:)](mlboostedtreeclassifier/predictions(from:).md)
  Predicts a column of labels for the given testing data.
### Saving a boosted tree classifier
- [func write(to: URL, metadata: MLModelMetadata?) throws](mlboostedtreeclassifier/write(to:metadata:).md)
  Exports a Core ML model file for use in your app.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](mlboostedtreeclassifier/write(tofile:metadata:).md)
  Exports a Core ML model file for use in your app.
### Inspecting a boosted tree classifier
- [var model: MLModel](mlboostedtreeclassifier/model.md)
  The Core ML model.
- [MLBoostedTreeClassifier.ModelParameters](mlboostedtreeclassifier/modelparameters-swift.struct.md)
  Parameters that affect the process of training a model.
- [let modelParameters: MLBoostedTreeClassifier.ModelParameters](mlboostedtreeclassifier/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
### Describing a boosted tree classifier
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
- [SendableMetatype](../Swift/SendableMetatype.md)

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