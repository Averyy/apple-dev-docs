# validationData

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

Validation data represented as a `MLDataTable`.

**Availability**:
- macOS 10.14+ - Deprecated in 10.15

> **Deprecated**: Use the validation property instead.

## Declaration

```swift
var validationData: MLDataTable? { get set }
```

#### Discussion

> **Note**: Setting this to `nil` means that the training data will be automatically split for validation. Setting it to an empty table means to not use a validation set.

## See Also

### Accessing parameters
- [var convergenceThreshold: Double](./convergencethreshold.md)
- [var featureRescaling: Bool](./featurerescaling.md)
- [var maxIterations: Int](./maxiterations.md)
- [var penalty: Double](./penalty.md)
- [var validation: MLSupportVectorClassifier.ModelParameters.ValidationData](./validation.md)
  Validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsupportvectorclassifier/modelparameters-swift.struct/validationdata-swift.property)*