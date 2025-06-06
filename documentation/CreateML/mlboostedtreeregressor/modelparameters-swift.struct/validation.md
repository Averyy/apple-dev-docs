# validation

**Framework**: Create ML  
**Kind**: property

Validation data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var validation: MLBoostedTreeRegressor.ModelParameters.ValidationData { get set }
```

#### Discussion

The default is `.split(strategy: .automatic)`, which automatically generates the validation dataset from 0% to 10% of the training dataset.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlboostedtreeregressor/modelparameters-swift.struct/validation)*