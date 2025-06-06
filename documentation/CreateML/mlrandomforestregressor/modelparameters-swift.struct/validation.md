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
var validation: MLRandomForestRegressor.ModelParameters.ValidationData { get set }
```

#### Discussion

The default is `.split(strategy: .automatic)`, which automatically generates the validation dataset from 0% to 10% of the training dataset.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrandomforestregressor/modelparameters-swift.struct/validation)*