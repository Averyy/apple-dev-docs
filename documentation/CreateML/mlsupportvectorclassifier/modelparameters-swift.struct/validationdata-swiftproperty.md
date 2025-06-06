# validationData

**Framework**: Createml  
**Kind**: property

Validation data represented as a `MLDataTable`.

**Availability**:
- macOS 10.14+

## Declaration

```swift
var validationData: MLDataTable? { get set }
```

#### Discussion

> **Note**: Setting this to `nil` means that the training data will be automatically split for validation. Setting it to an empty table means to not use a validation set.

## See Also

- [var convergenceThreshold: Double](mlsupportvectorclassifier/modelparameters-swift.struct/convergencethreshold.md)
- [var featureRescaling: Bool](mlsupportvectorclassifier/modelparameters-swift.struct/featurerescaling.md)
- [var maxIterations: Int](mlsupportvectorclassifier/modelparameters-swift.struct/maxiterations.md)
- [var penalty: Double](mlsupportvectorclassifier/modelparameters-swift.struct/penalty.md)
- [var validation: MLSupportVectorClassifier.ModelParameters.ValidationData](mlsupportvectorclassifier/modelparameters-swift.struct/validation.md)
  Validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsupportvectorclassifier/modelparameters-swift.struct/validationdata-swift.property)*