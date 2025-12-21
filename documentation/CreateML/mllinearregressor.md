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

### Creating a linear regressor asynchronously
- [static train(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)](mllinearregressor/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:).md)
  Trains a linear regressor.
- [static makeTrainingSession(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)](mllinearregressor/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:).md)
  Creates or restores a training session.
- [static func resume(MLTrainingSession<MLLinearRegressor>) throws -> MLJob<MLLinearRegressor>](mllinearregressor/resume(_:).md)
  Resumes a training session from the last checkpoint if available.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLLinearRegressor>](mllinearregressor/restoretrainingsession(sessionparameters:).md)
  Restores an existing training session.
### Creating a linear regressor from a checkpoint
- [init(checkpoint: MLCheckpoint) throws](mllinearregressor/init(checkpoint:).md)
  Creates a linear regressor from a checkpoint.
### Training a linear regressor synchronously
- [init(trainingData:targetColumn:featureColumns:parameters:)](mllinearregressor/init(trainingdata:targetcolumn:featurecolumns:parameters:).md)
  Creates a linear regressor.
- [var targetColumn: String](mllinearregressor/targetcolumn.md)
  The name of the column you selected at initialization to define which feature the regressor predicts.
- [var featureColumns: [String]](mllinearregressor/featurecolumns.md)
  The names of the columns you selected at initialization to train the regressor.
### Evaluating a linear regressor
- [func evaluation(on:)](mllinearregressor/evaluation(on:).md)
  Evaluates the classifier on the provided labeled data.
- [var trainingMetrics: MLRegressorMetrics](mllinearregressor/trainingmetrics.md)
  Measurements of the regressor’s performance on the training data set.
- [var validationMetrics: MLRegressorMetrics](mllinearregressor/validationmetrics.md)
  Measurements of the regressor’s performance on the validation data set.
### Testing a linear regressor
- [func predictions(from:)](mllinearregressor/predictions(from:).md)
  Predicts a column of labels for the given testing data.
### Saving a linear regressor
- [func write(to: URL, metadata: MLModelMetadata?) throws](mllinearregressor/write(to:metadata:).md)
  Exports a Core ML model file for use in your app.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](mllinearregressor/write(tofile:metadata:).md)
  Exports a Core ML model file for use in your app.
### Inspecting a linear regressor
- [var model: MLModel](mllinearregressor/model.md)
  The Core ML model.
- [MLLinearRegressor.ModelParameters](mllinearregressor/modelparameters-swift.struct.md)
  Parameters that affect the process of training a model.
- [let modelParameters: MLLinearRegressor.ModelParameters](mllinearregressor/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
### Describing a linear regressor
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