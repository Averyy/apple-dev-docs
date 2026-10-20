# MLDecisionTreeRegressor

**Framework**: Create ML  
**Kind**: struct  
**Role**: Structure

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

### Training a decision tree regressor asynchronously
- [static train(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)](./mldecisiontreeregressor/train%28trainingdata,targetcolumn,featurecolumns,parameters,sessionparameters%29.md)
  Trains a decision tree regressor.
- [static makeTrainingSession(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)](./mldecisiontreeregressor/maketrainingsession%28trainingdata,targetcolumn,featurecolumns,parameters,sessionparameters%29.md)
  Creates or restores a training session.
- [static func resume(MLTrainingSession<MLDecisionTreeRegressor>) throws -> MLJob<MLDecisionTreeRegressor>](./mldecisiontreeregressor/resume%28_%29.md)
  Resumes a training session from the last checkpoint if available.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLDecisionTreeRegressor>](./mldecisiontreeregressor/restoretrainingsession%28sessionparameters%29.md)
  Restores an existing training session.
### Creating a decision tree regressor from a checkpoint
- [init(checkpoint: MLCheckpoint) throws](./mldecisiontreeregressor/init%28checkpoint%29.md)
  Creates a decision tree regressor  from a checkpoint.
### Training a decision tree regressor synchronously
- [init(trainingData:targetColumn:featureColumns:parameters:)](./mldecisiontreeregressor/init%28trainingdata,targetcolumn,featurecolumns,parameters%29.md)
  Creates a decision tree regressor.
- [var targetColumn: String](./mldecisiontreeregressor/targetcolumn.md)
  The name of the column you selected at initialization to define which feature the regressor predicts.
- [var featureColumns: [String]](./mldecisiontreeregressor/featurecolumns.md)
  The names of the columns you selected at initialization to train the regressor.
### Evaluating a decision tree regressor
- [func evaluation(on:)](./mldecisiontreeregressor/evaluation%28on%29.md)
  Evaluates the classifier on the provided labeled data.
- [var trainingMetrics: MLRegressorMetrics](./mldecisiontreeregressor/trainingmetrics.md)
  Measurements of the regressor’s performance on the training data set.
- [var validationMetrics: MLRegressorMetrics](./mldecisiontreeregressor/validationmetrics.md)
  Measurements of the regressor’s performance on the validation data set.
### Testing a decision tree regressor
- [func predictions(from:)](./mldecisiontreeregressor/predictions%28from%29.md)
  Predicts a column of labels for the given testing data.
### Saving a decision tree regressor
- [func write(to: URL, metadata: MLModelMetadata?) throws](./mldecisiontreeregressor/write%28to,metadata%29.md)
  Exports a Core ML model file for use in your app.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](./mldecisiontreeregressor/write%28tofile,metadata%29.md)
  Exports a Core ML model file for use in your app.
### Inspecting a decision tree regressor
- [var model: MLModel](./mldecisiontreeregressor/model.md)
  The Core ML model.
- [MLDecisionTreeRegressor.ModelParameters](./mldecisiontreeregressor/modelparameters-swift.struct.md)
  Parameters that affect the process of training a model.
- [let modelParameters: MLDecisionTreeRegressor.ModelParameters](./mldecisiontreeregressor/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
### Describing a decision tree regressor
- [var description: String](./mldecisiontreeregressor/description.md)
  A text representation of the decision tree regressor.
- [var debugDescription: String](./mldecisiontreeregressor/debugdescription.md)
  A text representation of the decision tree regressor that’s suitable for output during debugging.
- [var playgroundDescription: Any](./mldecisiontreeregressor/playgrounddescription.md)
  A description of the decision tree regressor shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./mldecisiontreeregressor/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](./mldecisiontreeregressor/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](./mldecisiontreeregressor/customstringconvertible-implementations.md)

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
- [struct MLRandomForestRegressor](./mlrandomforestregressor.md)
  A regressor based on a collection of decision trees trained on subsets of the data.
- [struct MLBoostedTreeRegressor](./mlboostedtreeregressor.md)
  A regressor based on a collection of decision trees combined with gradient boosting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldecisiontreeregressor)*