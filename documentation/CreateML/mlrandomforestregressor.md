# MLRandomForestRegressor

**Framework**: Create ML  
**Kind**: struct  
**Role**: Structure

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
- [static train(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)](./mlrandomforestregressor/train%28trainingdata,targetcolumn,featurecolumns,parameters,sessionparameters%29.md)
  Trains a random forest regressor.
- [static makeTrainingSession(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)](./mlrandomforestregressor/maketrainingsession%28trainingdata,targetcolumn,featurecolumns,parameters,sessionparameters%29.md)
  Creates or restores a training session.
- [static func resume(MLTrainingSession<MLRandomForestRegressor>) throws -> MLJob<MLRandomForestRegressor>](./mlrandomforestregressor/resume%28_%29.md)
  Resumes a training session from the last checkpoint if available.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLRandomForestRegressor>](./mlrandomforestregressor/restoretrainingsession%28sessionparameters%29.md)
  Restores an existing training session.
### Creating a random forest regressor from a checkpoint
- [init(checkpoint: MLCheckpoint) throws](./mlrandomforestregressor/init%28checkpoint%29.md)
  Creates a random forest regressor  from a checkpoint.
### Training a random forest regressor synchronously
- [init(trainingData:targetColumn:featureColumns:parameters:)](./mlrandomforestregressor/init%28trainingdata,targetcolumn,featurecolumns,parameters%29.md)
  Creates a random tree regressor.
- [var targetColumn: String](./mlrandomforestregressor/targetcolumn.md)
  The name of the column you selected at initialization to define which feature the regressor predicts.
- [var featureColumns: [String]](./mlrandomforestregressor/featurecolumns.md)
  The names of the columns you selected at initialization to train the regressor.
### Evaluating a random forest regressor
- [func evaluation(on:)](./mlrandomforestregressor/evaluation%28on%29.md)
  Evaluates the classifier on the provided labeled data.
- [var trainingMetrics: MLRegressorMetrics](./mlrandomforestregressor/trainingmetrics.md)
  Measurements of the regressor’s performance on the training data set.
- [var validationMetrics: MLRegressorMetrics](./mlrandomforestregressor/validationmetrics.md)
  Measurements of the regressor’s performance on the validation data set.
### Testing a Random Forest Regressor
- [func predictions(from:)](./mlrandomforestregressor/predictions%28from%29.md)
  Predicts a column of labels for the given testing data.
### Saving a Random Forest Regressor
- [func write(to: URL, metadata: MLModelMetadata?) throws](./mlrandomforestregressor/write%28to,metadata%29.md)
  Exports a Core ML model file for use in your app.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](./mlrandomforestregressor/write%28tofile,metadata%29.md)
  Exports a Core ML model file for use in your app.
### Inspecting a random forest regressor
- [var model: MLModel](./mlrandomforestregressor/model.md)
  The Core ML model.
- [MLRandomForestRegressor.ModelParameters](./mlrandomforestregressor/modelparameters-swift.struct.md)
  Parameters that affect the process of training a model.
- [let modelParameters: MLRandomForestRegressor.ModelParameters](./mlrandomforestregressor/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
### Describing a random forest regressor
- [var description: String](./mlrandomforestregressor/description.md)
  A text representation of the random forest regressor.
- [var debugDescription: String](./mlrandomforestregressor/debugdescription.md)
  A text representation of the random forest regressor that’s suitable for output during debugging.
- [var playgroundDescription: Any](./mlrandomforestregressor/playgrounddescription.md)
  A description of the random forest regressor shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./mlrandomforestregressor/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](./mlrandomforestregressor/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](./mlrandomforestregressor/customstringconvertible-implementations.md)

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
- [struct MLBoostedTreeRegressor](./mlboostedtreeregressor.md)
  A regressor based on a collection of decision trees combined with gradient boosting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrandomforestregressor)*