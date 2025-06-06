# validationData

**Framework**: Createml  
**Kind**: property

Validation data represented as a `MLDataTable`.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
var validationData: MLDataTable? { get set }
```

#### Discussion

> **Note**: Setting this to `nil` means that the training data will be automatically split for validation. Setting it to an empty table means to not use a validation set.

## See Also

- [var columnSubsample: Double](mlrandomforestclassifier/modelparameters-swift.struct/columnsubsample.md)
  Must be in the range (0, 1).
- [var maxDepth: Int](mlrandomforestclassifier/modelparameters-swift.struct/maxdepth.md)
- [var maxIterations: Int](mlrandomforestclassifier/modelparameters-swift.struct/maxiterations.md)
- [var minChildWeight: Double](mlrandomforestclassifier/modelparameters-swift.struct/minchildweight.md)
- [var minLossReduction: Double](mlrandomforestclassifier/modelparameters-swift.struct/minlossreduction.md)
- [var randomSeed: Int](mlrandomforestclassifier/modelparameters-swift.struct/randomseed.md)
- [var rowSubsample: Double](mlrandomforestclassifier/modelparameters-swift.struct/rowsubsample.md)
  Must be in the range (0, 1).
- [var validation: MLRandomForestClassifier.ModelParameters.ValidationData](mlrandomforestclassifier/modelparameters-swift.struct/validation.md)
  Validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrandomforestclassifier/modelparameters-swift.struct/validationdata-swift.property)*