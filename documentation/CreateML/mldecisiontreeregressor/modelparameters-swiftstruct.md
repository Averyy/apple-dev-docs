# MLDecisionTreeRegressor.ModelParameters

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
- [init(validation: MLDecisionTreeRegressor.ModelParameters.ValidationData, maxDepth: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int)](mldecisiontreeregressor/modelparameters-swift.struct/init(validation:maxdepth:minlossreduction:minchildweight:randomseed:).md)
- [init(validationData: MLDataTable?, maxDepth: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int)](mldecisiontreeregressor/modelparameters-swift.struct/init(validationdata:maxdepth:minlossreduction:minchildweight:randomseed:).md)
  Creates a new set of parameters.
- [MLDecisionTreeRegressor.ModelParameters.ValidationData](mldecisiontreeregressor/modelparameters-swift.struct/validationdata-swift.enum.md)
  Values for specifying validation data.
### Accessing parameters
- [var maxDepth: Int](mldecisiontreeregressor/modelparameters-swift.struct/maxdepth.md)
- [var minChildWeight: Double](mldecisiontreeregressor/modelparameters-swift.struct/minchildweight.md)
- [var minLossReduction: Double](mldecisiontreeregressor/modelparameters-swift.struct/minlossreduction.md)
- [var randomSeed: Int](mldecisiontreeregressor/modelparameters-swift.struct/randomseed.md)
- [var validationData: MLDataTable?](mldecisiontreeregressor/modelparameters-swift.struct/validationdata-swift.property.md)
  Validation data represented as a `MLDataTable`.
- [var validation: MLDecisionTreeRegressor.ModelParameters.ValidationData](mldecisiontreeregressor/modelparameters-swift.struct/validation.md)
  Validation data.
### Describing parameters
- [var description: String](mldecisiontreeregressor/modelparameters-swift.struct/description.md)
  A text representation of the model parameters for a decision tree regressor.
- [var debugDescription: String](mldecisiontreeregressor/modelparameters-swift.struct/debugdescription.md)
  A text representation of the model parameters for a decision tree regressor that’s suitable for output during debugging.
- [var playgroundDescription: Any](mldecisiontreeregressor/modelparameters-swift.struct/playgrounddescription.md)
  A text representation of the model parameters for a decision tree regressor.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mldecisiontreeregressor/modelparameters-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mldecisiontreeregressor/modelparameters-swift.struct/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mldecisiontreeregressor/modelparameters-swift.struct/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [var model: MLModel](mldecisiontreeregressor/model.md)
  The Core ML model.
- [let modelParameters: MLDecisionTreeRegressor.ModelParameters](mldecisiontreeregressor/modelparameters-swift.property.md)
  The underlying parameters used when training the model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldecisiontreeregressor/modelparameters-swift.struct)*