# randomSeed

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

The seed value for random operations during tree building process.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var randomSeed: Int
```

## Discussion

Set the random seed value to ensure results are reproducible.

## See Also

### Accessing parameters
- [var validationData: MLDataTable?](./validationdata-swift.property.md)
  The data used for the validation set to inform the model training process.
- [var maxDepth: Int](./maxdepth.md)
  The maximum depth of the tree. Must be greater than 0.
- [var minLossReduction: Double](./minlossreduction.md)
  The minimum amount that the loss needs to be reduced to create a new split.
- [var minChildWeight: Double](./minchildweight.md)
  The minimum weight of each leaf node.
- [var validation: MLDecisionTreeClassifier.ModelParameters.ValidationData](./validation.md)
  Validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldecisiontreeclassifier/modelparameters-swift.struct/randomseed)*