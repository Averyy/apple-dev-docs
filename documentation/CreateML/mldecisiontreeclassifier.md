# MLDecisionTreeClassifier

**Framework**: Create ML  
**Kind**: struct

A classifier that predicts the target by creating rules to split the data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct MLDecisionTreeClassifier
```

## Topics

### Creating and training a decision tree classifier
- [init(checkpoint: MLCheckpoint) throws](mldecisiontreeclassifier/init(checkpoint:).md)
  Creates a decision tree classifier classifier  from a checkpoint.
- [init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLDecisionTreeClassifier.ModelParameters) throws](mldecisiontreeclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:)-3dvkw.md)
  Creates a decision tree classifier.
- [static func makeTrainingSession(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLDecisionTreeClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLDecisionTreeClassifier>](mldecisiontreeclassifier/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-1cgxc.md)
  Creates or restores a training session.
- [static func makeTrainingSession(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLDecisionTreeClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLDecisionTreeClassifier>](mldecisiontreeclassifier/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-73z9l.md)
  Creates or restores a training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLDecisionTreeClassifier>](mldecisiontreeclassifier/restoretrainingsession(sessionparameters:).md)
  Restores an existing training session.
- [static func resume(MLTrainingSession<MLDecisionTreeClassifier>) throws -> MLJob<MLDecisionTreeClassifier>](mldecisiontreeclassifier/resume(_:).md)
  Resumes a training session from the last checkpoint if available.
- [static func train(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLDecisionTreeClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLDecisionTreeClassifier>](mldecisiontreeclassifier/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-4155u.md)
  Trains a decision tree classifier.
- [static func train(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLDecisionTreeClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLDecisionTreeClassifier>](mldecisiontreeclassifier/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-50xr2.md)
  Trains a decision tree classifier.
- [init(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLDecisionTreeClassifier.ModelParameters) throws](mldecisiontreeclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:)-hmwt.md)
  Creates a Decision Tree Classifier from the feature columns in the training data to predict the categories in the target column.
- [MLDecisionTreeClassifier.ModelParameters](mldecisiontreeclassifier/modelparameters-swift.struct.md)
  Parameters that affect the process of training a model.
- [let modelParameters: MLDecisionTreeClassifier.ModelParameters](mldecisiontreeclassifier/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
- [var targetColumn: String](mldecisiontreeclassifier/targetcolumn.md)
  The name of the column you selected at initialization to define which categories the classifier predicts.
- [var featureColumns: [String]](mldecisiontreeclassifier/featurecolumns.md)
  The names of the columns you selected at initialization to train the classifier.
### Assessing model accuracy
- [var trainingMetrics: MLClassifierMetrics](mldecisiontreeclassifier/trainingmetrics.md)
  Measurements of the classifier’s performance on the training data set.
- [var validationMetrics: MLClassifierMetrics](mldecisiontreeclassifier/validationmetrics.md)
  Measurements of the classifier’s performance on the validation data set.
### Evaluating a decision tree classifier
- [func evaluation(on: DataFrame) -> MLClassifierMetrics](mldecisiontreeclassifier/evaluation(on:)-86lng.md)
  Evaluates the classifier on the provided labeled data.
- [func evaluation(on: MLDataTable) -> MLClassifierMetrics](mldecisiontreeclassifier/evaluation(on:)-69gvl.md)
  Evaluates the classifier on the provided labeled data.
### Testing a decision tree classifier
- [func predictions(from: DataFrame) throws -> AnyColumn](mldecisiontreeclassifier/predictions(from:)-2clno.md)
  Predicts a column of labels for the given testing data.
- [func predictions(from: MLDataTable) throws -> MLUntypedColumn](mldecisiontreeclassifier/predictions(from:)-2di6j.md)
  Classifies the provided data into the target categories.
### Saving a decision tree classifier
- [func write(to: URL, metadata: MLModelMetadata?) throws](mldecisiontreeclassifier/write(to:metadata:).md)
  Exports a Core ML model file for use in your app.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](mldecisiontreeclassifier/write(tofile:metadata:).md)
  Exports a Core ML model file for use in your app.
### Describing a decision tree classifier
- [var model: MLModel](mldecisiontreeclassifier/model.md)
  The Core ML model.
- [var description: String](mldecisiontreeclassifier/description.md)
  A text representation of the decision tree classifier.
- [var debugDescription: String](mldecisiontreeclassifier/debugdescription.md)
  A text representation of the decision tree classifier that’s suitable for output during debugging.
- [var playgroundDescription: Any](mldecisiontreeclassifier/playgrounddescription.md)
  A description of the decision tree classifier shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mldecisiontreeclassifier/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mldecisiontreeclassifier/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mldecisiontreeclassifier/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct MLRandomForestClassifier](mlrandomforestclassifier.md)
  A classifier based on a collection of decision trees trained on subsets of the data.
- [struct MLBoostedTreeClassifier](mlboostedtreeclassifier.md)
  A classifier based on a collection of decision trees combined with gradient boosting.
- [struct MLLogisticRegressionClassifier](mllogisticregressionclassifier.md)
  A classifier that predicts a discrete target value as a function of data features.
- [struct MLSupportVectorClassifier](mlsupportvectorclassifier.md)
  A classifier that predicts a binary target value by maximizing the separation between categories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldecisiontreeclassifier)*