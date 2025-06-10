# validationData

**Framework**: Create ML  
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

- [var convergenceThreshold: Double](mllogisticregressionclassifier/modelparameters-swift.struct/convergencethreshold.md)
- [var featureRescaling: Bool](mllogisticregressionclassifier/modelparameters-swift.struct/featurerescaling.md)
- [var l1Penalty: Double](mllogisticregressionclassifier/modelparameters-swift.struct/l1penalty.md)
- [var l2Penalty: Double](mllogisticregressionclassifier/modelparameters-swift.struct/l2penalty.md)
- [var maxIterations: Int](mllogisticregressionclassifier/modelparameters-swift.struct/maxiterations.md)
- [var stepSize: Double](mllogisticregressionclassifier/modelparameters-swift.struct/stepsize.md)
- [var validation: MLLogisticRegressionClassifier.ModelParameters.ValidationData](mllogisticregressionclassifier/modelparameters-swift.struct/validation.md)
  Validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mllogisticregressionclassifier/modelparameters-swift.struct/validationdata-swift.property)*