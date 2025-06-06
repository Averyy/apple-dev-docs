# MLRandomForestClassifier.ModelParameters

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
- [init(validation: MLRandomForestClassifier.ModelParameters.ValidationData, maxDepth: Int, maxIterations: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int, rowSubsample: Double, columnSubsample: Double)](mlrandomforestclassifier/modelparameters-swift.struct/init(validation:maxdepth:maxiterations:minlossreduction:minchildweight:randomseed:rowsubsample:columnsubsample:).md)
- [init(validationData: MLDataTable?, maxDepth: Int, maxIterations: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int, rowSubsample: Double, columnSubsample: Double)](mlrandomforestclassifier/modelparameters-swift.struct/init(validationdata:maxdepth:maxiterations:minlossreduction:minchildweight:randomseed:rowsubsample:columnsubsample:).md)
  Creates a new set of parameters.
- [MLRandomForestClassifier.ModelParameters.ValidationData](mlrandomforestclassifier/modelparameters-swift.struct/validationdata-swift.enum.md)
  Values for specifying validation data.
### Accessing parameters
- [var columnSubsample: Double](mlrandomforestclassifier/modelparameters-swift.struct/columnsubsample.md)
  Must be in the range (0, 1).
- [var maxDepth: Int](mlrandomforestclassifier/modelparameters-swift.struct/maxdepth.md)
- [var maxIterations: Int](mlrandomforestclassifier/modelparameters-swift.struct/maxiterations.md)
- [var minChildWeight: Double](mlrandomforestclassifier/modelparameters-swift.struct/minchildweight.md)
- [var minLossReduction: Double](mlrandomforestclassifier/modelparameters-swift.struct/minlossreduction.md)
- [var randomSeed: Int](mlrandomforestclassifier/modelparameters-swift.struct/randomseed.md)
- [var rowSubsample: Double](mlrandomforestclassifier/modelparameters-swift.struct/rowsubsample.md)
  Must be in the range (0, 1).
- [var validationData: MLDataTable?](mlrandomforestclassifier/modelparameters-swift.struct/validationdata-swift.property.md)
  Validation data represented as a `MLDataTable`.
- [var validation: MLRandomForestClassifier.ModelParameters.ValidationData](mlrandomforestclassifier/modelparameters-swift.struct/validation.md)
  Validation data.
### Describing parameters
- [var description: String](mlrandomforestclassifier/modelparameters-swift.struct/description.md)
  A text representation of the model parameters for a random forest classifier.
- [var debugDescription: String](mlrandomforestclassifier/modelparameters-swift.struct/debugdescription.md)
  A text representation of the model parameters for a random forest classifier that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlrandomforestclassifier/modelparameters-swift.struct/playgrounddescription.md)
  A description of the model parameters for a random forest classifier shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlrandomforestclassifier/modelparameters-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlrandomforestclassifier/modelparameters-swift.struct/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlrandomforestclassifier/modelparameters-swift.struct/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [init(checkpoint: MLCheckpoint) throws](mlrandomforestclassifier/init(checkpoint:).md)
  Creates a random forest classifier classifier  from a checkpoint.
- [init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLRandomForestClassifier.ModelParameters) throws](mlrandomforestclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:)-5nojh.md)
  Creates a random forest classifier.
- [init(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLRandomForestClassifier.ModelParameters) throws](mlrandomforestclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:)-4pxej.md)
  Creates a Random Forest Classifier from the feature columns in the training data to predict the categories in the target column.
- [let modelParameters: MLRandomForestClassifier.ModelParameters](mlrandomforestclassifier/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
- [var targetColumn: String](mlrandomforestclassifier/targetcolumn.md)
  The name of the column you selected at initialization to define which categories the classifier predicts.
- [var featureColumns: [String]](mlrandomforestclassifier/featurecolumns.md)
  The names of the columns you selected at initialization to train the classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrandomforestclassifier/modelparameters-swift.struct)*