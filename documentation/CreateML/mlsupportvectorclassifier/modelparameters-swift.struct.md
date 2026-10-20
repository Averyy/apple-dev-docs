# MLSupportVectorClassifier.ModelParameters

**Framework**: Create ML  
**Kind**: struct  
**Role**: Structure

Parameters that affect the process of training a model.

**Availability**:
- macOS 10.14+ - Deprecated in 14.0

## Declaration

```swift
struct ModelParameters
```

## Topics

### Creating parameters
- [init(validation: MLSupportVectorClassifier.ModelParameters.ValidationData, maxIterations: Int, penalty: Double, convergenceThreshold: Double, featureRescaling: Bool)](./modelparameters-swift.struct/init%28validation,maxiterations,penalty,convergencethreshold,featurerescaling%29.md)
  Creates a new set of parameters.
- [init(validationData: MLDataTable?, maxIterations: Int, penalty: Double, convergenceThreshold: Double, featureRescaling: Bool)](./modelparameters-swift.struct/init%28validationdata,maxiterations,penalty,convergencethreshold,featurerescaling%29.md)
  Creates a new set of parameters.
- [MLSupportVectorClassifier.ModelParameters.ValidationData](./modelparameters-swift.struct/validationdata-swift.enum.md)
  Values for specifying validation data.
### Accessing parameters
- [var convergenceThreshold: Double](./modelparameters-swift.struct/convergencethreshold.md)
- [var featureRescaling: Bool](./modelparameters-swift.struct/featurerescaling.md)
- [var maxIterations: Int](./modelparameters-swift.struct/maxiterations.md)
- [var penalty: Double](./modelparameters-swift.struct/penalty.md)
- [var validationData: MLDataTable?](./modelparameters-swift.struct/validationdata-swift.property.md)
  Validation data represented as a `MLDataTable`.
- [var validation: MLSupportVectorClassifier.ModelParameters.ValidationData](./modelparameters-swift.struct/validation.md)
  Validation data.
### Describing parameters
- [var description: String](./modelparameters-swift.struct/description.md)
  A text representation of the model parameters for a support vector classifier.
- [var debugDescription: String](./modelparameters-swift.struct/debugdescription.md)
  A text representation of the model parameters for a support vector classifier that’s suitable for output during debugging.
- [var playgroundDescription: Any](./modelparameters-swift.struct/playgrounddescription.md)
  A description of the model parameters for a support vector classifier shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./modelparameters-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](./modelparameters-swift.struct/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](./modelparameters-swift.struct/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomPlaygroundDisplayConvertible](../../Swift/customplaygrounddisplayconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Escapable](../../Swift/escapable.md)

## See Also

### Creating and training a support vector classifier
- [init(trainingData:targetColumn:featureColumns:parameters:)](./init%28trainingdata,targetcolumn,featurecolumns,parameters%29.md)
  Creates a support vector classifier.
- [let modelParameters: MLSupportVectorClassifier.ModelParameters](./modelparameters-swift.property.md)
  The underlying parameters used when training the model.
- [var targetColumn: String](./targetcolumn.md)
  The name of the column you selected at initialization to define which categories the classifier predicts.
- [var featureColumns: [String]](./featurecolumns.md)
  The names of the columns you selected at initialization to train the classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsupportvectorclassifier/modelparameters-swift.struct)*