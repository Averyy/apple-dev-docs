# init(validationData:maxDepth:minLossReduction:minChildWeight:randomSeed:)

**Framework**: Create ML  
**Kind**: init

Creates a new set of parameters.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
init(validationData: MLDataTable?, maxDepth: Int = 6, minLossReduction: Double = 0, minChildWeight: Double = 0.1, randomSeed: Int = 42)
```

## Parameters

- `validationData`: The dataset used to monitor how well the model is generalizing. The default value is `nil` which will use an automatically sampled validation set.
- `maxDepth`: The maximum depth of the tree. Must be a value of at least 1. The default value is 6.
- `minLossReduction`: The minimum amount of reduction to the loss function that is required to make another node to split the data. Larger values help prevent overfitting. The default value is 0.
- `minChildWeight`: Determines the minimum weight of each leaf node of the tree. Larger values help prevent overfitting. The default value is 0.1.
- `randomSeed`: A seed for internal random operations. Set this value to ensure reproducible results. The default value is 42.

## See Also

- [init(validation: MLDecisionTreeClassifier.ModelParameters.ValidationData, maxDepth: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int)](mldecisiontreeclassifier/modelparameters-swift.struct/init(validation:maxdepth:minlossreduction:minchildweight:randomseed:).md)
- [MLDecisionTreeClassifier.ModelParameters.ValidationData](mldecisiontreeclassifier/modelparameters-swift.struct/validationdata-swift.enum.md)
  Values for specifying validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldecisiontreeclassifier/modelparameters-swift.struct/init(validationdata:maxdepth:minlossreduction:minchildweight:randomseed:))*