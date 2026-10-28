# validation

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

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

## Discussion

The default is `.split(strategy: .automatic)`, which automatically generates the validation dataset from 0% to 10% of the training dataset.

## See Also

### Accessing parameters
- [var validationData: MLDataTable?](./validationdata-swift.property.md)
  Validation data represented as a `MLDataTable`.
- [var maxDepth: Int](./maxdepth.md)
- [var maxIterations: Int](./maxiterations.md)
- [var minLossReduction: Double](./minlossreduction.md)
- [var minChildWeight: Double](./minchildweight.md)
- [var randomSeed: Int](./randomseed.md)
- [var stepSize: Double](./stepsize.md)
  Must be in the range (0, 1).
- [var earlyStoppingRounds: Int?](./earlystoppingrounds.md)
  Validation data must be specified for an early stop.
- [var rowSubsample: Double](./rowsubsample.md)
  Must be in the range (0, 1).
- [var columnSubsample: Double](./columnsubsample.md)
  Must be in the range (0, 1).


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlboostedtreeclassifier/modelparameters-swift.struct/validation)*