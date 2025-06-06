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

- [var maxDepth: Int](mldecisiontreeregressor/modelparameters-swift.struct/maxdepth.md)
- [var minChildWeight: Double](mldecisiontreeregressor/modelparameters-swift.struct/minchildweight.md)
- [var minLossReduction: Double](mldecisiontreeregressor/modelparameters-swift.struct/minlossreduction.md)
- [var randomSeed: Int](mldecisiontreeregressor/modelparameters-swift.struct/randomseed.md)
- [var validation: MLDecisionTreeRegressor.ModelParameters.ValidationData](mldecisiontreeregressor/modelparameters-swift.struct/validation.md)
  Validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldecisiontreeregressor/modelparameters-swift.struct/validationdata-swift.property)*