# MLDecisionTreeRegressor

**Framework**: Create ML  
**Kind**: struct

A regressor that estimates the target by learning rules to split the data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct MLDecisionTreeRegressor
```

## Topics

### Creating and training a decision tree regressor
- [init(checkpoint: MLCheckpoint) throws](mldecisiontreeregressor/init(checkpoint:).md)
  Creates a decision tree regressor  from a checkpoint.
- [init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLDecisionTreeRegressor.ModelParameters) throws](mldecisiontreeregressor/init(trainingdata:targetcolumn:featurecolumns:parameters:)-5ugec.md)
  Creates a decision tree regressor.
- [static func makeTrainingSession(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLDecisionTreeRegressor.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLDecisionTreeRegressor>](mldecisiontreeregressor/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-69up6.md)
  Creates or restores a training session.
- [static func makeTrainingSession(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLDecisionTreeRegressor.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLDecisionTreeRegressor>](mldecisiontreeregressor/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-9ginr.md)
  Creates or restores a training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLDecisionTreeRegressor>](mldecisiontreeregressor/restoretrainingsession(sessionparameters:).md)
  Restores an existing training session.
- [static func resume(MLTrainingSession<MLDecisionTreeRegressor>) throws -> MLJob<MLDecisionTreeRegressor>](mldecisiontreeregressor/resume(_:).md)
  Resumes a training session from the last checkpoint if available.
- [static func train(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLDecisionTreeRegressor.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLDecisionTreeRegressor>](mldecisiontreeregressor/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-5l3pj.md)
  Trains a decision tree regressor.
- [static func train(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLDecisionTreeRegressor.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLDecisionTreeRegressor>](mldecisiontreeregressor/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-6ldjt.md)
  Trains a decision tree regressor.
- [init(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLDecisionTreeRegressor.ModelParameters) throws](mldecisiontreeregressor/init(trainingdata:targetcolumn:featurecolumns:parameters:)-7cjvn.md)
  Creates a Decision Tree Regressor from the feature columns in the training data to predict the values in the target column.
- [MLDecisionTreeRegressor.ModelParameters](mldecisiontreeregressor/modelparameters-swift.struct.md)
  Parameters that affect the process of training a model.
- [let modelParameters: MLDecisionTreeRegressor.ModelParameters](mldecisiontreeregressor/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
- [var targetColumn: String](mldecisiontreeregressor/targetcolumn.md)
  The name of the column you selected at initialization to define which feature the regressor predicts.
- [var featureColumns: [String]](mldecisiontreeregressor/featurecolumns.md)
  The names of the columns you selected at initialization to train the regressor.
### Assessing model accuracy
- [var trainingMetrics: MLRegressorMetrics](mldecisiontreeregressor/trainingmetrics.md)
  Measurements of the regressor’s performance on the training data set.
- [var validationMetrics: MLRegressorMetrics](mldecisiontreeregressor/validationmetrics.md)
  Measurements of the regressor’s performance on the validation data set.
### Evaluating a decision tree regressor
- [func evaluation(on: DataFrame) -> MLRegressorMetrics](mldecisiontreeregressor/evaluation(on:)-8uw90.md)
  Evaluates the classifier on the provided labeled data.
- [func evaluation(on: MLDataTable) -> MLRegressorMetrics](mldecisiontreeregressor/evaluation(on:)-7zk9x.md)
  Evaluates the classifier on the provided labeled data.
### Testing a decision tree regressor
- [func predictions(from: DataFrame) throws -> AnyColumn](mldecisiontreeregressor/predictions(from:)-8kcfl.md)
  Predicts a column of labels for the given testing data.
- [func predictions(from: MLDataTable) throws -> MLUntypedColumn](mldecisiontreeregressor/predictions(from:)-20026.md)
  Predicts the target value from the provided data.
### Saving a decision tree regressor
- [func write(to: URL, metadata: MLModelMetadata?) throws](mldecisiontreeregressor/write(to:metadata:).md)
  Exports a Core ML model file for use in your app.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](mldecisiontreeregressor/write(tofile:metadata:).md)
  Exports a Core ML model file for use in your app.
### Describing a decision tree regressor
- [var model: MLModel](mldecisiontreeregressor/model.md)
  The Core ML model.
- [var description: String](mldecisiontreeregressor/description.md)
  A text representation of the decision tree regressor.
- [var debugDescription: String](mldecisiontreeregressor/debugdescription.md)
  A text representation of the decision tree regressor that’s suitable for output during debugging.
- [var playgroundDescription: Any](mldecisiontreeregressor/playgrounddescription.md)
  A description of the decision tree regressor shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mldecisiontreeregressor/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mldecisiontreeregressor/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mldecisiontreeregressor/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct MLLinearRegressor](mllinearregressor.md)
  A regressor that estimates the target as a linear function of the features.
- [struct MLRandomForestRegressor](mlrandomforestregressor.md)
  A regressor based on a collection of decision trees trained on subsets of the data.
- [struct MLBoostedTreeRegressor](mlboostedtreeregressor.md)
  A regressor based on a collection of decision trees combined with gradient boosting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldecisiontreeregressor)*