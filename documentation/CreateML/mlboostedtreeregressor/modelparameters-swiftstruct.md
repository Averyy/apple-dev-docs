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

- [var model: MLModel](mlboostedtreeregressor/model.md)
  The Core ML model.
- [let modelParameters: MLBoostedTreeRegressor.ModelParameters](mlboostedtreeregressor/modelparameters-swift.property.md)
  The underlying parameters used when training the model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlboostedtreeregressor/modelparameters-swift.struct)*