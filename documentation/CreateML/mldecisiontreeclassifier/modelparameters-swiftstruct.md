# MLDecisionTreeClassifier.ModelParameters

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
- [init(validation: MLDecisionTreeClassifier.ModelParameters.ValidationData, maxDepth: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int)](mldecisiontreeclassifier/modelparameters-swift.struct/init(validation:maxdepth:minlossreduction:minchildweight:randomseed:).md)
- [init(validationData: MLDataTable?, maxDepth: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int)](mldecisiontreeclassifier/modelparameters-swift.struct/init(validationdata:maxdepth:minlossreduction:minchildweight:randomseed:).md)
  Creates a new set of parameters.
- [MLDecisionTreeClassifier.ModelParameters.ValidationData](mldecisiontreeclassifier/modelparameters-swift.struct/validationdata-swift.enum.md)
  Values for specifying validation data.
### Accessing parameters
- [var validationData: MLDataTable?](mldecisiontreeclassifier/modelparameters-swift.struct/validationdata-swift.property.md)
  The data used for the validation set to inform the model training process.
- [var maxDepth: Int](mldecisiontreeclassifier/modelparameters-swift.struct/maxdepth.md)
  The maximum depth of the tree. Must be greater than 0.
- [var minLossReduction: Double](mldecisiontreeclassifier/modelparameters-swift.struct/minlossreduction.md)
  The minimum amount that the loss needs to be reduced to create a new split.
- [var minChildWeight: Double](mldecisiontreeclassifier/modelparameters-swift.struct/minchildweight.md)
  The minimum weight of each leaf node.
- [var randomSeed: Int](mldecisiontreeclassifier/modelparameters-swift.struct/randomseed.md)
  The seed value for random operations during tree building process.
- [var validation: MLDecisionTreeClassifier.ModelParameters.ValidationData](mldecisiontreeclassifier/modelparameters-swift.struct/validation.md)
  Validation data.
### Describing parameters
- [var description: String](mldecisiontreeclassifier/modelparameters-swift.struct/description.md)
  A text representation of the model parameters for a decision tree classifier.
- [var debugDescription: String](mldecisiontreeclassifier/modelparameters-swift.struct/debugdescription.md)
  A text representation of the model parameters for a decision tree classifier that’s suitable for output during debugging.
- [var playgroundDescription: Any](mldecisiontreeclassifier/modelparameters-swift.struct/playgrounddescription.md)
  A description of the model parameters for a decision tree classifier shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mldecisiontreeclassifier/modelparameters-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mldecisiontreeclassifier/modelparameters-swift.struct/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mldecisiontreeclassifier/modelparameters-swift.struct/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [init(checkpoint: MLCheckpoint) throws](mldecisiontreeclassifier/init(checkpoint:).md)
  Creates a decision tree classifier classifier  from a checkpoint.
- [init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLDecisionTreeClassifier.ModelParameters) throws](mldecisiontreeclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:)-3dvkw.md)
  Creates a decision tree classifier.
- [static func makeTrainingSession(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLDecisionTreeClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLDecisionTreeClassifier>](mldecisiontreeclassifier/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-1cgxc.md)
  Creates or restores a training session.
- [static func makeTrainingSession(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLDecisionTreeClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLDecisionTreeClassifier>](mldecisiontreeclassifier/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-73z9l.md)
  Creates or restores a training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLDecisionTreeClassifier>](mldecisiontreeclassifier/restoretrainingsession(sessionparameters:).md)
  Restores an existing training session.
- [static func resume(MLTrainingSession<MLDecisionTreeClassifier>) throws -> MLJob<MLDecisionTreeClassifier>](mldecisiontreeclassifier/resume(_:).md)
  Resumes a training session from the last checkpoint if available.
- [static func train(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLDecisionTreeClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLDecisionTreeClassifier>](mldecisiontreeclassifier/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-4155u.md)
  Trains a decision tree classifier.
- [static func train(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLDecisionTreeClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLDecisionTreeClassifier>](mldecisiontreeclassifier/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-50xr2.md)
  Trains a decision tree classifier.
- [init(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLDecisionTreeClassifier.ModelParameters) throws](mldecisiontreeclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:)-hmwt.md)
  Creates a Decision Tree Classifier from the feature columns in the training data to predict the categories in the target column.
- [let modelParameters: MLDecisionTreeClassifier.ModelParameters](mldecisiontreeclassifier/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
- [var targetColumn: String](mldecisiontreeclassifier/targetcolumn.md)
  The name of the column you selected at initialization to define which categories the classifier predicts.
- [var featureColumns: [String]](mldecisiontreeclassifier/featurecolumns.md)
  The names of the columns you selected at initialization to train the classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldecisiontreeclassifier/modelparameters-swift.struct)*