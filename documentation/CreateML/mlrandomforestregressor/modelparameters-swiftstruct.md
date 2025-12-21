# MLRandomForestRegressor.ModelParameters

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
- [init(validation: MLRandomForestRegressor.ModelParameters.ValidationData, maxDepth: Int, maxIterations: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int, rowSubsample: Double, columnSubsample: Double)](mlrandomforestregressor/modelparameters-swift.struct/init(validation:maxdepth:maxiterations:minlossreduction:minchildweight:randomseed:rowsubsample:columnsubsample:).md)
- [init(validationData: MLDataTable?, maxDepth: Int, maxIterations: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int, rowSubsample: Double, columnSubsample: Double)](mlrandomforestregressor/modelparameters-swift.struct/init(validationdata:maxdepth:maxiterations:minlossreduction:minchildweight:randomseed:rowsubsample:columnsubsample:).md)
  Creates a new set of parameters.
- [MLRandomForestRegressor.ModelParameters.ValidationData](mlrandomforestregressor/modelparameters-swift.struct/validationdata-swift.enum.md)
  Values for specifying validation data.
### Accessing parameters
- [var columnSubsample: Double](mlrandomforestregressor/modelparameters-swift.struct/columnsubsample.md)
  Must be in the range (0, 1).
- [var maxDepth: Int](mlrandomforestregressor/modelparameters-swift.struct/maxdepth.md)
- [var maxIterations: Int](mlrandomforestregressor/modelparameters-swift.struct/maxiterations.md)
- [var minChildWeight: Double](mlrandomforestregressor/modelparameters-swift.struct/minchildweight.md)
- [var minLossReduction: Double](mlrandomforestregressor/modelparameters-swift.struct/minlossreduction.md)
- [var randomSeed: Int](mlrandomforestregressor/modelparameters-swift.struct/randomseed.md)
- [var rowSubsample: Double](mlrandomforestregressor/modelparameters-swift.struct/rowsubsample.md)
  Must be in the range (0, 1).
- [var validationData: MLDataTable?](mlrandomforestregressor/modelparameters-swift.struct/validationdata-swift.property.md)
  Validation data represented as a `MLDataTable`.
- [var validation: MLRandomForestRegressor.ModelParameters.ValidationData](mlrandomforestregressor/modelparameters-swift.struct/validation.md)
  Validation data.
### Describing parameters
- [var description: String](mlrandomforestregressor/modelparameters-swift.struct/description.md)
  A text representation of the model parameters for a random forest regressor.
- [var debugDescription: String](mlrandomforestregressor/modelparameters-swift.struct/debugdescription.md)
  A text representation of the model parameters for a random forest regressor that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlrandomforestregressor/modelparameters-swift.struct/playgrounddescription.md)
  A description of the model parameters for a random forest regressor shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlrandomforestregressor/modelparameters-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlrandomforestregressor/modelparameters-swift.struct/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlrandomforestregressor/modelparameters-swift.struct/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [var model: MLModel](mlrandomforestregressor/model.md)
  The Core ML model.
- [let modelParameters: MLRandomForestRegressor.ModelParameters](mlrandomforestregressor/modelparameters-swift.property.md)
  The underlying parameters used when training the model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrandomforestregressor/modelparameters-swift.struct)*