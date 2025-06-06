# MLBoostedTreeRegressor

**Framework**: Create ML  
**Kind**: struct

A regressor based on a collection of decision trees combined with gradient boosting.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct MLBoostedTreeRegressor
```

## Topics

### Creating and training a boosted tree regressor
- [init(checkpoint: MLCheckpoint) throws](mlboostedtreeregressor/init(checkpoint:).md)
  Creates a boosted tree regressor  from a checkpoint.
- [init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLBoostedTreeRegressor.ModelParameters) throws](mlboostedtreeregressor/init(trainingdata:targetcolumn:featurecolumns:parameters:)-6z8wm.md)
  Creates a boosted tree regressor.
- [static func makeTrainingSession(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLBoostedTreeRegressor.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLBoostedTreeRegressor>](mlboostedtreeregressor/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-1x5hc.md)
  Creates or restores a training session.
- [static func makeTrainingSession(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLBoostedTreeRegressor.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLBoostedTreeRegressor>](mlboostedtreeregressor/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-4d0fx.md)
  Creates or restores a training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLBoostedTreeRegressor>](mlboostedtreeregressor/restoretrainingsession(sessionparameters:).md)
  Restores an existing training session.
- [static func resume(MLTrainingSession<MLBoostedTreeRegressor>) throws -> MLJob<MLBoostedTreeRegressor>](mlboostedtreeregressor/resume(_:).md)
  Resumes a training session from the last checkpoint if available.
- [static func train(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLBoostedTreeRegressor.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLBoostedTreeRegressor>](mlboostedtreeregressor/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-1razs.md)
  Trains a boosted tree regressor.
- [static func train(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLBoostedTreeRegressor.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLBoostedTreeRegressor>](mlboostedtreeregressor/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-4okyp.md)
  Trains a boosted tree regressor.
- [init(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLBoostedTreeRegressor.ModelParameters) throws](mlboostedtreeregressor/init(trainingdata:targetcolumn:featurecolumns:parameters:)-hfxs.md)
  Creates a Boosted Tree Regressor from the feature columns in the training data to predict the values in the target column.
- [MLBoostedTreeRegressor.ModelParameters](mlboostedtreeregressor/modelparameters-swift.struct.md)
  Parameters that affect the process of training a model.
- [let modelParameters: MLBoostedTreeRegressor.ModelParameters](mlboostedtreeregressor/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
- [var targetColumn: String](mlboostedtreeregressor/targetcolumn.md)
  The name of the column you selected at initialization to define which feature the regressor predicts.
- [var featureColumns: [String]](mlboostedtreeregressor/featurecolumns.md)
  The names of the columns you selected at initialization to train the regressor.
### Assessing model accuracy
- [var trainingMetrics: MLRegressorMetrics](mlboostedtreeregressor/trainingmetrics.md)
  Measurements of the regressor’s performance on the training data set.
- [var validationMetrics: MLRegressorMetrics](mlboostedtreeregressor/validationmetrics.md)
  Measurements of the regressor’s performance on the validation data set.
### Evaluating a boosted tree regressor
- [func evaluation(on: DataFrame) -> MLRegressorMetrics](mlboostedtreeregressor/evaluation(on:)-88akn.md)
  Evaluates the classifier on the provided labeled data.
- [func evaluation(on: MLDataTable) -> MLRegressorMetrics](mlboostedtreeregressor/evaluation(on:)-2tsxy.md)
  Evaluates the classifier on the provided labeled data.
### Testing a boosted tree regressor
- [func predictions(from: DataFrame) throws -> AnyColumn](mlboostedtreeregressor/predictions(from:)-5a8oi.md)
  Predicts a column of labels for the given testing data.
- [func predictions(from: MLDataTable) throws -> MLUntypedColumn](mlboostedtreeregressor/predictions(from:)-3daff.md)
  Predicts the target value from the provided data.
### Saving a boosted tree regressor
- [func write(to: URL, metadata: MLModelMetadata?) throws](mlboostedtreeregressor/write(to:metadata:).md)
  Exports a Core ML model file for use in your app.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](mlboostedtreeregressor/write(tofile:metadata:).md)
  Exports a Core ML model file for use in your app.
### Describing a boosted tree regressor
- [var model: MLModel](mlboostedtreeregressor/model.md)
  The Core ML model.
- [var description: String](mlboostedtreeregressor/description.md)
  A text representation of the boosted tree regressor.
- [var debugDescription: String](mlboostedtreeregressor/debugdescription.md)
  A text representation of the boosted tree regressor that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlboostedtreeregressor/playgrounddescription.md)
  A description of the boosted tree regressor shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlboostedtreeregressor/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlboostedtreeregressor/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlboostedtreeregressor/customstringconvertible-implementations.md)

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
- [struct MLDecisionTreeRegressor](mldecisiontreeregressor.md)
  A regressor that estimates the target by learning rules to split the data.
- [struct MLRandomForestRegressor](mlrandomforestregressor.md)
  A regressor based on a collection of decision trees trained on subsets of the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlboostedtreeregressor)*