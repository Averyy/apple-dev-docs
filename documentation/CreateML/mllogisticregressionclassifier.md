# MLLogisticRegressionClassifier

**Framework**: Create ML  
**Kind**: struct

A classifier that predicts a discrete target value as a function of data features.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct MLLogisticRegressionClassifier
```

## Topics

### Training a logistic regression classifier asynchronously
- [static train(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)](mllogisticregressionclassifier/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:).md)
  Trains a logistic regression classifier.
- [static makeTrainingSession(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)](mllogisticregressionclassifier/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:).md)
  Creates or restores a training session.
- [static func resume(MLTrainingSession<MLLogisticRegressionClassifier>) throws -> MLJob<MLLogisticRegressionClassifier>](mllogisticregressionclassifier/resume(_:).md)
  Resumes a training session from the last checkpoint if available.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLLogisticRegressionClassifier>](mllogisticregressionclassifier/restoretrainingsession(sessionparameters:).md)
  Restores an existing training session.
### Creating a logistic regression classifier from a checkpoint
- [init(checkpoint: MLCheckpoint) throws](mllogisticregressionclassifier/init(checkpoint:).md)
  Creates a logistic regression classifier from a checkpoint.
### Training a logistic regression classifier synchronously
- [init(trainingData:targetColumn:featureColumns:parameters:)](mllogisticregressionclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:).md)
  Creates a logistic regression classifier.
- [var targetColumn: String](mllogisticregressionclassifier/targetcolumn.md)
  The name of the column you selected at initialization to define which categories the classifier predicts.
- [var featureColumns: [String]](mllogisticregressionclassifier/featurecolumns.md)
  The names of the columns you selected at initialization to train the classifier.
### Evaluating a logistic regression classifier
- [func evaluation(on:)](mllogisticregressionclassifier/evaluation(on:).md)
  Evaluates the classifier on the provided labeled data.
- [var trainingMetrics: MLClassifierMetrics](mllogisticregressionclassifier/trainingmetrics.md)
  Measurements of the classifier’s performance on the training data set.
- [var validationMetrics: MLClassifierMetrics](mllogisticregressionclassifier/validationmetrics.md)
  Measurements of the classifier’s performance on the validation data set.
### Testing a logistic regression classifier
- [func predictions(from:)](mllogisticregressionclassifier/predictions(from:).md)
  Predicts a column of labels for the given testing data.
### Saving a logistic regression classifier
- [func write(to: URL, metadata: MLModelMetadata?) throws](mllogisticregressionclassifier/write(to:metadata:).md)
  Exports a Core ML model file for use in your app.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](mllogisticregressionclassifier/write(tofile:metadata:).md)
  Exports a Core ML model file for use in your app.
### Inspecting a boosted tree classifier
- [var model: MLModel](mllogisticregressionclassifier/model.md)
  The Core ML model.
- [MLLogisticRegressionClassifier.ModelParameters](mllogisticregressionclassifier/modelparameters-swift.struct.md)
  Parameters that affect the process of training a model.
- [let modelParameters: MLLogisticRegressionClassifier.ModelParameters](mllogisticregressionclassifier/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
### Describing a logistic regression classifier
- [var description: String](mllogisticregressionclassifier/description.md)
  A text representation of the logistic regression classifier.
- [var debugDescription: String](mllogisticregressionclassifier/debugdescription.md)
  A text representation of the logistic regression classifier that’s suitable for output during debugging.
- [var playgroundDescription: Any](mllogisticregressionclassifier/playgrounddescription.md)
  A description of the logistic regression classifier shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mllogisticregressionclassifier/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mllogisticregressionclassifier/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mllogisticregressionclassifier/customstringconvertible-implementations.md)

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
- [struct MLBoostedTreeClassifier](mlboostedtreeclassifier.md)
  A classifier based on a collection of decision trees combined with gradient boosting.
- [struct MLSupportVectorClassifier](mlsupportvectorclassifier.md)
  A classifier that predicts a binary target value by maximizing the separation between categories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mllogisticregressionclassifier)*