# MLBoostedTreeRegressor.ModelParameters

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
- [init(validation: MLBoostedTreeRegressor.ModelParameters.ValidationData, maxDepth: Int, maxIterations: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int, stepSize: Double, earlyStoppingRounds: Int?, rowSubsample: Double, columnSubsample: Double)](mlboostedtreeregressor/modelparameters-swift.struct/init(validation:maxdepth:maxiterations:minlossreduction:minchildweight:randomseed:stepsize:earlystoppingrounds:rowsubsample:columnsubsample:).md)
- [init(validationData: MLDataTable?, maxDepth: Int, maxIterations: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int, stepSize: Double, earlyStoppingRounds: Int?, rowSubsample: Double, columnSubsample: Double)](mlboostedtreeregressor/modelparameters-swift.struct/init(validationdata:maxdepth:maxiterations:minlossreduction:minchildweight:randomseed:stepsize:earlystoppingrounds:rowsubsample:columnsubsample:).md)
  Creates a new set of parameters.
- [MLBoostedTreeRegressor.ModelParameters.ValidationData](mlboostedtreeregressor/modelparameters-swift.struct/validationdata-swift.enum.md)
  Values for specifying validation data.
### Accessing parameters
- [var columnSubsample: Double](mlboostedtreeregressor/modelparameters-swift.struct/columnsubsample.md)
  Must be in the range (0, 1).
- [var earlyStoppingRounds: Int?](mlboostedtreeregressor/modelparameters-swift.struct/earlystoppingrounds.md)
  Validation data must be specified for an early stop.
- [var maxDepth: Int](mlboostedtreeregressor/modelparameters-swift.struct/maxdepth.md)
- [var maxIterations: Int](mlboostedtreeregressor/modelparameters-swift.struct/maxiterations.md)
- [var minChildWeight: Double](mlboostedtreeregressor/modelparameters-swift.struct/minchildweight.md)
- [var minLossReduction: Double](mlboostedtreeregressor/modelparameters-swift.struct/minlossreduction.md)
- [var randomSeed: Int](mlboostedtreeregressor/modelparameters-swift.struct/randomseed.md)
- [var rowSubsample: Double](mlboostedtreeregressor/modelparameters-swift.struct/rowsubsample.md)
  Must be in the range (0, 1).
- [var stepSize: Double](mlboostedtreeregressor/modelparameters-swift.struct/stepsize.md)
  Must be in the range (0, 1).
- [var validationData: MLDataTable?](mlboostedtreeregressor/modelparameters-swift.struct/validationdata-swift.property.md)
  Validation data represented as a `MLDataTable`.
- [var validation: MLBoostedTreeRegressor.ModelParameters.ValidationData](mlboostedtreeregressor/modelparameters-swift.struct/validation.md)
  Validation data.
### Describing parameters
- [var description: String](mlboostedtreeregressor/modelparameters-swift.struct/description.md)
  A text representation of the model parameters for a boosted tree regressor.
- [var debugDescription: String](mlboostedtreeregressor/modelparameters-swift.struct/debugdescription.md)
  A text representation of the model parameters for a boosted tree regressor that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlboostedtreeregressor/modelparameters-swift.struct/playgrounddescription.md)
  A description of the model parameters for a boosted tree regressor shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlboostedtreeregressor/modelparameters-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlboostedtreeregressor/modelparameters-swift.struct/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlboostedtreeregressor/modelparameters-swift.struct/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

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
- [let modelParameters: MLBoostedTreeRegressor.ModelParameters](mlboostedtreeregressor/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
- [var targetColumn: String](mlboostedtreeregressor/targetcolumn.md)
  The name of the column you selected at initialization to define which feature the regressor predicts.
- [var featureColumns: [String]](mlboostedtreeregressor/featurecolumns.md)
  The names of the columns you selected at initialization to train the regressor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlboostedtreeregressor/modelparameters-swift.struct)*