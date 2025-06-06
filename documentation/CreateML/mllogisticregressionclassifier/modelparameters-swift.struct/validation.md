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
var validation: MLLogisticRegressionClassifier.ModelParameters.ValidationData { get set }
```

#### Discussion

The default is `.split(strategy: .automatic)`, which automatically generates the validation dataset from 0% to 10% of the training dataset.

## See Also

- [var convergenceThreshold: Double](mllogisticregressionclassifier/modelparameters-swift.struct/convergencethreshold.md)
- [var featureRescaling: Bool](mllogisticregressionclassifier/modelparameters-swift.struct/featurerescaling.md)
- [var l1Penalty: Double](mllogisticregressionclassifier/modelparameters-swift.struct/l1penalty.md)
- [var l2Penalty: Double](mllogisticregressionclassifier/modelparameters-swift.struct/l2penalty.md)
- [var maxIterations: Int](mllogisticregressionclassifier/modelparameters-swift.struct/maxiterations.md)
- [var stepSize: Double](mllogisticregressionclassifier/modelparameters-swift.struct/stepsize.md)
- [var validationData: MLDataTable?](mllogisticregressionclassifier/modelparameters-swift.struct/validationdata-swift.property.md)
  Validation data represented as a `MLDataTable`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mllogisticregressionclassifier/modelparameters-swift.struct/validation)*