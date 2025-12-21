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

### Training a boosted tree regressor asynchronously
- [static train(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)](mlboostedtreeregressor/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:).md)
  Trains a boosted tree regressor.
- [static makeTrainingSession(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)](mlboostedtreeregressor/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:).md)
  Creates or restores a training session.
- [static func resume(MLTrainingSession<MLBoostedTreeRegressor>) throws -> MLJob<MLBoostedTreeRegressor>](mlboostedtreeregressor/resume(_:).md)
  Resumes a training session from the last checkpoint if available.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLBoostedTreeRegressor>](mlboostedtreeregressor/restoretrainingsession(sessionparameters:).md)
  Restores an existing training session.
### Creating a boosted tree regressor from a checkpoint
- [init(checkpoint: MLCheckpoint) throws](mlboostedtreeregressor/init(checkpoint:).md)
  Creates a boosted tree regressor  from a checkpoint.
### Training a boosted tree regressor synchronously
- [init(trainingData:targetColumn:featureColumns:parameters:)](mlboostedtreeregressor/init(trainingdata:targetcolumn:featurecolumns:parameters:).md)
  Creates a boosted tree regressor.
- [var targetColumn: String](mlboostedtreeregressor/targetcolumn.md)
  The name of the column you selected at initialization to define which feature the regressor predicts.
- [var featureColumns: [String]](mlboostedtreeregressor/featurecolumns.md)
  The names of the columns you selected at initialization to train the regressor.
### Evaluating a boosted tree regressor
- [func evaluation(on:)](mlboostedtreeregressor/evaluation(on:).md)
  Evaluates the classifier on the provided labeled data.
- [var trainingMetrics: MLRegressorMetrics](mlboostedtreeregressor/trainingmetrics.md)
  Measurements of the regressor’s performance on the training data set.
- [var validationMetrics: MLRegressorMetrics](mlboostedtreeregressor/validationmetrics.md)
  Measurements of the regressor’s performance on the validation data set.
### Testing a boosted tree regressor
- [func predictions(from:)](mlboostedtreeregressor/predictions(from:).md)
  Predicts a column of labels for the given testing data.
### Saving a boosted tree regressor
- [func write(to: URL, metadata: MLModelMetadata?) throws](mlboostedtreeregressor/write(to:metadata:).md)
  Exports a Core ML model file for use in your app.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](mlboostedtreeregressor/write(tofile:metadata:).md)
  Exports a Core ML model file for use in your app.
### Inspecting a boosted tree regressor
- [var model: MLModel](mlboostedtreeregressor/model.md)
  The Core ML model.
- [MLBoostedTreeRegressor.ModelParameters](mlboostedtreeregressor/modelparameters-swift.struct.md)
  Parameters that affect the process of training a model.
- [let modelParameters: MLBoostedTreeRegressor.ModelParameters](mlboostedtreeregressor/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
### Describing a boosted tree regressor
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
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct MLLinearRegressor](mllinearregressor.md)
  A regressor that estimates the target as a linear function of the features.
- [struct MLDecisionTreeRegressor](mldecisiontreeregressor.md)
  A regressor that estimates the target by learning rules to split the data.
- [struct MLRandomForestRegressor](mlrandomforestregressor.md)
  A regressor based on a collection of decision trees trained on subsets of the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlboostedtreeregressor)*