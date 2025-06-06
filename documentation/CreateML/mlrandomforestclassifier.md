# MLRandomForestClassifier

**Framework**: Create ML  
**Kind**: struct

A classifier based on a collection of decision trees trained on subsets of the data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct MLRandomForestClassifier
```

## Topics

### Creating and training a random forest classifier
- [init(checkpoint: MLCheckpoint) throws](mlrandomforestclassifier/init(checkpoint:).md)
  Creates a random forest classifier classifier  from a checkpoint.
- [init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLRandomForestClassifier.ModelParameters) throws](mlrandomforestclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:)-5nojh.md)
  Creates a random forest classifier.
- [init(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLRandomForestClassifier.ModelParameters) throws](mlrandomforestclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:)-4pxej.md)
  Creates a Random Forest Classifier from the feature columns in the training data to predict the categories in the target column.
- [MLRandomForestClassifier.ModelParameters](mlrandomforestclassifier/modelparameters-swift.struct.md)
  Parameters that affect the process of training a model.
- [let modelParameters: MLRandomForestClassifier.ModelParameters](mlrandomforestclassifier/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
- [var targetColumn: String](mlrandomforestclassifier/targetcolumn.md)
  The name of the column you selected at initialization to define which categories the classifier predicts.
- [var featureColumns: [String]](mlrandomforestclassifier/featurecolumns.md)
  The names of the columns you selected at initialization to train the classifier.
### Assessing model accuracy
- [var trainingMetrics: MLClassifierMetrics](mlrandomforestclassifier/trainingmetrics.md)
  Measurements of the classifier’s performance on the training data set.
- [var validationMetrics: MLClassifierMetrics](mlrandomforestclassifier/validationmetrics.md)
  Measurements of the classifier’s performance on the validation data set.
### Creating a training session
- [static func makeTrainingSession(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLRandomForestClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLRandomForestClassifier>](mlrandomforestclassifier/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-7e0li.md)
  Creates or restores a training session.
- [static func makeTrainingSession(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLRandomForestClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLRandomForestClassifier>](mlrandomforestclassifier/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-8fmoq.md)
  Creates or restores a training session.
### Restoring a training session
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLRandomForestClassifier>](mlrandomforestclassifier/restoretrainingsession(sessionparameters:).md)
  Restores an existing training session.
### Resuming a training session
- [static func resume(MLTrainingSession<MLRandomForestClassifier>) throws -> MLJob<MLRandomForestClassifier>](mlrandomforestclassifier/resume(_:).md)
  Resumes a training session from the last checkpoint if available.
### Training a random forest classifier
- [static func train(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLRandomForestClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLRandomForestClassifier>](mlrandomforestclassifier/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-1q4n7.md)
  Trains a random forest classifier.
- [static func train(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLRandomForestClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLRandomForestClassifier>](mlrandomforestclassifier/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-3teom.md)
  Trains a random forest classifier.
### Evaluating a random forest classifier
- [func evaluation(on: DataFrame) -> MLClassifierMetrics](mlrandomforestclassifier/evaluation(on:)-9nxk0.md)
  Evaluates the classifier on the provided labeled data.
- [func evaluation(on: MLDataTable) -> MLClassifierMetrics](mlrandomforestclassifier/evaluation(on:)-3w3a0.md)
  Evaluates the classifier on the provided labeled data.
### Testing a random forest classifier
- [func predictions(from: DataFrame) throws -> AnyColumn](mlrandomforestclassifier/predictions(from:)-20act.md)
  Predicts a column of labels for the given testing data.
- [func predictions(from: MLDataTable) throws -> MLUntypedColumn](mlrandomforestclassifier/predictions(from:)-9dvl3.md)
  Classifies the provided data into the target categories.
### Saving a random forest classifier
- [func write(to: URL, metadata: MLModelMetadata?) throws](mlrandomforestclassifier/write(to:metadata:).md)
  Exports a Core ML model file for use in your app.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](mlrandomforestclassifier/write(tofile:metadata:).md)
  Exports a Core ML model file for use in your app.
### Describing a random forest classifier
- [var model: MLModel](mlrandomforestclassifier/model.md)
  The Core ML model.
- [var description: String](mlrandomforestclassifier/description.md)
  A text representation of the random forest classifier.
- [var debugDescription: String](mlrandomforestclassifier/debugdescription.md)
  A text representation of the random forest classifier that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlrandomforestclassifier/playgrounddescription.md)
  A description of the random forest classifier shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlrandomforestclassifier/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlrandomforestclassifier/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlrandomforestclassifier/customstringconvertible-implementations.md)

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
- [struct MLBoostedTreeClassifier](mlboostedtreeclassifier.md)
  A classifier based on a collection of decision trees combined with gradient boosting.
- [struct MLLogisticRegressionClassifier](mllogisticregressionclassifier.md)
  A classifier that predicts a discrete target value as a function of data features.
- [struct MLSupportVectorClassifier](mlsupportvectorclassifier.md)
  A classifier that predicts a binary target value by maximizing the separation between categories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrandomforestclassifier)*