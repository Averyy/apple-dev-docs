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

### Creating and training a logistic regression classifier
- [init(checkpoint: MLCheckpoint) throws](mllogisticregressionclassifier/init(checkpoint:).md)
  Creates a logistic regression classifier from a checkpoint.
- [init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLLogisticRegressionClassifier.ModelParameters) throws](mllogisticregressionclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:)-3ilkk.md)
  Creates a logistic regression classifier.
- [init(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLLogisticRegressionClassifier.ModelParameters) throws](mllogisticregressionclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:)-7xy2g.md)
  Creates a Logistic Regression Classifier from the feature columns in the training data to predict the categories in the target column.
- [static func train(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLLogisticRegressionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLLogisticRegressionClassifier>](mllogisticregressionclassifier/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-1jn01.md)
  Trains a logistic regression classifier.
- [static func train(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLLogisticRegressionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLLogisticRegressionClassifier>](mllogisticregressionclassifier/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-8vpa1.md)
  Trains a logistic regression classifier.
- [static func makeTrainingSession(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLLogisticRegressionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLLogisticRegressionClassifier>](mllogisticregressionclassifier/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-4anyg.md)
  Creates or restores a training session.
- [static func makeTrainingSession(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLLogisticRegressionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLLogisticRegressionClassifier>](mllogisticregressionclassifier/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-7l7f0.md)
  Creates or restores a training session.
- [static func resume(MLTrainingSession<MLLogisticRegressionClassifier>) throws -> MLJob<MLLogisticRegressionClassifier>](mllogisticregressionclassifier/resume(_:).md)
  Resumes a training session from the last checkpoint if available.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLLogisticRegressionClassifier>](mllogisticregressionclassifier/restoretrainingsession(sessionparameters:).md)
  Restores an existing training session.
- [MLLogisticRegressionClassifier.ModelParameters](mllogisticregressionclassifier/modelparameters-swift.struct.md)
  Parameters that affect the process of training a model.
- [let modelParameters: MLLogisticRegressionClassifier.ModelParameters](mllogisticregressionclassifier/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
- [var targetColumn: String](mllogisticregressionclassifier/targetcolumn.md)
  The name of the column you selected at initialization to define which categories the classifier predicts.
- [var featureColumns: [String]](mllogisticregressionclassifier/featurecolumns.md)
  The names of the columns you selected at initialization to train the classifier.
### Assessing model accuracy
- [var trainingMetrics: MLClassifierMetrics](mllogisticregressionclassifier/trainingmetrics.md)
  Measurements of the classifier’s performance on the training data set.
- [var validationMetrics: MLClassifierMetrics](mllogisticregressionclassifier/validationmetrics.md)
  Measurements of the classifier’s performance on the validation data set.
### Evaluating a logistic regression classifier
- [func evaluation(on: DataFrame) -> MLClassifierMetrics](mllogisticregressionclassifier/evaluation(on:)-55vpv.md)
  Evaluates the classifier on the provided labeled data.
- [func evaluation(on: MLDataTable) -> MLClassifierMetrics](mllogisticregressionclassifier/evaluation(on:)-8v2xt.md)
  Evaluates the classifier on the provided labeled data.
### Testing a logistic regression classifier
- [func predictions(from: DataFrame) throws -> AnyColumn](mllogisticregressionclassifier/predictions(from:)-3hmro.md)
  Predicts a column of labels for the given testing data.
- [func predictions(from: MLDataTable) throws -> MLUntypedColumn](mllogisticregressionclassifier/predictions(from:)-80abo.md)
  Classifies the provided data into the target categories.
### Saving a logistic regression classifier
- [func write(to: URL, metadata: MLModelMetadata?) throws](mllogisticregressionclassifier/write(to:metadata:).md)
  Exports a Core ML model file for use in your app.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](mllogisticregressionclassifier/write(tofile:metadata:).md)
  Exports a Core ML model file for use in your app.
### Describing a logistic regression classifier
- [var model: MLModel](mllogisticregressionclassifier/model.md)
  The Core ML model.
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