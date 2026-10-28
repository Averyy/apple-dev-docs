# validation

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

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

## Discussion

The default is `.split(strategy: .automatic)`, which automatically generates the validation dataset from 0% to 10% of the training dataset.

## See Also

### Accessing parameters
- [var validationData: MLDataTable?](./validationdata-swift.property.md)
  Validation data represented as a `MLDataTable`.
- [var maxIterations: Int](./maxiterations.md)
- [var l1Penalty: Double](./l1penalty.md)
- [var l2Penalty: Double](./l2penalty.md)
- [var stepSize: Double](./stepsize.md)
- [var convergenceThreshold: Double](./convergencethreshold.md)
- [var featureRescaling: Bool](./featurerescaling.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mllinearregressor/modelparameters-swift.struct/validation)*