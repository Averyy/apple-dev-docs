# validationData

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

The data used for the validation set to inform the model training process.

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

## See Also

### Accessing parameters
- [var maxDepth: Int](./maxdepth.md)
  The maximum depth of the tree. Must be greater than 0.
- [var minLossReduction: Double](./minlossreduction.md)
  The minimum amount that the loss needs to be reduced to create a new split.
- [var minChildWeight: Double](./minchildweight.md)
  The minimum weight of each leaf node.
- [var randomSeed: Int](./randomseed.md)
  The seed value for random operations during tree building process.
- [var validation: MLDecisionTreeClassifier.ModelParameters.ValidationData](./validation.md)
  Validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldecisiontreeclassifier/modelparameters-swift.struct/validationdata-swift.property)*