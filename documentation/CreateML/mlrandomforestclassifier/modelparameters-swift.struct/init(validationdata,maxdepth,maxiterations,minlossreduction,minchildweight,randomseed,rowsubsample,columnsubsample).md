# init(validationData:maxDepth:maxIterations:minLossReduction:minChildWeight:randomSeed:rowSubsample:columnSubsample:)

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
init(validationData: MLDataTable?, maxDepth: Int = 6, maxIterations: Int = 10, minLossReduction: Double = 0, minChildWeight: Double = 0.1, randomSeed: Int = 42, rowSubsample: Double = 0.8, columnSubsample: Double = 0.8)
```

## Parameters

- `validationData`: The dataset used to monitor how well the model is generalizing. The default value is `nil` which will use an automatically sampled validation set.
- `maxDepth`: The maximum depth of the tree. Must be a value of at least 1. The default value is 6.
- `maxIterations`: The maximum number of passes through the data. The default value is 10.
- `minLossReduction`: The minimum amount of reduction in the loss function that is required to make another split to the data. Larger values help prevent overfitting. The default value is 0.
- `minChildWeight`: Determines the minimum weight of each leaf node of the tree. Larger values help prevent overfitting. The default value is 0.1.
- `randomSeed`: A seed for internal random operations. Set this value to ensure reproducible results. The default value is 42.
- `rowSubsample`: Select the specified ratio from the training set to grow each tree. This technique is known as bagging. The default value is 0.8.
- `columnSubsample`: Select the specified ratio of columns from the training set to use when growing each tree. Similar to row subsampling, this can be used to prevent overfitting. The default value is 0.8

## See Also

- [init(validation: MLRandomForestClassifier.ModelParameters.ValidationData, maxDepth: Int, maxIterations: Int, minLossReduction: Double, minChildWeight: Double, randomSeed: Int, rowSubsample: Double, columnSubsample: Double)](mlrandomforestclassifier/modelparameters-swift.struct/init(validation:maxdepth:maxiterations:minlossreduction:minchildweight:randomseed:rowsubsample:columnsubsample:).md)
- [MLRandomForestClassifier.ModelParameters.ValidationData](mlrandomforestclassifier/modelparameters-swift.struct/validationdata-swift.enum.md)
  Values for specifying validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrandomforestclassifier/modelparameters-swift.struct/init(validationdata:maxdepth:maxiterations:minlossreduction:minchildweight:randomseed:rowsubsample:columnsubsample:))*