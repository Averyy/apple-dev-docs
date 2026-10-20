# maxIterations

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var maxIterations: Int
```

## See Also

### Accessing parameters
- [var validationData: MLDataTable?](./validationdata-swift.property.md)
  Validation data represented as a `MLDataTable`.
- [var maxDepth: Int](./maxdepth.md)
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
- [var validation: MLBoostedTreeClassifier.ModelParameters.ValidationData](./validation.md)
  Validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlboostedtreeclassifier/modelparameters-swift.struct/maxiterations)*