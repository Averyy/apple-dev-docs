# validationData

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

Validation data represented as a `MLDataTable`.

**Availability**:
- iOS 15.0+ - Deprecated in 16.0
- iPadOS 15.0+ - Deprecated in 16.0
- Mac Catalyst 15.0+ - Deprecated in 16.0
- macOS 10.14+ - Deprecated in 10.15
- visionOS 1.0+

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
- [var l1Penalty: Double](./l1penalty.md)
- [var l2Penalty: Double](./l2penalty.md)
- [var maxIterations: Int](./maxiterations.md)
- [var stepSize: Double](./stepsize.md)
- [var validation: MLLogisticRegressionClassifier.ModelParameters.ValidationData](./validation.md)
  Validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mllogisticregressionclassifier/modelparameters-swift.struct/validationdata-swift.property)*