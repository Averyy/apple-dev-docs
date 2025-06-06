# MLLinearRegressor.ModelParameters

**Framework**: Create ML  
**Kind**: struct

Parameters that affect the process of training a model.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct ModelParameters
```

## Topics

### Creating parameters
- [init(validation: MLLinearRegressor.ModelParameters.ValidationData, maxIterations: Int, l1Penalty: Double, l2Penalty: Double, stepSize: Double, convergenceThreshold: Double, featureRescaling: Bool)](mllinearregressor/modelparameters-swift.struct/init(validation:maxiterations:l1penalty:l2penalty:stepsize:convergencethreshold:featurerescaling:).md)
- [init(validationData: MLDataTable?, maxIterations: Int, l1Penalty: Double, l2Penalty: Double, stepSize: Double, convergenceThreshold: Double, featureRescaling: Bool)](mllinearregressor/modelparameters-swift.struct/init(validationdata:maxiterations:l1penalty:l2penalty:stepsize:convergencethreshold:featurerescaling:).md)
  Creates a new set of parameters.
- [MLLinearRegressor.ModelParameters.ValidationData](mllinearregressor/modelparameters-swift.struct/validationdata-swift.enum.md)
  Values for specifying validation data.
### Accessing parameters
- [var validationData: MLDataTable?](mllinearregressor/modelparameters-swift.struct/validationdata-swift.property.md)
  Validation data represented as a `MLDataTable`.
- [var maxIterations: Int](mllinearregressor/modelparameters-swift.struct/maxiterations.md)
- [var l1Penalty: Double](mllinearregressor/modelparameters-swift.struct/l1penalty.md)
- [var l2Penalty: Double](mllinearregressor/modelparameters-swift.struct/l2penalty.md)
- [var stepSize: Double](mllinearregressor/modelparameters-swift.struct/stepsize.md)
- [var convergenceThreshold: Double](mllinearregressor/modelparameters-swift.struct/convergencethreshold.md)
- [var featureRescaling: Bool](mllinearregressor/modelparameters-swift.struct/featurerescaling.md)
- [var validation: MLLinearRegressor.ModelParameters.ValidationData](mllinearregressor/modelparameters-swift.struct/validation.md)
  Validation data.
### Describing parameters
- [var description: String](mllinearregressor/modelparameters-swift.struct/description.md)
  A text representation of the model parameters for a linear regressor.
- [var debugDescription: String](mllinearregressor/modelparameters-swift.struct/debugdescription.md)
  A text representation of the model parameters for a linear regressor that’s suitable for output during debugging.
- [var playgroundDescription: Any](mllinearregressor/modelparameters-swift.struct/playgrounddescription.md)
  A description of the model parameters for a linear regressor shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mllinearregressor/modelparameters-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mllinearregressor/modelparameters-swift.struct/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mllinearregressor/modelparameters-swift.struct/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

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
- [let modelParameters: MLLinearRegressor.ModelParameters](mllinearregressor/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
- [var targetColumn: String](mllinearregressor/targetcolumn.md)
  The name of the column you selected at initialization to define which feature the regressor predicts.
- [var featureColumns: [String]](mllinearregressor/featurecolumns.md)
  The names of the columns you selected at initialization to train the regressor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mllinearregressor/modelparameters-swift.struct)*