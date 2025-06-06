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
var validation: MLRandomForestClassifier.ModelParameters.ValidationData { get set }
```

#### Discussion

The default is `.split(strategy: .automatic)`, which automatically generates the validation dataset from 0% to 10% of the training dataset.

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
- [var validationData: MLDataTable?](mlrandomforestclassifier/modelparameters-swift.struct/validationdata-swift.property.md)
  Validation data represented as a `MLDataTable`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrandomforestclassifier/modelparameters-swift.struct/validation)*