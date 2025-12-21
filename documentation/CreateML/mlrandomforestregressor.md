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

### Training a random forest regressor
- [static train(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)](mlrandomforestregressor/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:).md)
  Trains a random forest regressor.
- [static makeTrainingSession(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)](mlrandomforestregressor/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:).md)
  Creates or restores a training session.
- [static func resume(MLTrainingSession<MLRandomForestRegressor>) throws -> MLJob<MLRandomForestRegressor>](mlrandomforestregressor/resume(_:).md)
  Resumes a training session from the last checkpoint if available.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLRandomForestRegressor>](mlrandomforestregressor/restoretrainingsession(sessionparameters:).md)
  Restores an existing training session.
### Creating a random forest regressor from a checkpoint
- [init(checkpoint: MLCheckpoint) throws](mlrandomforestregressor/init(checkpoint:).md)
  Creates a random forest regressor  from a checkpoint.
### Training a random forest regressor synchronously
- [init(trainingData:targetColumn:featureColumns:parameters:)](mlrandomforestregressor/init(trainingdata:targetcolumn:featurecolumns:parameters:).md)
  Creates a random tree regressor.
- [var targetColumn: String](mlrandomforestregressor/targetcolumn.md)
  The name of the column you selected at initialization to define which feature the regressor predicts.
- [var featureColumns: [String]](mlrandomforestregressor/featurecolumns.md)
  The names of the columns you selected at initialization to train the regressor.
### Evaluating a random forest regressor
- [func evaluation(on:)](mlrandomforestregressor/evaluation(on:).md)
  Evaluates the classifier on the provided labeled data.
- [var trainingMetrics: MLRegressorMetrics](mlrandomforestregressor/trainingmetrics.md)
  Measurements of the regressor’s performance on the training data set.
- [var validationMetrics: MLRegressorMetrics](mlrandomforestregressor/validationmetrics.md)
  Measurements of the regressor’s performance on the validation data set.
### Testing a Random Forest Regressor
- [func predictions(from:)](mlrandomforestregressor/predictions(from:).md)
  Predicts a column of labels for the given testing data.
### Saving a Random Forest Regressor
- [func write(to: URL, metadata: MLModelMetadata?) throws](mlrandomforestregressor/write(to:metadata:).md)
  Exports a Core ML model file for use in your app.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](mlrandomforestregressor/write(tofile:metadata:).md)
  Exports a Core ML model file for use in your app.
### Inspecting a random forest regressor
- [var model: MLModel](mlrandomforestregressor/model.md)
  The Core ML model.
- [MLRandomForestRegressor.ModelParameters](mlrandomforestregressor/modelparameters-swift.struct.md)
  Parameters that affect the process of training a model.
- [let modelParameters: MLRandomForestRegressor.ModelParameters](mlrandomforestregressor/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
### Describing a random forest regressor
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