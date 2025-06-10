# MLLinearRegressor

**Framework**: Create ML  
**Kind**: struct

A regressor that estimates the target as a linear function of the features.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct MLLinearRegressor
```

## Topics

### Creating and Training a Linear Regressor
- [init(checkpoint: MLCheckpoint) throws](mllinearregressor/init(checkpoint:).md)
  Creates a linear regressor from a checkpoint.
- [init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLLinearRegressor.ModelParameters) throws](mllinearregressor/init(trainingdata:targetcolumn:featurecolumns:parameters:)-5xpue.md)
  Creates a linear regressor.
- [static func makeTrainingSession(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLLinearRegressor.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLLinearRegressor>](mllinearregressor/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-3cosv.md)
  Creates or restores a training session.
- [static func makeTrainingSession(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLLinearRegressor.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLLinearRegressor>](mllinearregressor/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-7xqak.md)
  Creates or restores a training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLLinearRegressor>](mllinearregressor/restoretrainingsession(sessionparameters:).md)
  Restores an existing training session.
- [static func resume(MLTrainingSession<MLLinearRegressor>) throws -> MLJob<MLLinearRegressor>](mllinearregressor/resume(_:).md)
  Resumes a training session from the last checkpoint if available.
- [static func train(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLLinearRegressor.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLLinearRegressor>](mllinearregressor/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-1v1q5.md)
  Trains a linear regressor.
- [static func train(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLLinearRegressor.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLLinearRegressor>](mllinearregressor/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-7j70n.md)
  Trains a linear regressor.
- [init(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLLinearRegressor.ModelParameters) throws](mllinearregressor/init(trainingdata:targetcolumn:featurecolumns:parameters:)-5lmry.md)
  Creates a Linear Regressor from the feature columns in the training data to predict the values in the target column.
- [MLLinearRegressor.ModelParameters](mllinearregressor/modelparameters-swift.struct.md)
  Parameters that affect the process of training a model.
- [let modelParameters: MLLinearRegressor.ModelParameters](mllinearregressor/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
- [var targetColumn: String](mllinearregressor/targetcolumn.md)
  The name of the column you selected at initialization to define which feature the regressor predicts.
- [var featureColumns: [String]](mllinearregressor/featurecolumns.md)
  The names of the columns you selected at initialization to train the regressor.
### Assessing Model Accuracy
- [var trainingMetrics: MLRegressorMetrics](mllinearregressor/trainingmetrics.md)
  Measurements of the regressor’s performance on the training data set.
- [var validationMetrics: MLRegressorMetrics](mllinearregressor/validationmetrics.md)
  Measurements of the regressor’s performance on the validation data set.
### Evaluating a Linear Regressor
- [func evaluation(on: DataFrame) -> MLRegressorMetrics](mllinearregressor/evaluation(on:)-96oll.md)
  Evaluates the classifier on the provided labeled data.
- [func evaluation(on: MLDataTable) -> MLRegressorMetrics](mllinearregressor/evaluation(on:)-6pyq9.md)
  Evaluates the classifier on the provided labeled data.
### Testing a Linear Regressor
- [func predictions(from: DataFrame) throws -> AnyColumn](mllinearregressor/predictions(from:)-7mob0.md)
  Predicts a column of labels for the given testing data.
- [func predictions(from: MLDataTable) throws -> MLUntypedColumn](mllinearregressor/predictions(from:)-2gc5w.md)
  Predicts the target value from the provided data.
### Saving a Linear Regressor
- [func write(to: URL, metadata: MLModelMetadata?) throws](mllinearregressor/write(to:metadata:).md)
  Exports a Core ML model file for use in your app.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](mllinearregressor/write(tofile:metadata:).md)
  Exports a Core ML model file for use in your app.
### Describing a Linear Regressor
- [var model: MLModel](mllinearregressor/model.md)
  The Core ML model.
- [var description: String](mllinearregressor/description.md)
  A text representation of the linear regressor.
- [var debugDescription: String](mllinearregressor/debugdescription.md)
  A text representation of the linear regressor that’s suitable for output during debugging.
- [var playgroundDescription: Any](mllinearregressor/playgrounddescription.md)
  A description of the linear regressor shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mllinearregressor/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mllinearregressor/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mllinearregressor/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct MLDecisionTreeRegressor](mldecisiontreeregressor.md)
  A regressor that estimates the target by learning rules to split the data.
- [struct MLRandomForestRegressor](mlrandomforestregressor.md)
  A regressor based on a collection of decision trees trained on subsets of the data.
- [struct MLBoostedTreeRegressor](mlboostedtreeregressor.md)
  A regressor based on a collection of decision trees combined with gradient boosting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mllinearregressor)*