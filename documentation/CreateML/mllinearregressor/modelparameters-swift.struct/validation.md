# validation

**Framework**: Create ML  
**Kind**: property

Validation data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var validation: MLLinearRegressor.ModelParameters.ValidationData { get set }
```

#### Discussion

The default is `.split(strategy: .automatic)`, which automatically generates the validation dataset from 0% to 10% of the training dataset.

## See Also

- [var validationData: MLDataTable?](mllinearregressor/modelparameters-swift.struct/validationdata-swift.property.md)
  Validation data represented as a `MLDataTable`.
- [var maxIterations: Int](mllinearregressor/modelparameters-swift.struct/maxiterations.md)
- [var l1Penalty: Double](mllinearregressor/modelparameters-swift.struct/l1penalty.md)
- [var l2Penalty: Double](mllinearregressor/modelparameters-swift.struct/l2penalty.md)
- [var stepSize: Double](mllinearregressor/modelparameters-swift.struct/stepsize.md)
- [var convergenceThreshold: Double](mllinearregressor/modelparameters-swift.struct/convergencethreshold.md)
- [var featureRescaling: Bool](mllinearregressor/modelparameters-swift.struct/featurerescaling.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mllinearregressor/modelparameters-swift.struct/validation)*