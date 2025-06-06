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
var validation: MLDecisionTreeRegressor.ModelParameters.ValidationData { get set }
```

#### Discussion

The default is `.split(strategy: .automatic)`, which automatically generates the validation dataset from 0% to 10% of the training dataset.

## See Also

- [var maxDepth: Int](mldecisiontreeregressor/modelparameters-swift.struct/maxdepth.md)
- [var minChildWeight: Double](mldecisiontreeregressor/modelparameters-swift.struct/minchildweight.md)
- [var minLossReduction: Double](mldecisiontreeregressor/modelparameters-swift.struct/minlossreduction.md)
- [var randomSeed: Int](mldecisiontreeregressor/modelparameters-swift.struct/randomseed.md)
- [var validationData: MLDataTable?](mldecisiontreeregressor/modelparameters-swift.struct/validationdata-swift.property.md)
  Validation data represented as a `MLDataTable`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldecisiontreeregressor/modelparameters-swift.struct/validation)*