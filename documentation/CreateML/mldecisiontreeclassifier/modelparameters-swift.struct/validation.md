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
var validation: MLDecisionTreeClassifier.ModelParameters.ValidationData { get set }
```

#### Discussion

The default is `.split(strategy: .automatic)`, which automatically generates the validation dataset from 0% to 10% of the training dataset.

## See Also

- [var validationData: MLDataTable?](mldecisiontreeclassifier/modelparameters-swift.struct/validationdata-swift.property.md)
  The data used for the validation set to inform the model training process.
- [var maxDepth: Int](mldecisiontreeclassifier/modelparameters-swift.struct/maxdepth.md)
  The maximum depth of the tree. Must be greater than 0.
- [var minLossReduction: Double](mldecisiontreeclassifier/modelparameters-swift.struct/minlossreduction.md)
  The minimum amount that the loss needs to be reduced to create a new split.
- [var minChildWeight: Double](mldecisiontreeclassifier/modelparameters-swift.struct/minchildweight.md)
  The minimum weight of each leaf node.
- [var randomSeed: Int](mldecisiontreeclassifier/modelparameters-swift.struct/randomseed.md)
  The seed value for random operations during tree building process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldecisiontreeclassifier/modelparameters-swift.struct/validation)*