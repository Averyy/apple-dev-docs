# MLRandomForestRegressor

**Framework**: Create ML  
**Kind**: struct

A regressor based on a collection of decision trees trained on subsets of the data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct MLRandomForestRegressor
```

## Topics

### Creating and Training a Random Forest Regressor
- [init(checkpoint: MLCheckpoint) throws](mlrandomforestregressor/init(checkpoint:).md)
  Creates a random forest regressor  from a checkpoint.
- [init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLRandomForestRegressor.ModelParameters) throws](mlrandomforestregressor/init(trainingdata:targetcolumn:featurecolumns:parameters:)-7ep5e.md)
  Creates a random tree regressor.
- [static func makeTrainingSession(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLRandomForestRegressor.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLRandomForestRegressor>](mlrandomforestregressor/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-3e9dp.md)
  Creates or restores a training session.
- [static func makeTrainingSession(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLRandomForestRegressor.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLRandomForestRegressor>](mlrandomforestregressor/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-8ds4f.md)
  Creates or restores a training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLRandomForestRegressor>](mlrandomforestregressor/restoretrainingsession(sessionparameters:).md)
  Restores an existing training session.
- [static func resume(MLTrainingSession<MLRandomForestRegressor>) throws -> MLJob<MLRandomForestRegressor>](mlrandomforestregressor/resume(_:).md)
  Resumes a training session from the last checkpoint if available.
- [static func train(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLRandomForestRegressor.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLRandomForestRegressor>](mlrandomforestregressor/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-4mev0.md)
  Trains a random forest regressor.
- [static func train(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLRandomForestRegressor.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLRandomForestRegressor>](mlrandomforestregressor/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-7axdk.md)
  Trains a random forest regressor.
- [init(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLRandomForestRegressor.ModelParameters) throws](mlrandomforestregressor/init(trainingdata:targetcolumn:featurecolumns:parameters:)-9p7os.md)
  Creates a Random Forest Regressor from the feature columns in the training data to predict the values in the target column.
- [MLRandomForestRegressor.ModelParameters](mlrandomforestregressor/modelparameters-swift.struct.md)
  Parameters that affect the process of training a model.
- [let modelParameters: MLRandomForestRegressor.ModelParameters](mlrandomforestregressor/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
- [var targetColumn: String](mlrandomforestregressor/targetcolumn.md)
  The name of the column you selected at initialization to define which feature the regressor predicts.
- [var featureColumns: [String]](mlrandomforestregressor/featurecolumns.md)
  The names of the columns you selected at initialization to train the regressor.
### Assessing Model Accuracy
- [var trainingMetrics: MLRegressorMetrics](mlrandomforestregressor/trainingmetrics.md)
  Measurements of the regressor’s performance on the training data set.
- [var validationMetrics: MLRegressorMetrics](mlrandomforestregressor/validationmetrics.md)
  Measurements of the regressor’s performance on the validation data set.
### Evaluating a Random Forest Regressor
- [func evaluation(on: DataFrame) -> MLRegressorMetrics](mlrandomforestregressor/evaluation(on:)-237pc.md)
  Evaluates the classifier on the provided labeled data.
- [func evaluation(on: MLDataTable) -> MLRegressorMetrics](mlrandomforestregressor/evaluation(on:)-99j4w.md)
  Evaluates the classifier on the provided labeled data.
### Testing a Random Forest Regressor
- [func predictions(from: DataFrame) throws -> AnyColumn](mlrandomforestregressor/predictions(from:)-8s2mn.md)
  Predicts a column of labels for the given testing data.
- [func predictions(from: MLDataTable) throws -> MLUntypedColumn](mlrandomforestregressor/predictions(from:)-59u6.md)
  Predicts the target value from the provided data.
### Saving a Random Forest Regressor
- [func write(to: URL, metadata: MLModelMetadata?) throws](mlrandomforestregressor/write(to:metadata:).md)
  Exports a Core ML model file for use in your app.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](mlrandomforestregressor/write(tofile:metadata:).md)
  Exports a Core ML model file for use in your app.
### Describing a Random Forest Regressor
- [var model: MLModel](mlrandomforestregressor/model.md)
  The Core ML model.
- [var description: String](mlrandomforestregressor/description.md)
  A text representation of the random forest regressor.
- [var debugDescription: String](mlrandomforestregressor/debugdescription.md)
  A text representation of the random forest regressor that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlrandomforestregressor/playgrounddescription.md)
  A description of the random forest regressor shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlrandomforestregressor/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlrandomforestregressor/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlrandomforestregressor/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct MLLinearRegressor](mllinearregressor.md)
  A regressor that estimates the target as a linear function of the features.
- [struct MLDecisionTreeRegressor](mldecisiontreeregressor.md)
  A regressor that estimates the target by learning rules to split the data.
- [struct MLBoostedTreeRegressor](mlboostedtreeregressor.md)
  A regressor based on a collection of decision trees combined with gradient boosting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrandomforestregressor)*