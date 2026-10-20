# MLBoostedTreeClassifier.ModelParameters

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
- [init(validation: MLBoostedTreeClassifier.ModelParameters.ValidationData, maxDepth: Int, maxIterations: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int, stepSize: Double, earlyStoppingRounds: Int?, rowSubsample: Double, columnSubsample: Double)](./modelparameters-swift.struct/init%28validation,maxdepth,maxiterations,minlossreduction,minchildweight,randomseed,stepsize,earlystoppingrounds,rowsubsample,columnsubsample%29.md)
- [init(validationData: MLDataTable?, maxDepth: Int, maxIterations: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int, stepSize: Double, earlyStoppingRounds: Int?, rowSubsample: Double, columnSubsample: Double)](./modelparameters-swift.struct/init%28validationdata,maxdepth,maxiterations,minlossreduction,minchildweight,randomseed,stepsize,earlystoppingrounds,rowsubsample,columnsubsample%29.md)
  Creates a new set of parameters defining how a boosted tree classifier should be built.
- [MLBoostedTreeClassifier.ModelParameters.ValidationData](./modelparameters-swift.struct/validationdata-swift.enum.md)
  Values for specifying validation data.
### Accessing parameters
- [var validationData: MLDataTable?](./modelparameters-swift.struct/validationdata-swift.property.md)
  Validation data represented as a `MLDataTable`.
- [var maxDepth: Int](./modelparameters-swift.struct/maxdepth.md)
- [var maxIterations: Int](./modelparameters-swift.struct/maxiterations.md)
- [var minLossReduction: Double](./modelparameters-swift.struct/minlossreduction.md)
- [var minChildWeight: Double](./modelparameters-swift.struct/minchildweight.md)
- [var randomSeed: Int](./modelparameters-swift.struct/randomseed.md)
- [var stepSize: Double](./modelparameters-swift.struct/stepsize.md)
  Must be in the range (0, 1).
- [var earlyStoppingRounds: Int?](./modelparameters-swift.struct/earlystoppingrounds.md)
  Validation data must be specified for an early stop.
- [var rowSubsample: Double](./modelparameters-swift.struct/rowsubsample.md)
  Must be in the range (0, 1).
- [var columnSubsample: Double](./modelparameters-swift.struct/columnsubsample.md)
  Must be in the range (0, 1).
- [var validation: MLBoostedTreeClassifier.ModelParameters.ValidationData](./modelparameters-swift.struct/validation.md)
  Validation data.
### Describing parameters
- [var description: String](./modelparameters-swift.struct/description.md)
  A text representation of the model parameters for a boosted tree classifier.
- [var debugDescription: String](./modelparameters-swift.struct/debugdescription.md)
  A text representation of the model parameters for a boosted tree classifier that’s suitable for output during debugging.
- [var playgroundDescription: Any](./modelparameters-swift.struct/playgrounddescription.md)
  A description of the model parameters for a boosted tree classifier shown in a playground.
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

### Inspecting a boosted tree classifier
- [var model: MLModel](./model.md)
  The Core ML model.
- [let modelParameters: MLBoostedTreeClassifier.ModelParameters](./modelparameters-swift.property.md)
  The underlying parameters used when training the model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlboostedtreeclassifier/modelparameters-swift.struct)*