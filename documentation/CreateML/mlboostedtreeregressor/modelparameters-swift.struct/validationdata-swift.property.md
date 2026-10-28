# validationData

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

Validation data represented as a `MLDataTable`.

**Availability**:
- iOS 15.0+ - Deprecated in 16.0
- iPadOS 15.0+ - Deprecated in 16.0
- Mac Catalyst 15.0+ - Deprecated in 16.0
- macOS 10.14+ - Deprecated in 11.0
- visionOS 1.0+

> **Deprecated**: Use the validation property instead.

## Declaration

```swift
var validationData: MLDataTable? { get set }
```

## Discussion

> **Note**: Setting this to `nil` means that the training data will be automatically split for validation. Setting it to an empty table means to not use a validation set.

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
- [var validation: MLBoostedTreeRegressor.ModelParameters.ValidationData](./validation.md)
  Validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlboostedtreeregressor/modelparameters-swift.struct/validationdata-swift.property)*