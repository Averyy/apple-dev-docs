# MLBoostedTreeRegressor

**Framework**: Create ML  
**Kind**: struct  
**Role**: Structure

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
- [static train(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)](./mlboostedtreeregressor/train%28trainingdata,targetcolumn,featurecolumns,parameters,sessionparameters%29.md)
  Trains a boosted tree regressor.
- [static makeTrainingSession(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)](./mlboostedtreeregressor/maketrainingsession%28trainingdata,targetcolumn,featurecolumns,parameters,sessionparameters%29.md)
  Creates or restores a training session.
- [static func resume(MLTrainingSession<MLBoostedTreeRegressor>) throws -> MLJob<MLBoostedTreeRegressor>](./mlboostedtreeregressor/resume%28_%29.md)
  Resumes a training session from the last checkpoint if available.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLBoostedTreeRegressor>](./mlboostedtreeregressor/restoretrainingsession%28sessionparameters%29.md)
  Restores an existing training session.
### Creating a boosted tree regressor from a checkpoint
- [init(checkpoint: MLCheckpoint) throws](./mlboostedtreeregressor/init%28checkpoint%29.md)
  Creates a boosted tree regressor  from a checkpoint.
### Training a boosted tree regressor synchronously
- [init(trainingData:targetColumn:featureColumns:parameters:)](./mlboostedtreeregressor/init%28trainingdata,targetcolumn,featurecolumns,parameters%29.md)
  Creates a boosted tree regressor.
- [var targetColumn: String](./mlboostedtreeregressor/targetcolumn.md)
  The name of the column you selected at initialization to define which feature the regressor predicts.
- [var featureColumns: [String]](./mlboostedtreeregressor/featurecolumns.md)
  The names of the columns you selected at initialization to train the regressor.
### Evaluating a boosted tree regressor
- [func evaluation(on:)](./mlboostedtreeregressor/evaluation%28on%29.md)
  Evaluates the classifier on the provided labeled data.
- [var trainingMetrics: MLRegressorMetrics](./mlboostedtreeregressor/trainingmetrics.md)
  Measurements of the regressor’s performance on the training data set.
- [var validationMetrics: MLRegressorMetrics](./mlboostedtreeregressor/validationmetrics.md)
  Measurements of the regressor’s performance on the validation data set.
### Testing a boosted tree regressor
- [func predictions(from:)](./mlboostedtreeregressor/predictions%28from%29.md)
  Predicts a column of labels for the given testing data.
### Saving a boosted tree regressor
- [func write(to: URL, metadata: MLModelMetadata?) throws](./mlboostedtreeregressor/write%28to,metadata%29.md)
  Exports a Core ML model file for use in your app.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](./mlboostedtreeregressor/write%28tofile,metadata%29.md)
  Exports a Core ML model file for use in your app.
### Inspecting a boosted tree regressor
- [var model: MLModel](./mlboostedtreeregressor/model.md)
  The Core ML model.
- [MLBoostedTreeRegressor.ModelParameters](./mlboostedtreeregressor/modelparameters-swift.struct.md)
  Parameters that affect the process of training a model.
- [let modelParameters: MLBoostedTreeRegressor.ModelParameters](./mlboostedtreeregressor/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
### Describing a boosted tree regressor
- [var description: String](./mlboostedtreeregressor/description.md)
  A text representation of the boosted tree regressor.
- [var debugDescription: String](./mlboostedtreeregressor/debugdescription.md)
  A text representation of the boosted tree regressor that’s suitable for output during debugging.
- [var playgroundDescription: Any](./mlboostedtreeregressor/playgrounddescription.md)
  A description of the boosted tree regressor shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./mlboostedtreeregressor/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](./mlboostedtreeregressor/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](./mlboostedtreeregressor/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/customplaygrounddisplayconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Escapable](../Swift/escapable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Supporting regressor types
- [struct MLLinearRegressor](./mllinearregressor.md)
  A regressor that estimates the target as a linear function of the features.
- [struct MLDecisionTreeRegressor](./mldecisiontreeregressor.md)
  A regressor that estimates the target by learning rules to split the data.
- [struct MLRandomForestRegressor](./mlrandomforestregressor.md)
  A regressor based on a collection of decision trees trained on subsets of the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlboostedtreeregressor)*