# MLLogisticRegressionClassifier.ModelParameters

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
- [init(validation: MLLogisticRegressionClassifier.ModelParameters.ValidationData, maxIterations: Int, l1Penalty: Double, l2Penalty: Double, stepSize: Double, convergenceThreshold: Double, featureRescaling: Bool)](mllogisticregressionclassifier/modelparameters-swift.struct/init(validation:maxiterations:l1penalty:l2penalty:stepsize:convergencethreshold:featurerescaling:).md)
- [init(validationData: MLDataTable?, maxIterations: Int, l1Penalty: Double, l2Penalty: Double, stepSize: Double, convergenceThreshold: Double, featureRescaling: Bool)](mllogisticregressionclassifier/modelparameters-swift.struct/init(validationdata:maxiterations:l1penalty:l2penalty:stepsize:convergencethreshold:featurerescaling:).md)
  Creates a new set of parameters.
- [MLLogisticRegressionClassifier.ModelParameters.ValidationData](mllogisticregressionclassifier/modelparameters-swift.struct/validationdata-swift.enum.md)
  Values for specifying validation data.
### Accessing parameters
- [var convergenceThreshold: Double](mllogisticregressionclassifier/modelparameters-swift.struct/convergencethreshold.md)
- [var featureRescaling: Bool](mllogisticregressionclassifier/modelparameters-swift.struct/featurerescaling.md)
- [var l1Penalty: Double](mllogisticregressionclassifier/modelparameters-swift.struct/l1penalty.md)
- [var l2Penalty: Double](mllogisticregressionclassifier/modelparameters-swift.struct/l2penalty.md)
- [var maxIterations: Int](mllogisticregressionclassifier/modelparameters-swift.struct/maxiterations.md)
- [var stepSize: Double](mllogisticregressionclassifier/modelparameters-swift.struct/stepsize.md)
- [var validationData: MLDataTable?](mllogisticregressionclassifier/modelparameters-swift.struct/validationdata-swift.property.md)
  Validation data represented as a `MLDataTable`.
- [var validation: MLLogisticRegressionClassifier.ModelParameters.ValidationData](mllogisticregressionclassifier/modelparameters-swift.struct/validation.md)
  Validation data.
### Describing parameters
- [var description: String](mllogisticregressionclassifier/modelparameters-swift.struct/description.md)
  A text representation of the model parameters for a logistic regression classifier.
- [var debugDescription: String](mllogisticregressionclassifier/modelparameters-swift.struct/debugdescription.md)
  A text representation of the model parameters for a logistic regression classifier that’s suitable for output during debugging.
- [var playgroundDescription: Any](mllogisticregressionclassifier/modelparameters-swift.struct/playgrounddescription.md)
  A description of the model parameters for a logistic regression classifier shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mllogisticregressionclassifier/modelparameters-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mllogisticregressionclassifier/modelparameters-swift.struct/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mllogisticregressionclassifier/modelparameters-swift.struct/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [init(checkpoint: MLCheckpoint) throws](mllogisticregressionclassifier/init(checkpoint:).md)
  Creates a logistic regression classifier from a checkpoint.
- [init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLLogisticRegressionClassifier.ModelParameters) throws](mllogisticregressionclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:)-3ilkk.md)
  Creates a logistic regression classifier.
- [init(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLLogisticRegressionClassifier.ModelParameters) throws](mllogisticregressionclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:)-7xy2g.md)
  Creates a Logistic Regression Classifier from the feature columns in the training data to predict the categories in the target column.
- [static func train(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLLogisticRegressionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLLogisticRegressionClassifier>](mllogisticregressionclassifier/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-1jn01.md)
  Trains a logistic regression classifier.
- [static func train(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLLogisticRegressionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLLogisticRegressionClassifier>](mllogisticregressionclassifier/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-8vpa1.md)
  Trains a logistic regression classifier.
- [static func makeTrainingSession(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLLogisticRegressionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLLogisticRegressionClassifier>](mllogisticregressionclassifier/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-4anyg.md)
  Creates or restores a training session.
- [static func makeTrainingSession(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLLogisticRegressionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLLogisticRegressionClassifier>](mllogisticregressionclassifier/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-7l7f0.md)
  Creates or restores a training session.
- [static func resume(MLTrainingSession<MLLogisticRegressionClassifier>) throws -> MLJob<MLLogisticRegressionClassifier>](mllogisticregressionclassifier/resume(_:).md)
  Resumes a training session from the last checkpoint if available.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLLogisticRegressionClassifier>](mllogisticregressionclassifier/restoretrainingsession(sessionparameters:).md)
  Restores an existing training session.
- [let modelParameters: MLLogisticRegressionClassifier.ModelParameters](mllogisticregressionclassifier/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
- [var targetColumn: String](mllogisticregressionclassifier/targetcolumn.md)
  The name of the column you selected at initialization to define which categories the classifier predicts.
- [var featureColumns: [String]](mllogisticregressionclassifier/featurecolumns.md)
  The names of the columns you selected at initialization to train the classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mllogisticregressionclassifier/modelparameters-swift.struct)*