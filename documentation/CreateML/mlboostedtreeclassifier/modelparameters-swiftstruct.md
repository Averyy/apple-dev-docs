# MLBoostedTreeClassifier.ModelParameters

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
- [init(validation: MLBoostedTreeClassifier.ModelParameters.ValidationData, maxDepth: Int, maxIterations: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int, stepSize: Double, earlyStoppingRounds: Int?, rowSubsample: Double, columnSubsample: Double)](mlboostedtreeclassifier/modelparameters-swift.struct/init(validation:maxdepth:maxiterations:minlossreduction:minchildweight:randomseed:stepsize:earlystoppingrounds:rowsubsample:columnsubsample:).md)
- [init(validationData: MLDataTable?, maxDepth: Int, maxIterations: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int, stepSize: Double, earlyStoppingRounds: Int?, rowSubsample: Double, columnSubsample: Double)](mlboostedtreeclassifier/modelparameters-swift.struct/init(validationdata:maxdepth:maxiterations:minlossreduction:minchildweight:randomseed:stepsize:earlystoppingrounds:rowsubsample:columnsubsample:).md)
  Creates a new set of parameters defining how a boosted tree classifier should be built.
- [MLBoostedTreeClassifier.ModelParameters.ValidationData](mlboostedtreeclassifier/modelparameters-swift.struct/validationdata-swift.enum.md)
  Values for specifying validation data.
### Accessing parameters
- [var validationData: MLDataTable?](mlboostedtreeclassifier/modelparameters-swift.struct/validationdata-swift.property.md)
  Validation data represented as a `MLDataTable`.
- [var maxDepth: Int](mlboostedtreeclassifier/modelparameters-swift.struct/maxdepth.md)
- [var maxIterations: Int](mlboostedtreeclassifier/modelparameters-swift.struct/maxiterations.md)
- [var minLossReduction: Double](mlboostedtreeclassifier/modelparameters-swift.struct/minlossreduction.md)
- [var minChildWeight: Double](mlboostedtreeclassifier/modelparameters-swift.struct/minchildweight.md)
- [var randomSeed: Int](mlboostedtreeclassifier/modelparameters-swift.struct/randomseed.md)
- [var stepSize: Double](mlboostedtreeclassifier/modelparameters-swift.struct/stepsize.md)
  Must be in the range (0, 1).
- [var earlyStoppingRounds: Int?](mlboostedtreeclassifier/modelparameters-swift.struct/earlystoppingrounds.md)
  Validation data must be specified for an early stop.
- [var rowSubsample: Double](mlboostedtreeclassifier/modelparameters-swift.struct/rowsubsample.md)
  Must be in the range (0, 1).
- [var columnSubsample: Double](mlboostedtreeclassifier/modelparameters-swift.struct/columnsubsample.md)
  Must be in the range (0, 1).
- [var validation: MLBoostedTreeClassifier.ModelParameters.ValidationData](mlboostedtreeclassifier/modelparameters-swift.struct/validation.md)
  Validation data.
### Describing parameters
- [var description: String](mlboostedtreeclassifier/modelparameters-swift.struct/description.md)
  A text representation of the model parameters for a boosted tree classifier.
- [var debugDescription: String](mlboostedtreeclassifier/modelparameters-swift.struct/debugdescription.md)
  A text representation of the model parameters for a boosted tree classifier that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlboostedtreeclassifier/modelparameters-swift.struct/playgrounddescription.md)
  A description of the model parameters for a boosted tree classifier shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlboostedtreeclassifier/modelparameters-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlboostedtreeclassifier/modelparameters-swift.struct/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlboostedtreeclassifier/modelparameters-swift.struct/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [var model: MLModel](mlboostedtreeclassifier/model.md)
  The Core ML model.
- [let modelParameters: MLBoostedTreeClassifier.ModelParameters](mlboostedtreeclassifier/modelparameters-swift.property.md)
  The underlying parameters used when training the model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlboostedtreeclassifier/modelparameters-swift.struct)*