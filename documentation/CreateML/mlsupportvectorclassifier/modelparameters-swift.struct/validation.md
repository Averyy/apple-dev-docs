# validation

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

Validation data.

**Availability**:
- macOS 10.15+ - Deprecated in 14.0

## Declaration

```swift
var validation: MLSupportVectorClassifier.ModelParameters.ValidationData { get set }
```

#### Discussion

The default is `.split(strategy: .automatic)`, which automatically generates the validation dataset from 0% to 10% of the training dataset.

## See Also

### Accessing parameters
- [var convergenceThreshold: Double](./convergencethreshold.md)
- [var featureRescaling: Bool](./featurerescaling.md)
- [var maxIterations: Int](./maxiterations.md)
- [var penalty: Double](./penalty.md)
- [var validationData: MLDataTable?](./validationdata-swift.property.md)
  Validation data represented as a `MLDataTable`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsupportvectorclassifier/modelparameters-swift.struct/validation)*