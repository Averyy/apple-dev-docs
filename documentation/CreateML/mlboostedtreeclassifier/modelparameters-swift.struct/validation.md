# validation

**Framework**: Create ML  
**Kind**: property

Validation data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var validation: MLBoostedTreeClassifier.ModelParameters.ValidationData { get set }
```

#### Discussion

The default is `.split(strategy: .automatic)`, which automatically generates the validation dataset from 0% to 10% of the training dataset.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlboostedtreeclassifier/modelparameters-swift.struct/validation)*