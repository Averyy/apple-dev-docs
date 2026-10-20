# MLDecisionTreeClassifier.ModelParameters

**Framework**: Create ML  
**Kind**: struct  
**Role**: Structure

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
- [init(validation: MLDecisionTreeClassifier.ModelParameters.ValidationData, maxDepth: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int)](./modelparameters-swift.struct/init%28validation,maxdepth,minlossreduction,minchildweight,randomseed%29.md)
- [init(validationData: MLDataTable?, maxDepth: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int)](./modelparameters-swift.struct/init%28validationdata,maxdepth,minlossreduction,minchildweight,randomseed%29.md)
  Creates a new set of parameters.
- [MLDecisionTreeClassifier.ModelParameters.ValidationData](./modelparameters-swift.struct/validationdata-swift.enum.md)
  Values for specifying validation data.
### Accessing parameters
- [var validationData: MLDataTable?](./modelparameters-swift.struct/validationdata-swift.property.md)
  The data used for the validation set to inform the model training process.
- [var maxDepth: Int](./modelparameters-swift.struct/maxdepth.md)
  The maximum depth of the tree. Must be greater than 0.
- [var minLossReduction: Double](./modelparameters-swift.struct/minlossreduction.md)
  The minimum amount that the loss needs to be reduced to create a new split.
- [var minChildWeight: Double](./modelparameters-swift.struct/minchildweight.md)
  The minimum weight of each leaf node.
- [var randomSeed: Int](./modelparameters-swift.struct/randomseed.md)
  The seed value for random operations during tree building process.
- [var validation: MLDecisionTreeClassifier.ModelParameters.ValidationData](./modelparameters-swift.struct/validation.md)
  Validation data.
### Describing parameters
- [var description: String](./modelparameters-swift.struct/description.md)
  A text representation of the model parameters for a decision tree classifier.
- [var debugDescription: String](./modelparameters-swift.struct/debugdescription.md)
  A text representation of the model parameters for a decision tree classifier that’s suitable for output during debugging.
- [var playgroundDescription: Any](./modelparameters-swift.struct/playgrounddescription.md)
  A description of the model parameters for a decision tree classifier shown in a playground.
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

### Inspecting a decision tree classifier
- [var model: MLModel](./model.md)
  The Core ML model.
- [let modelParameters: MLDecisionTreeClassifier.ModelParameters](./modelparameters-swift.property.md)
  The underlying parameters used when training the model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldecisiontreeclassifier/modelparameters-swift.struct)*