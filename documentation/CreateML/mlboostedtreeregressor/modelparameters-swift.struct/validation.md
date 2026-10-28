# validation

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

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

## Discussion

The default is `.split(strategy: .automatic)`, which automatically generates the validation dataset from 0% to 10% of the training dataset.

## See Also

### Accessing parameters
- [var columnSubsample: Double](./columnsubsample.md)
  Must be in the range (0, 1).
- [var earlyStoppingRounds: Int?](./earlystoppingrounds.md)
  Validation data must be specified for an early stop.
- [var maxDepth: Int](./maxdepth.md)
- [var maxIterations: Int](./maxiterations.md)
- [var minChildWeight: Double](./minchildweight.md)
- [var minLossReduction: Double](./minlossreduction.md)
- [var randomSeed: Int](./randomseed.md)
- [var rowSubsample: Double](./rowsubsample.md)
  Must be in the range (0, 1).
- [var stepSize: Double](./stepsize.md)
  Must be in the range (0, 1).
- [var validationData: MLDataTable?](./validationdata-swift.property.md)
  Validation data represented as a `MLDataTable`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlboostedtreeregressor/modelparameters-swift.struct/validation)*