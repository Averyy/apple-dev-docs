# validation

**Framework**: Create ML  
**Kind**: property

Validation data.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var validation: MLSupportVectorClassifier.ModelParameters.ValidationData { get set }
```

#### Discussion

The default is `.split(strategy: .automatic)`, which automatically generates the validation dataset from 0% to 10% of the training dataset.

## See Also

- [var convergenceThreshold: Double](mlsupportvectorclassifier/modelparameters-swift.struct/convergencethreshold.md)
- [var featureRescaling: Bool](mlsupportvectorclassifier/modelparameters-swift.struct/featurerescaling.md)
- [var maxIterations: Int](mlsupportvectorclassifier/modelparameters-swift.struct/maxiterations.md)
- [var penalty: Double](mlsupportvectorclassifier/modelparameters-swift.struct/penalty.md)
- [var validationData: MLDataTable?](mlsupportvectorclassifier/modelparameters-swift.struct/validationdata-swift.property.md)
  Validation data represented as a `MLDataTable`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsupportvectorclassifier/modelparameters-swift.struct/validation)*