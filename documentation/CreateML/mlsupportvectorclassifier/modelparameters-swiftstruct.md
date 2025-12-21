# MLSupportVectorClassifier.ModelParameters

**Framework**: Create ML  
**Kind**: struct

Parameters that affect the process of training a model.

**Availability**:
- macOS 10.14+

## Declaration

```swift
struct ModelParameters
```

## Topics

### Creating parameters
- [init(validation: MLSupportVectorClassifier.ModelParameters.ValidationData, maxIterations: Int, penalty: Double, convergenceThreshold: Double, featureRescaling: Bool)](mlsupportvectorclassifier/modelparameters-swift.struct/init(validation:maxiterations:penalty:convergencethreshold:featurerescaling:).md)
  Creates a new set of parameters.
- [init(validationData: MLDataTable?, maxIterations: Int, penalty: Double, convergenceThreshold: Double, featureRescaling: Bool)](mlsupportvectorclassifier/modelparameters-swift.struct/init(validationdata:maxiterations:penalty:convergencethreshold:featurerescaling:).md)
  Creates a new set of parameters.
- [MLSupportVectorClassifier.ModelParameters.ValidationData](mlsupportvectorclassifier/modelparameters-swift.struct/validationdata-swift.enum.md)
  Values for specifying validation data.
### Accessing parameters
- [var convergenceThreshold: Double](mlsupportvectorclassifier/modelparameters-swift.struct/convergencethreshold.md)
- [var featureRescaling: Bool](mlsupportvectorclassifier/modelparameters-swift.struct/featurerescaling.md)
- [var maxIterations: Int](mlsupportvectorclassifier/modelparameters-swift.struct/maxiterations.md)
- [var penalty: Double](mlsupportvectorclassifier/modelparameters-swift.struct/penalty.md)
- [var validationData: MLDataTable?](mlsupportvectorclassifier/modelparameters-swift.struct/validationdata-swift.property.md)
  Validation data represented as a `MLDataTable`.
- [var validation: MLSupportVectorClassifier.ModelParameters.ValidationData](mlsupportvectorclassifier/modelparameters-swift.struct/validation.md)
  Validation data.
### Describing parameters
- [var description: String](mlsupportvectorclassifier/modelparameters-swift.struct/description.md)
  A text representation of the model parameters for a support vector classifier.
- [var debugDescription: String](mlsupportvectorclassifier/modelparameters-swift.struct/debugdescription.md)
  A text representation of the model parameters for a support vector classifier that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlsupportvectorclassifier/modelparameters-swift.struct/playgrounddescription.md)
  A description of the model parameters for a support vector classifier shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlsupportvectorclassifier/modelparameters-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlsupportvectorclassifier/modelparameters-swift.struct/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlsupportvectorclassifier/modelparameters-swift.struct/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [init(trainingData:targetColumn:featureColumns:parameters:)](mlsupportvectorclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:).md)
  Creates a support vector classifier.
- [let modelParameters: MLSupportVectorClassifier.ModelParameters](mlsupportvectorclassifier/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
- [var targetColumn: String](mlsupportvectorclassifier/targetcolumn.md)
  The name of the column you selected at initialization to define which categories the classifier predicts.
- [var featureColumns: [String]](mlsupportvectorclassifier/featurecolumns.md)
  The names of the columns you selected at initialization to train the classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsupportvectorclassifier/modelparameters-swift.struct)*